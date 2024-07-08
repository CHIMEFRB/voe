from click.testing import CliRunner

from frbvoe.cli.main import cli


def test_version_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert "FRB VOE version" in result.output
