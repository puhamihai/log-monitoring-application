import subprocess
import sys
from pathlib import Path

def test_script__logs_default():
    script_path = Path(__file__).parents[1] / "log_monitoring_application.py"
    log_file = Path(__file__).parent / "logs-default.log"

    process = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--app-log-file",
            log_file,
        ],
        capture_output=True,
        text=True,
    )

    logs = [log.split(":")[0] for log in process.stdout.strip().split("\n")]

    assert logs.count("WARNING") == 21
    assert logs.count("ERROR") == 11


def test_script__logs_1_warning():
    script_path = Path(__file__).parents[1] / "log_monitoring_application.py"
    log_file = Path(__file__).parent / "logs-1-warning.log"

    process = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--app-log-file",
            log_file,
        ],
        capture_output=True,
        text=True,
    )

    logs = [log.split(":")[0] for log in process.stdout.strip().split("\n")]

    assert logs.count("WARNING") == 1
    assert logs.count("ERROR") == 1
