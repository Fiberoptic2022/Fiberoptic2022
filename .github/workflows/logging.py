import datetime
import csv

# Define the file path for the alert log
alert_log_file = "closed_alert_log.csv"

# Open the alert log file in append mode
with open(alert_log_file, mode='a', newline='') as f:
    writer = csv.writer(f)

    # Use a while loop to prompt the user for input multiple times
    while True:
        # Ask the user for input
        alert_link = input('Enter the alert link: ')
        alert_type = input('Enter the alert type: ')
        alert_description = input('Enter the alert description: ')
        alert_severity = input('Enter the alert severity: ')
        alert_disposition = input('Enter the alert disposition: ')
        alert_disposition_note = input('Enter reason for the disposition: ')
        alert_suppressed = input('Enter Y if the alert was suppressed or N if it was not: ')


        # Get the current date and time
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Write the alert information to the CSV file
        writer.writerow([timestamp, alert_link, alert_type, alert_description, alert_severity, alert_disposition, alert_disposition_note, alert_suppressed])

        # Print a confirmation message
        print(f'Alert logged at {timestamp}')

        # Ask the user if they want to log another alert
        user_input = input('Do you want to log another alert? (y/n): ')

        # Check if the user wants to continue
        if user_input.lower() != 'y':
            break

# Print a final message when the loop is exited
print('Logging complete')