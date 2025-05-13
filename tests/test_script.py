import subprocess
import sys


def test_script__logs_default():
    process = subprocess.run(
        [
            sys.executable,
            "../log_monitoring_application.py",
            "--app-log-file",
            "logs-default.log",
        ],
        capture_output=True,
        text=True,
    )

    logs = [log.split(":")[0] for log in process.stdout.strip().split("\n")]

    assert logs.count("WARNING") == 21
    assert logs.count("ERROR") == 11


def test_script__logs_1_warning():
    process = subprocess.run(
        [
            sys.executable,
            "../log_monitoring_application.py",
            "--app-log-file",
            "logs-1-warning.log",
        ],
        capture_output=True,
        text=True,
    )

    logs = [log.split(":")[0] for log in process.stdout.strip().split("\n")]

    assert logs.count("WARNING") == 1
    assert logs.count("ERROR") == 1
