import unittest
from unittest.mock import patch
from frbvoe.utilities.TNSAgent import TNSAgent

class TestTNSAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TNSAgent()

    def test_set_api_key(self):
        api_key = "my_api_key"
        self.agent.set_api_key(api_key)
        self.assertEqual(self.agent.api_key, api_key)

    def test_set_tns_id(self):
        tns_id = "my_tns_id"
        self.agent.set_tns_id(tns_id)
        self.assertEqual(self.agent.tns_id, tns_id)

    def test_set_bot_name(self):
        bot_name = "my_bot_name"
        self.agent.set_bot_name(bot_name)
        self.assertEqual(self.agent.bot_name, bot_name)

    def test_set_tns_marker(self):
        self.agent.set_tns_marker()
        self.assertIsNotNone(self.agent.tns_marker)

    def test_set_sandbox(self):
        self.agent.set_sandbox()
        self.assertEqual(self.agent.url, "https://sandbox.wis-tns.org/api")

    def test_set_live(self):
        self.agent.set_live()
        self.assertEqual(self.agent.url, "https://www.wis-tns.org/api")

    def test_format_payload(self):
        payload = {"key": "value"}
        formatted_payload = self.agent.format_payload(payload)
        self.assertEqual(formatted_payload, '{"key": "value"}')

    @patch("frbvoe.utilities.TNSAgent.requests.get")
    def test_try_get_tns_name(self, mock_get):
        json_data = {"name": "FRB123"}
        mock_get.return_value.json.return_value = json_data
        tns_name = self.agent.try_get_tns_name(json_data)
        self.assertEqual(tns_name, "FRB123")

    @patch("frbvoe.utilities.TNSAgent.requests.Response")
    def test_check_response(self, mock_response):
        mock_response.status_code = 200
        self.assertTrue(self.agent.check_response(mock_response))

    @patch("frbvoe.utilities.TNSAgent.requests.get")
    def test_get_bulk_report_reply(self, mock_get):
        report_id = "123"
        mock_get.return_value.status_code = 200
        response = self.agent.get_bulk_report_reply(report_id)
        self.assertEqual(response.status_code, 200)

    @patch("frbvoe.utilities.TNSAgent.requests.get")
    def test_print_bulk_report_reply(self, mock_get):
        report_id = "123"
        mock_get.return_value.json.return_value = {"reply": "Success"}
        with patch("builtins.print") as mock_print:
            self.agent.print_bulk_report_reply(report_id)
            mock_print.assert_called_with("Reply: Success")

    @patch("frbvoe.utilities.TNSAgent.requests.post")
    def test_send_report(self, mock_post):
        payload = {"key": "value"}
        mock_post.return_value.status_code = 200
        self.assertTrue(self.agent.send_report(payload))

    @patch("frbvoe.utilities.TNSAgent.requests.post")
    def test_search_by_internal_name(self, mock_post):
        payload = {"name": "FRB123"}
        mock_post.return_value.json.return_value = {"result": "Found"}
        result = self.agent.search_by_internal_name(payload)
        self.assertEqual(result, "Found")

    def test_change_prop_period(self):
        payload = {"key": "value"}
        self.assertTrue(self.agent.change_prop_period(payload))

    def test_reset(self):
        self.agent.reset()
        self.assertIsNone(self.agent.api_key)
        self.assertIsNone(self.agent.tns_id)
        self.assertIsNone(self.agent.bot_name)
        self.assertIsNone(self.agent.tns_marker)
        self.assertIsNone(self.agent.url)
        self.assertIsNone(self.agent.tns_name)
        self.assertIsNone(self.agent.report_id)
        self.assertIsNone(self.agent.id_code)
        self.assertIsNone(self.agent.id_message)
        self.assertEqual(self.agent.sleep_interval, 0)
        self.assertEqual(self.agent.loop_counter, 0)
        self.assertEqual(self.agent.http_errors, {})


if __name__ == "__main__":
    unittest.main()