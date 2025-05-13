"""Module to parse a log file and throw a warning or an error based on duration."""

import argparse
from datetime import datetime, timedelta


def main():
    """Main"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-log-file", required=True, help="Full path to the application log file")
    args = parser.parse_args()

    processed_task = {}

    with open(args.app_log_file, encoding="utf-8") as log_file_handler:
        for line in log_file_handler:
            start_time, task_name, action, pid = line.strip().split(",")
            start_time = datetime.strptime(start_time, "%H:%M:%S")

            # Each time we processed a log(we have a new current time) - with this,
            # check the duration for the old running processes
            now = start_time
            for process, data in processed_task.items():
                if (
                    now - data["start_time"] > timedelta(minutes=5)
                    and not data["warning"]
                ):
                    print(f"WARNING: {process} is taking more than 5 minutes!")
                    data["warning"] = True
                if (
                    now - data["start_time"] > timedelta(minutes=10)
                    and not data["error"]
                ):
                    print(f"ERROR: {process} is taking more than 10 minutes!")
                    data["error"] = True
                    # Once the error treshold was reached, process can be deleted
                    # from the processed_task for memory/time optimizations.

            # We are looking only for processes that have started and adding them into a 'stack'
            if action.strip() == "START":
                processed_task[(task_name, pid)] = {
                    "start_time": start_time,
                    "warning": False,
                    "error": False,
                }
            else:
                processed_task.pop((task_name, pid), None)


if __name__ == "__main__":
    main()
