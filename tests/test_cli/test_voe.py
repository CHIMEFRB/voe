from click.testing import CliRunner

from frbvoe.cli.voe import send, voe


def test_voe():
    runner = CliRunner()
    result = runner.invoke(voe, ["--help"])
    assert result.exit_code == 0
    assert "Usage: voe [OPTIONS]" in result.output


def test_send():
    runner = CliRunner()
    result = runner.invoke(send, ["--help"])
    assert result.exit_code == 0
    assert "Usage: send [OPTIONS]" in result.output
