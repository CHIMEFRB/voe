"""VOE CLI."""

import click


@click.group(name="voe", help="VOEvent Tools.")
def voe():
    """Manage workflow pipelines."""
    pass


@voe.command("send", help="Send VOEvent.")
@click.option("--hostname", default="localhost", help="Destination to send the VOE.")
@click.option("--port", default=8098, help="Port to send the VOE.")
@click.option(
    "--file",
    default="./voe",
    type=click.File("r"),
    help="VOEvent file.",
    show_default=True,
)
def send(hostname, port):
    """Send VOEvent."""
    click.echo(f"Send VOEvent.{hostname}:{port}")
