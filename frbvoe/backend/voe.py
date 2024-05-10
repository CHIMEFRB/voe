"""VOEvent Server Blueprint."""

from pymongo.errors import PyMongoError
from sanic import Blueprint
from sanic.log import logger
from sanic.request import Request
from sanic.response import json as json_response
from sanic_ext import openapi

import picologging as logging
logging.basicConfig()
log = logging.getLogger()

from frbvoe.models.comet import Comet
from frbvoe.models.email import Email
from frbvoe.models.voe import VOEvent

voe = Blueprint("voe", url_prefix="/")

# Post at /create_voe
@voe.post("create_voe")
@openapi.response(201, description="Validates VOEvent data from a host observatory.")
# Add the validated payload to the MongoDB Database
async def create_voe(request: Request): #TODO: Shiny, should I add voe_event: VOEvent?
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
    log.info("Processing VOEvent")
    voe = VOEvent(**request.json)
    print(voe.json())
    
    

    # Send VOEvent to Comet
    # comet_report = Comet(**request.json)
    # comet_report.send

    # Send VOEvent to Email
    email_report = Email(**request.json)
    email_report.send

    # Add VOEvent to MongoDB
    # Database Name: frbvoe
    # Collection Name: voe
    # Document -> VOEvent Payload Dict.
    mongo = request.app.ctx.mongo
    try:
        insert_result = await mongo["frbvoe"]["voe"].insert_one(voe.model_dump())
    except (Exception, PyMongoError) as mongo_error:
        logger.error(f"{mongo_error} on /voe")
        return json_response({"message": mongo_error}, status=500)

    return json_response({"id": insert_result.inserted_id}, status=201)


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
