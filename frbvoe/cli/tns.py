"""TNS CLI."""

import click


@click.group(name="tns", help="TNS Tools.")
def tns():
    """Manage workflow pipelines."""
    pass


@tns.command("submit", help="Submit an FRB to the TNS.")
@click.option("--username", help="TNS username.")
@click.option(
    "--period", default=2, help="Proprietary period of the FRB.", show_default=True
)
@click.option(
    "--sandbox", help="Set to False when submitting to the live TNS.", show_default=True
)
def send(username, period, sandbox):
    """submit an FRB to the TNS."""
    click.echo(f"submit FRB to TNS. {username} {period} {sandbox}")
