"""FRB VOE CLI."""

import click

from frbvoe.cli.subscriber import subscriber
from frbvoe.cli.tns import tns
from frbvoe.cli.voe import voe


@click.group()
def cli():
    """FRB VOE Command Line Interface."""
    pass


@cli.command("version", help="FRB VOE version.")
def version():
    """FRB VOE version."""
    click.echo("VOEvent Tools v0.1.0")


cli.add_command(voe)
cli.add_command(tns)
cli.add_command(subscriber)
