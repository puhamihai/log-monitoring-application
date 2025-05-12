# Log Monitoring Application

Current script monitor a log file to check if a certain process reached a treshold, if the job is running for more than 5 minutes, it will throw a __warning__. If it is running for more than 10 minutes it will throw an __error__.

It was designed to not have memory overflow because of the filelog size, it's not loading the logfile entirely in the memory, but sequentially parsing and processing the logs.

## Usage
```bash
➜ python3 log_monitoring_application.py --help
usage: log_monitoring_application.py [-h] --app-log-file APP_LOG_FILE

options:
  -h, --help            show this help message and exit
  --app-log-file APP_LOG_FILE
                        Full path to the application log file

➜ python3 log_monitoring_application.py --app-log-file <path-to-log-file>
```