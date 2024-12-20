"""VOEvent Server Blueprint."""

import picologging as logging
from pymongo.errors import PyMongoError
from sanic import Blueprint
from sanic.log import logger
from sanic.request import Request
from sanic.response import json as json_response
from sanic_ext import openapi

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()

voe = Blueprint("voe", url_prefix="/")


# Post at /create_voe
@voe.post("create_voe")
@openapi.response(201, description="Creates an FRB VOEvent.")
# Process a new VOEvent (validate, send to Comet, send to Email, save to MongoDB)
async def create_voe(request: Request):
    """Process a VOEvent.

    Args:
        request (Request): The request object.
        voe_event (VOEvent): The VOEvent to be processed.

    Returns:
        JSON response: A JSON response containing the inserted ID if successful,
        or an error message if there was an issue.

    Raises:
        Exception: If there is an error inserting the VOEvent into MongoDB.
        PyMongoError: If there is an error with the PyMongo library.

    """
    # Validate the VOEvent
    try:
        log.info("Validating the VOEvent")
        voevent = VOEvent(**request.json)
        validation_status = "Success"
        status_code = 200
    except Exception as validation_error:
        log.exception(f"Error while validating the VOEvent: {validation_error}")
        validation_status = "Failure"
        status_code = 400

    # Send VOEvent to Comet
    try:
        log.info("Sending the VOEvent to Comet")
        voevent.send_comet
        comet_status = "Success"
    except Exception as comet_error:
        log.exception(f" While sending the VOEvent to Comet: {comet_error}")
        comet_status = "Failure"
        status_code = 500
    # Send VOEvent to Email
    try:
        log.info("Sending the VOEvent to Email")
        voevent.send_email
        email_status = "Success"
    except Exception as email_error:
        log.exception(f" While sending the VOEvent to Email: {email_error}")
        email_status = "Failure"
        status_code = 500

    # Save VOEvent to MongoDB
    # DB Name: frbvoe, Collection: voe, Document: VOEvent Payload Dict
    try:
        log.info("Saving the VOEvent to MongoDB")
        mongo = request.app.ctx.mongo
        insert_result = await mongo["frbvoe"]["voe"].insert_one(voevent.model_dump())
        database_status = "Success"
    except (Exception, PyMongoError) as mongo_error:
        log.exception(f" While saving the VOEvent to MongoDB: {mongo_error}")
        database_status = "Failure"
        status_code = 500

    print(
        f"""Validation: {validation_status}\n
        Comet: {comet_status}\n
        Email : {email_status}\n
        Database : {database_status}"""
    )

    return json_response(
        {
            "validation": validation_status,
            "comet": comet_status,
            "email": email_status,
            "database": database_status,
            "id": insert_result.inserted_id,
        },
        status=status_code,
    )


# Post at /delete_voe
@voe.post("delete_voe")
@openapi.response(201, description="Deletes an FRB VOEvent.")
# Delete a VOEvent from the MongoDB
async def delete_voe(request: Request):
    """Delete a VOE document from the database.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: The HTTP response object.

    Raises:
        HTTPException: If the request is missing the 'id' parameter.
        HTTPException: If there is an error deleting the document from the database.
    """
    if "id" not in request.args.keys():
        return json_response({"message": "Your request needs an ID."}, status=400)
    id = request.args["id"]
    mongo = request.app.ctx.mongo
    try:
        delete_result = await mongo["frbvoe"]["voe"].delete_one({"id": id})
    except (Exception, PyMongoError) as mongo_error:
        logger.error(f"{mongo_error} on /voe")
        return json_response({"message": mongo_error}, status=500)

    return json_response({"message": delete_result.delete_count}, status=202)
