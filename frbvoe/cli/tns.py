"""TNS CLI."""

import click

from frbvoe.backend.tns import TNS


@click.group(name="tns", help="TNS Tools.")
def tns():
    """Manage workflow pipelines."""
    pass

@tns.command("submit", help="Submit an FRB to the TNS.")
@click.option(
    "--period",
    default=10,
    help="Proprietary period of the FRB.",
    show_default=True
    )
@click.option(
    "--sandbox",
    help="Submit to the sandbox TNS (if True) or live TNS (if False).",
    show_default=True,
    )

def submit(proprietary_period, sandbox):
    """Submit an FRB to the TNS."""
    TNS.submit(proprietary_period, sandbox)
