import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "orpita17@cse.pstu.ac.bd"
EMAIL_PASSWORD = "udvi wpvq vwyt qnwb"
contacts = ['abidakhan98763@gmail.com']

def is_valid_email(email):
    # Simple email validation using '@' and '.'
    return '@' in email and '.' in email

invalid_emails = [email for email in contacts if not is_valid_email(email)]
if invalid_emails:
    print("Invalid email addresses:", invalid_emails)
    exit()

msg = EmailMessage()
msg['Subject'] = 'Sending to Multiple Receivers'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ", ".join(contacts)
msg.set_content('Documents Attached.......')

files = ['1902004.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(file)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Additional attachments (images)
image_files = ['image.jpg']
for file in image_files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = file.split('.')[-1]  # Extracting file extension to determine subtype
        file_name = os.path.basename(file)
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

