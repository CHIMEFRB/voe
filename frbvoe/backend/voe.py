"""VOEvent Server Blueprint."""

from sanic import Blueprint
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic.response import json as json_response
from sanic_ext import openapi
from pymongo.errors import PyMongoError

from frbvoe.models.voe import VOEvent
from frbvoe.utilities.senders import send_to_comet

voe = Blueprint("voe", url_prefix="/")


# Post at /voe
@voe.post("voe")
@openapi.response(201, description="Validates data from the telescope.")
# Add the validated payload to the MongoDB Database
async def create_voe(request: Request, voe_event: VOEvent):

    mongo = request.app.ctx.mongo
    request.app.add_task(send_to_comet(voe_event.model_dump()))
    # Database Name: frbvoe
    # Collection Name: voe
    # Document -> VOEvent Payload Dict.
    try:
        insert_result = await mongo["frbvoe"]["voe"].insert_one(voe_event.model_dump())
    except (Exception, PyMongoError) as mongo_error:
        logger.error(f"{mongo_error} on /voe")
        return json_response({"message": mongo_error}, status=500)

    return json_response({"id": insert_result.inserted_id}, status=201)


async def delete_voe(request: Request):

    # /voe?id=<id>
    if "id" not in request.args.keys():
        return json_response(
            {"message": "Your request needs an ID."}, status=400
        )
    id = request.args["id"]
    mongo = request.app.ctx.mongo
    try:
        delete_result = await mongo["frbvoe"]["voe"].delete_one({"id": id})
    except (Exception, PyMongoError) as mongo_error:
        logger.error(f"{mongo_error} on /voe")
        return json_response({"message": mongo_error}, status=500)

    return json_response({"message": delete_result.delete_count}, status=202)
