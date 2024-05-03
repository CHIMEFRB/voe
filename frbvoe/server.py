"""Buckets Server."""

from asyncio import AbstractEventLoop
from functools import partial

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
from sanic import Sanic
from sanic.log import logger
from sanic.worker.loader import AppLoader

from frbvoe.models.voe import VOEvent
from frbvoe.backend.voe import voe as voe_blueprint


async def mongo(app: Sanic, loop: AbstractEventLoop) -> None:
    """Connect to the database.

    Args:
        app (Sanic): The application.
        loop (AbstractEventLoop): The event loop.
    """
    # SANIC_MONGODB_HOSTNAME
    hostname = str(app.config.get("MONGODB_HOSTNAME", "localhost"))
    # SANIC_MONGODB_PORT
    port = int(app.config.get("MONGODB_PORT", 27017))
    # SANIC_MONGODB_USERNAME
    username = app.config.get("MONGODB_USERNAME", "")
    # SANIC_MONGODB_PASSWORD
    password = app.config.get("MONGODB_PASSWORD", "")
    try:
        logger.debug(f"Connecting to MongoDB at {hostname}:{port}")
        client = AsyncIOMotorClient(
            host=hostname, port=port, username=username, password=password, io_loop=loop
        )
        await client.admin.command("ping")
        logger.debug("MongoDB Connection Established")
        app.ctx.mongo = client
    except ConnectionFailure as error:
        logger.error(error)
        logger.debug("MongoDB Connection Failed")


async def inject_dependencies(app: Sanic):
    """Adds dependencies for route handlers to the app.

    Parameters
    ----------
    app : Sanic
        Sanic application.
    loop : AbstractEventLoop
        Event loop.
    """
    logger.info("Injecting dependencies.")
    app.ext.add_dependency(VOEvent, VOEvent.compile)


def create(name: str = "frbvoe", debug: bool = False) -> Sanic:
    """Create the buckets server.

    Args:
        debug (bool, optional): Whether to enable debug mode.
            Defaults to False.

    Returns:
        Sanic: The buckets server.
    """
    app = Sanic(name)
    logger.propagate = False
    app.config.CORS_ORIGINS = "*"  # CORS
    app.config.HEALTH = True
    app.config.HEALTH_ENDPOINT = True
    app.ctx.debug = debug
    app.config.FALL
    BACK_ERROR_FORMAT = "json"
    # ? Blueprints
    app.blueprint(voe_blueprint)
    # ? Listeners
    app.register_listener(mongo, "before_server_start")
    return app


if __name__ == "__main__":
    loader = AppLoader(factory=partial(create))
    server: Sanic = loader.load()
    server.prepare(
        host=server.config.get("HOSTNAME", "localhost"),  # type: ignore
        port=server.config.get("PORT", 8002),  # type: ignore
        access_log=server.config.get("ACCESS_LOG", False),
        auto_reload=server.config.get("AUTO_RELOAD", True),
        debug=server.config.get("DEBUG", True),
    )
    Sanic.serve(primary=server, app_loader=loader)
