import pytest
from click.testing import CliRunner
from quasar.cli import smell
from quasar.cli import SmellType, FormatterType


def test_smell_with_class_smell_type() -> None:
    runner = CliRunner()
    result = runner.invoke(
        smell, ['.', '--recursive', SmellType.CLASS.value, '--output', 'json'])
    assert result.exit_code == 0


def test_smell_with_method_smell_type() -> None:
    runner = CliRunner()
    result = runner.invoke(
        smell, ['.', '--recursive', SmellType.METHOD.value, '--output', 'json'])
    assert result.exit_code == 0


def test_smell_with_invalid_smell_type() -> None:
    runner = CliRunner()
    result = runner.invoke(
        smell, ['.', '--recursive', 'INVALID', '--output', 'json'])
    assert result.exit_code == 2
    assert "Invalid smell_type. Choices are CLASS or METHOD." in result.output


def test_smell_with_invalid_path() -> None:
    runner = CliRunner()
    result = runner.invoke(
        smell, ['invalid_path', SmellType.CLASS.value, '--recursive', '--output', 'json'])
    assert result.exit_code == 2
    assert "Invalid value for 'PATH'" in result.output


def test_smell_with_non_directory_path() -> None:
    runner = CliRunner()
    result = runner.invoke(
        smell, ['.', '--recursive', SmellType.CLASS.value, '--output', 'json'])
    assert result.exit_code == 2
    assert "Path is not a directory." in result.output