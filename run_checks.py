"""Run the lab checks locally; this does not validate Jenkins itself."""

import json
from pathlib import Path
import platform
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
COMMANDS = [
    ("environment", ["-m", "pip", "freeze"]),
    ("lint", ["-m", "flake8", "app.py", "deploy.py", "tests",
              "run_checks.py"]),
    ("tests", ["-m", "pytest", "-v", "--junitxml=reports/junit.xml"]),
    ("coverage_run", ["-m", "coverage", "run", "-m", "pytest", "-v"]),
    ("coverage_html", ["-m", "coverage", "html", "--fail-under=0"]),
    ("coverage_xml", ["-m", "coverage", "xml", "--fail-under=0"]),
    ("coverage_json", ["-m", "coverage", "json", "--fail-under=0",
                       "-o", "reports/coverage.json"]),
    ("coverage_report", ["-m", "coverage", "report", "-m",
                         "--fail-under=90"]),
    ("security", ["-m", "bandit", "app.py", "deploy.py", "-f", "json",
                  "-o", "reports/bandit.json"]),
    ("deploy", ["deploy.py"]),
    ("deployed_app", ["deployment/current/app.py"]),
]


def main():
    """Record actual commands, output and exit codes, stopping on failure."""
    reports = ROOT / "reports"
    reports.mkdir(exist_ok=True)
    summary = {
        "kind": "Local Python checks only; Jenkins has not been run",
        "python": sys.version,
        "platform": platform.platform(),
        "commands": [],
    }
    for name, arguments in COMMANDS:
        command = [sys.executable, *arguments]
        result = subprocess.run(
            command, cwd=ROOT, capture_output=True, text=True,
            encoding="utf-8", errors="replace", check=False,
        )
        output = result.stdout + result.stderr
        transcript = (
            f"LOCAL CHECK: {name}\n"
            f"Command: python {' '.join(arguments)}\n"
            f"Exit code: {result.returncode}\n\n{output}"
        )
        (reports / f"{name}.txt").write_text(transcript, encoding="utf-8")
        print(transcript)
        summary["commands"].append({
            "name": name, "arguments": arguments,
            "exit_code": result.returncode,
        })
        (reports / "local_validation.json").write_text(
            json.dumps(summary, indent=2) + "\n", encoding="utf-8"
        )
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
