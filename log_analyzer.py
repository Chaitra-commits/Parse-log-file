import re
import json
from collections import Counter

def read_log_file(log_file):
    """
    It will read the log file to analyze log levels, services, and error messages.

    argument : log_file(the name of the log file)

    Functionality:
    Reads the log file line by line.
    Uses regex pattern to extract log details and match with each line
    Counts log levels, services, and ERROR messages
    Handles malformed lines gracefully and logs a warning
    Result is loaded in JSON format with counts for log levels and services,
          and the most common ERROR message (if any).

    Returns:
            None: Output a JSON data to the console and writes it to the output.json file.

    """

    # Regex pattern to match log lines
    log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (\w+) - (.+)$")

    # Counting for log levels, services and ERROR
    log_level_count = Counter()
    service_count = Counter()
    error_msg = Counter()

    try:
        with open(log_file, "r") as log_file:
            for line in log_file:
                line = line.strip()

                # Match the line with the pattern
                match = log_pattern.match(line)
                if match:
                    timestamp, service_name, log_level, message = match.groups()

                    # Count the log levels
                    log_level_count[log_level] += 1

                    # Count the services
                    service_count[service_name] += 1

                    #count the Error log level
                    if log_level == "ERROR":
                        error_msg[message] += 1
                else:
                    print(f"Malformed line: {line}")

        #create dict to format it in readable way
        my_dict = {
            "log_level_count": dict(log_level_count),
            "service_count": dict(service_count),
            "most_common_error_msg" : (
                {"message": error_msg.most_common(1)[0][0],
                    "occurrences": error_msg.most_common(1)[0][1]
                }
                if error_msg else None
                )

        }

        # Print the my_dict data
        print("\nmy_dict:")
        result = json.dumps(my_dict, indent=4)
        print(result)

        # write result data to a json file as output.json
        with open("output.json", "w") as json_file:
            json_file.write(result)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Running script from command line and taking input as log file for read_log_file function
    """
    log_file = "app.log"  
    read_log_file(log_file)