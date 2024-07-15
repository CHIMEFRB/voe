from click.testing import CliRunner

from frbvoe.cli.tns import submit


def test_tns_submit():
    runner = CliRunner()
    result = runner.invoke(submit, ["--help"])
    assert result.exit_code == 0
    assert "Usage: submit [OPTIONS]" in result.output
