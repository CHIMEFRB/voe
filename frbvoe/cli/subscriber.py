"""Subscriber CLI."""

import click

@click.group(name="subscriber", help="Subscriber Tools.")

def subscriber():
    """Manage subscribers."""
    pass

@subscriber.command("add", help="Add a subscriber to the database.")
@click.option("--subscriber_name", help="Name of the subscriber.")
@click.option("--subscriber_email", help="Email address of the subscriber.")

def add(subscriber_name, subscriber_email):
    """Add subscriber."""
    click.echo(f"Saved subscriber {subscriber_name} with email {subscriber_email} to the database.")
    
def remove(subscriber_name, subscriber_email):
    """Remove subscriber."""
    click.echo(f"Removed subscriber {subscriber_name} with email {subscriber_email} from the database.")