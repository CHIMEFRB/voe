"""VOEvent Server Blueprint."""

import picologging as logging
from pymongo.errors import PyMongoError
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json as json_response
from sanic_ext import openapi

from frbvoe.models.tns import TNS

logging.basicConfig()
log = logging.getLogger()

tns = Blueprint("tns", url_prefix="/")


# Post at /submit_tns
@tns.post("submit_tns")
@openapi.response(201, description="Submits an FRB to the TNS.")
# Validate the TNS report, submit to the TNS, and save the TNS name to the MongoDB
async def submit_tns(
    request: Request, proprierary_period: int = 10, sandbox: bool = True
):
    """Submits a TNS (Transient Name Server) report.

    Args:
        request (Request): The request object.
        proprierary_period (int, optional): The proprietary period for the TNS report.
        Defaults to 10.
        sandbox (bool, optional): If true, submits the report to the TNS sandbox.
        Defaults to True.

    Returns:
        dict: A dictionary containing the validation status,
        TNS status, database status, and the inserted ID.
    """
    # Validate the VOEvent
    try:
        log.info("Validating the TNS Report")
        tns_report = TNS(**request.json)
        validation_status = "Success"
        status_code = 200
    except Exception as validation_error:
        log.exception(f"Error while validating the VOEvent: {validation_error}")
        validation_status = "Failure"
        status_code = 400

    # Submit to the TNS
    try:
        log.info("Submitting the VOEvent to TNS")
        tns_report.submit(proprierary_period, sandbox)
        tns_status = "Success"
    except Exception as tns_error:
        log.exception(f" While sending the VOEvent to the TNS: {tns_error}")
        tns_status = "Failure"
        status_code = 500

    # Save VOEvent to MongoDB
    # DB Name: frbvoe, Collection: tns, Document: TNS Name Dict
    try:
        log.info("Saving the TNS name to MongoDB")
        mongo = request.app.ctx.mongo
        insert_result = await mongo["frbvoe"]["tns"].insert_one(tns_report.model_dump())
        database_status = "Success"
    except (Exception, PyMongoError) as mongo_error:
        log.exception(f" While saving the TNS name to MongoDB: {mongo_error}")
        database_status = "Failure"
        status_code = 500

    print(
        f"""Validation: {validation_status}\n
        TNS: {tns_status}\n
        Database : {database_status}"""
    )

    return json_response(
        {
            "validation": validation_status,
            "tns": tns_status,
            "database": database_status,
            "id": insert_result.inserted_id,
        },
        status=status_code,
    )
