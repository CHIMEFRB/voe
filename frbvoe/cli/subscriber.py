"""Subscriber CLI."""

import click

from frbvoe.backend.subscriber import add_subscriber, delete_subscriber


@click.group(name="subscriber", help="Subscriber Tools.")
def subscriber():
    """Manage subscribers."""
    pass


@subscriber.command("add", help="Add a subscriber to the database.")
@click.option("--subscriber_name", help="Name of the subscriber.")
@click.option("--subscriber_email", help="Email address of the subscriber.")
def add(subscriber_name, subscriber_email):
    """Add subscriber."""
    add_subscriber(subscriber_name, subscriber_email)
    click.echo(
        f"Saved subscriber {subscriber_name}"
        f"with email {subscriber_email} to the database."
    )


def delete(subscriber_name, subscriber_email):
    """Delete subscriber."""
    delete_subscriber(subscriber_name, subscriber_email)
    click.echo(
        f"Deleted subscriber {subscriber_name}"
        f"with email {subscriber_email} from the database."
    )
