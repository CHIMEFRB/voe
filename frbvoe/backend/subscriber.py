"""Subscriber Server Blueprint."""

import picologging as logging
from pymongo.errors import PyMongoError
from sanic import Blueprint
from sanic.log import logger
from sanic.request import Request
from sanic.response import json as json_response
from sanic_ext import openapi

from frbvoe.models.subscriber import Subscriber

logging.basicConfig()
log = logging.getLogger()

voe = Blueprint("voe", url_prefix="/")


# Post at /add_subscriber
@voe.post("add_subscriber")
@openapi.response(
    201, description="Adds or removes a subscriber from the VOEvent server."
)
# Add the subscriber payload to the MongoDB Database
async def add_subscriber(request: Request):
    """Adds a subscriber document to the database.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: The HTTP response object.
    """
    # Validate the Subscriber
    try:
        log.info("Validating the Subscriber")
        subscriber = Subscriber(**request.json)
        validation_status = "Success"
        status_code = 200
    except Exception as validation_error:
        log.exception(f"Error while validating the Subscriber: {validation_error}")
        validation_status = "Failure"
        status_code = 400

    # Save Subscriber to MongoDB
    # DB Name: frbvoe, Collection: subscriber, Document: Subscriber Payload Dict
    try:
        mongo = request.app.ctx.mongo
        log.info("Saving the Subscriber to MongoDB")
        mongo = request.app.ctx.mongo
        insert_result = await mongo["frbvoe"]["subscriber"].insert_one(
            subscriber.model_dump()
        )
        database_status = "Success"
    except (Exception, PyMongoError) as mongo_error:
        log.exception(f" While saving the Subscriber to MongoDB: {mongo_error}")
        database_status = "Failure"
        status_code = 500

    return json_response(
        {
            "validation": validation_status,
            "database": database_status,
            "id": insert_result.inserted_id,
        },
        status=status_code,
    )


# Post at /delete_subscriber
@voe.post("delete_subscriber")
@openapi.response(201, description="Deletes an FRB VOEvent subscriber.")
# Delete a VOEvent from the MongoDB
async def delete_subscriber(request: Request):
    """Delete a subscriber from the database.

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
        delete_result = await mongo["frbvoe"]["subscriber"].delete_one({"id": id})
    except (Exception, PyMongoError) as mongo_error:
        logger.error(f"{mongo_error} on /subscriber")
        return json_response({"message": mongo_error}, status=500)

    return json_response({"message": delete_result.delete_count}, status=202)
