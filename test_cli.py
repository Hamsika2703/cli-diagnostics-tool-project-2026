import json
import os
import diagnostics_tool.cli as cli

from diagnostics_tool.cli import main


def test_main():
    result = main()
    assert result == 0
    assert os.path.exists("diagnostics_report.json")
    assert os.path.exists("diagnostics_report.txt")


def test_json_report_contains_system_info():
    main()

    with open("diagnostics_report.json", "r", encoding="utf-8") as file:
        report = json.load(file)

    assert "system" in report
    assert "python_version" in report
    assert "machine" in report
    assert "developer_tools" in report


def test_text_report_exists():
    main()

    with open("diagnostics_report.txt", "r", encoding="utf-8") as file:
        content = file.read()

    assert "SYSTEM DIAGNOSTICS REPORT" in content


def test_missing_developer_tool():
    original_which = cli.shutil.which

    try:
        cli.shutil.which = lambda tool: None
        result = cli.main()
        assert result == 0
    finally:
        cli.shutil.which = original_which

def test_invalid_directory(monkeypatch):
    def raise_os_error():
        raise OSError("Invalid directory")

    monkeypatch.setattr(cli.os, "getcwd", raise_os_error)

    result = cli.main()

    assert result == 1