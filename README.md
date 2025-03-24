# Parse-log-file
Log file analyzer

How to run script

1. Save the script as log_analyzer.py.
2. Place the app.log file in same dict or add path of app.log file.
3. Run the script from the command line
		python log_analyzer.py
4. The script will print the result and save it as output.json.

Assumptions:
1. The regex pattern is handles as (YYYY-MM-DD HH:MM:SS - ServiceName - LogLevel - Message)
2. Malformed lines are logged as warnings and skipped
3. The JSON is saved to the current working directory as output.json
