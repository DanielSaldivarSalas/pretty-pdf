from typer.testing import CliRunner

from .main import app
from click.testing import Result

runner = CliRunner()


def test_app():
    # given
    cli_arguments = ["greeter", "Daniel", "--city", "Paris"]

    # when
    result: Result = runner.invoke(app, cli_arguments)

    # then
    assert result.exit_code == 0
    assert "Hello Daniel" in result.stdout
    assert "Let's have coffee in Paris."
    print(result)
