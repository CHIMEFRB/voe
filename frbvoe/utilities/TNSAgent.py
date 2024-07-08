"""TNS Agent class modelled on public TNS script [1]."""

import json
import logging
import tempfile
import time
from collections import OrderedDict
from typing import Union

import requests

logging.basicConfig(format="%(levelname)s:%(message)s")
log = logging.getLogger(__name__)


class TNSAgent:
    """Utility class for interfacing with the Transient Name Server.

    Args:
        debug : bool, default=True
            Verbose printing in debug mode.

    Attributes:
        api_key : str
            The TNS User Group API key, generated upon creation of the
            TNS bot, using the TNS web portal. Keep it secret.

        tns_id : str
            Unique ID corresponding to the user's TNS
            API bot. Required for authenticating requests to the
            TNS.

        bot_name : str
            Name of the user's TNS API bot as it appears on the TNS.

        tns_marker : str
            TNS marker for User-Agent string. See [2].

        url : str
            Base TNS URL, can be set to the sandbox or live site.

        tns_name : str
            The official TNS name for the submitted FRB.

        report_id : str
            The TNS report ID assigned to a newly submitted FRB report.
            Should be saved for reference to contact TNS regarding problems.

        id_code : str
            The HTTP request error code value returned from the attempt
            to send the FRB JSON report to the TNS.

        id_message : str
            The HTTP request error code message returned from
            the attempt to send the FRB JSON report to the TNS.

        sleep_interval : int
            Wait this many seconds for the TNS to update before checking
            the status of a submitted FRB JSON report.

        loop_counter : int
            How many times to check the TNS after FRB JSON report submission
            for the report to have been successfully uploaded. Each loop
            sleeps for a number of seconds equal to `self.sleep_interval`.

        http_errors : dict, int : str
            Look-up reference for the meaning of HTTP errors coming out
            of the TNS API endpoints.

    References:
        Core python components generously provied by the TNS developers at
        [1] https://wis-tns.weizmann.ac.il/content/tns-getting-started
        [2] https://sandbox.wis-tns.org/content/tns-newsfeed

    """

    def __init__(self, debug: bool = True) -> None:
        """Initialize a TNS agent."""
        self.debug: bool = debug

        self.sleep_interval: int = 5  # seconds
        self.loop_counter: int = 2  # number of times to check TNS response

        self.http_errors: dict = {
            304: "Error 304: Not Modified: There was no new data to return.",
            400: "Error 400: Bad Request: The request was invalid.",
            401: "Error 401: Unauthorized: Double check your TNS credentials",
            403: "Error 403: Forbidden: Request understood, but refused.",
            404: "Error 404: Not Found: Request invalid or resource does not exist.",
            500: "Error 500: Internal Server Error: Contact TNS developers.",
            503: "Error 503: Unavailable: TNS is unavailable.",
        }
        self._introspect()

        # The following attributes should be reset after any actions.
        self.url: Union[None, str] = None
        self.tns_name: Union[None, str] = None
        self.report_id: Union[None, str] = None
        self.id_code: Union[None, str] = None
        self.id_message: Union[None, str] = None

    def _introspect(self) -> None:
        if self.debug:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.ERROR)

    def set_api_key(self, api_key: str) -> None:
        """Set the TNS API key.

        Every group in the TNS must have
        a unique API key, and it must be kept secret to avoid
        duplication or impersonation.

        Args:
            api_key : str
                The API key for the TNS bot representing the group
                uploading their FRB JSON reports.

        """
        log.info("Setting TNS API key")
        self.api_key: str = api_key

    def set_tns_id(self, tns_id: str) -> None:
        """Set the TNS bot ID.

        Every group in the TNS must use a
        bot for API submissions. The ID is usually equal to
        the TNS group ID.

        Args:
            tns_id : str
                The unique ID assigned to the TNS group's API bot.

        """
        log.info("Setting TNS bot ID")
        self.tns_id: str = tns_id

    def set_bot_name(self, bot_name: str) -> None:
        """Set the TNS bot name.

        Every group in the TNS must use a
        bot for API submissions. The name is assigned by the TNS
        user that creates the bot for the TNS group.

        Args:
            bot_name : str
                The name of the TNS group's API bot.

        """
        log.info("Setting TNS bot name")
        self.bot_name: str = bot_name

    def set_tns_marker(self) -> None:
        """Set the TNS marker, part of the header for all TNS requests."""
        self.tns_marker: str = (
            'tns_marker{"tns_id": "'
            + str(self.tns_id)
            + '", "type": "bot", "name": "'
            + self.bot_name
            + '"}'
        )

    def set_sandbox(self) -> None:
        """Set the URL to the TNS Sandbox (for testing only)."""
        url = "https://sandbox.wis-tns.org/api"
        log.info(f"Setting TNS URL to {url}")
        self.url = url

    def set_live(self) -> None:
        """Set the URL to the TNS live system (for real submissions only)."""
        url = "https://www.wis-tns.org/api"
        log.info(f"Setting TNS URL to {url}")
        self.url = url

    def format_payload(self, payload: dict) -> str:
        """Cast FRB payload to string format of TNS FRB JSON standard.

        Args:
            payload : dict
                The dictionary payload to be converted
                to the string format expected by the TNS
                endpoints.

        Returns:
            formatted : str
                The input dictionary transformed to a
                properly formatted string that is acceptable
                to the TNS endpoints.

        """
        # Need to convert the payload to a string so it can be properly accepted
        log.info("Dumping FRB JSON report to string format")
        tf = tempfile.TemporaryFile(mode="r+")  # Readable and writeable
        tf.write(json.dumps(payload, indent=2))
        tf.seek(0)  # Without this, the file will appear empty
        parsed = json.loads(tf.read(), object_pairs_hook=OrderedDict)
        formatted = json.dumps(parsed, indent=2)
        return formatted

    def try_get_tns_name(
        self,
        json_data,
    ):
        """Try to find the TNS name from the JSON response.

        Args:
            json_data : dict
                JSON response data from bulk-report-reply.

        Returns:
            tns_name: str
                Name of the TNS event.

        """
        log.info("Trying to find TNS name in the JSON respose")
        tns_name = None
        try:
            data = json_data["data"]["feedback"]["frb_report"][0]
            for item in data:
                if item == "100":
                    tns_name = data[item]["objname"]
                    log.info("Found TNS name in the JSON response")
        except Exception as e:
            log.error(f"Failed to read TNS name from JSON response due to: {e}")
        finally:
            return tns_name

    def check_response(self, response: requests.Response) -> bool:
        """Check response from TNS API endpoint.

        Return True only if the TNS API endpoint handled the
        request without internal errors.

        Args:
            response : requests.Response
                The input is the response from the requests module
                after calling a GET, POST, etc.

        Returns:
            bool
                True, if no external or internal HTTP errors were made
                when handling the request represented by the input response.
                False, otherwise.

        """
        status_code = int(response.status_code)
        if status_code == 200:
            json_data = response.json()
            self.id_code = str(json_data["id_code"])
            self.id_message = str(json_data["id_message"])
            log.info(f"The TNS response ID code is: {self.id_code}")
            log.info(f"The TNS reponse ID message is: {self.id_message}")
            if self.id_code == "200" and self.id_message == "OK":
                return True
            elif self.id_code == "400" and self.id_message == "Bad request":
                # The following is a special case and may need help from TNS developers.
                return False
            else:
                return False
        else:
            # Check if the status is among other possible known HTTP errors.
            if status_code in list(self.http_errors.keys()):
                log.error(
                    list(self.http_errors.values())[
                        list(self.http_errors.keys()).index(status_code)
                    ]
                )
            else:
                log.error(
                    "Undocumented error. Retain the report ID to contact the TNS."
                )
            return False

    def get_bulk_report_reply(self, report_id: str) -> requests.Response:
        """Get the reply for a given FRB JSON report by its ID number.

        Args:
            report_id : str
                The ID number for the report.

        Returns:
            dict
                The response from the '/bulk-report-reply' endpoint.

        """
        reply_data = {"api_key": self.api_key, "report_id": report_id}
        url = f"{self.url}/bulk-report-reply"
        log.info(f"Getting bulk report reply from URL {url} for {reply_data}")
        headers = {"User-Agent": self.tns_marker}
        response = requests.post(url, headers=headers, data=reply_data)
        return response

    def print_bulk_report_reply(self, report_id: str) -> None:
        """Print the reply from the TNS for a submitted FRB JSON report.

        Args:
            report_id : int
                The ID number for the FRB JSON report.

        """
        log.info(f"Getting reply for the report with ID {report_id}.")
        reply_resp = self.get_bulk_report_reply(report_id)
        reply_resp_check = self.check_response(reply_resp)
        if reply_resp_check is True:
            log.info("The report was successfully processed on the TNS.")
            json_data = reply_resp.json()
            log.info(f"JSON reponse: {json_data}")
            self.tns_name = self.try_get_tns_name(json_data)
        else:
            log.error(
                "There was a problem processing the report on the TNS. "
                + "Check response messages before reattempting submission. "
                + "Retain the report ID to contact TNS developers."
            )
            response_dict = reply_resp.json()
            output = json.dumps(response_dict, indent=2)
            log.error(f"Response from /bulk-report-reply: {output}")

    def send_report(self, payload: dict) -> bool:
        """Use `/bulk-report` endpoint to submit an FRB report.

        The response messages will contain the TNS name
        when the submission is successful.

        Args:
            payload : dict
                Use frb_voe.utilities.tns_validators.Report
                to pass a correctly formatted payload.

        Returns:
            bool
                If the request to the TNS API was successful, print
                the JSON response and return True. Else, print the
                error and return False.

        """
        try:
            formatted = self.format_payload(payload)
            log.info(
                "Sending the following data to the TNS: {}".format(
                    formatted,
                )
            )
            # TNS Group API key
            send_data = [("api_key", (None, self.api_key)), ("data", (None, formatted))]
            headers = {"User-Agent": self.tns_marker}
            url = f"{self.url}/bulk-report"
            response = requests.post(url, headers=headers, files=send_data)
            log.info(f"Checking response from '{url}'")
            json_data = response.json()
            response_check = self.check_response(response)

            if response_check is True:
                log.info("The report was succesfully sent to the TNS.")
                log.info(f"\t--> JSON response: {json_data}")
                # Obtain the report ID from the JSON response
                report_id = str(json_data["data"]["report_id"])
                log.info(f"The TNS report ID is: {report_id}")
                self.report_id = report_id
                # Sleep while waiting for the recently submitted report
                # to show up at the TNS; then ask for feedback on the
                # submission using the report ID
                log.info(
                    "Looping for TNS response: {} times ({} s per loop).".format(
                        self.loop_counter,
                        self.sleep_interval,
                    )
                )
                counter = 0
                looping = True
                while looping:
                    # Ensure the report was accepted by checking TNS periodically.
                    time.sleep(self.sleep_interval)
                    reply_response = self.get_bulk_report_reply(report_id)
                    reply_resp_check = self.check_response(reply_response)
                    if reply_resp_check is False or counter >= self.loop_counter:
                        looping = False
                    counter += 1
                log.info(
                    "Wake up! Print the reply from TNS for report ID {}".format(
                        report_id
                    )
                )
                # N.B. Here we just need the base URL, not the `/bulk-report` URL
                self.print_bulk_report_reply(report_id)
                log.info(f"JSON response from request to {url}:\n{response.json()}")
                return True
            else:
                log.error("The report was not sent to the TNS!")
                log.error(f"JSON response: {json_data}")
                return False
        except Exception as e:
            log.error(f"Caught exception while sending FRB JSON report: {e}")
            return False

    def search_by_internal_name(self, payload: dict) -> str:
        """Search TNS for an FRB object by its internal name.

        Args:
            payload : dict
                Dict with primary key equal to internal name given
                to the FRB prior to TNS submission.
                Each TNS Group is liable to track this differently.

        Returns:
            found_name : str, default="UNKNOWN"
                TNS object name matching the given `internal_name`.

        """
        internal_name = payload["internal_name"]

        search_obj = [
            ("internal_name", internal_name),
        ]
        json_file = OrderedDict(search_obj)
        # TNS Group API Key
        input_data = {"api_key": self.api_key, "data": json.dumps(json_file)}
        log.info(
            "Getting response from {url} with input {input}".format(
                url=f"{self.url}/get/search",
                input=input_data,
            )
        )
        headers = {"User-Agent": self.tns_marker}
        log.info(f"**** HEADERS ****: {headers}")
        search_url = f"{self.url}/get/search"
        found_name = "UNKNOWN"

        try:
            resp = requests.post(
                search_url,
                headers=headers,
                data=input_data,
            )
            resp_json = json.loads(resp.text)
            log.info(f"Got response from {search_url} with code {resp.status_code}")
            log.info(f"JSON response: {resp_json}")
            # TNS name is listed under "objnames"
            objnames = []
            for item in resp_json["data"]["reply"]:
                objnames.append(item["objname"])
            log.info(
                "Got {} TNS name(s) for {}: {}".format(
                    len(objnames),
                    internal_name,
                    objnames,
                )
            )
            found_name = objnames[0]
        except Exception as e:
            log.error(
                "Could not search the TNS for {} at {} due to: {}".format(
                    internal_name,
                    search_url,
                    e,
                )
            )
            if resp.status_code in self.http_errors:
                log.error(
                    f"Corresponding error code: {self.http_errors[resp.status_code]}"
                )

        return found_name

    def change_prop_period(self, payload: dict) -> bool:
        """Change the end date for the proprietary period for 
        a previously submitted FRB.

        Use cases include:
        (1) Extending the proprietary period until the
        data is ready to be made public.
        (2) Changing to the next UTC
        day in order to stage a public release of FRBs on the TNS.

        Args:
            payload : dict
                Dictionary formitted data subject to data validation.

        Returns:
            bool
               If the request to the TNS API succeeds, print JSON response
               and return True. Else, print the error and return False.

        """
        try:
            url = f"{self.url}/set/prop-period"
            # Convert payload to JSON format
            json_file = OrderedDict(payload)
            data = {"api_key": self.api_key, "data": json.dumps(json_file)}
            headers = {"User-Agent": self.tns_marker}
            log.info(
                f"Getting response from {url} with input {data} and headers {headers}"
            )
            # Update proprietary period by POST request to TNS API
            response = requests.post(
                url,
                headers=headers,
                data=data,
            )
            response.raise_for_status()
            parsed = json.loads(response.text, object_pairs_hook=OrderedDict)
            json_data = json.dumps(parsed, indent=2)
            log.info(f"JSON response: {json_data}")
            return True
        except Exception as e:
            log.error(f"Request to {url} failed due to: {e}")
            return False

    def reset(self) -> None:
        """Reset these attributes after any action is performed.

        Resets the URL, TNS name, and FRB JSON report response
        details, to allow recycling the object instance.
        """
        self.url = None
        self.tns_name = None
        self.report_id = None
        self.id_code = None
        self.id_message = None
