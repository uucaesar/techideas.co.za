from flask import Flask, render_template, request, redirect
import smtplib, ssl, os
from email.mime.text import MIMEText

app = Flask(__name__)
application = app  # For compatibility with some deployment setups

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    
    elif request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        enquiry = request.form["message"]

        # --- Email Server Settings ---
        host = "mail.techideas.co.za"
        port = 465  # Standard port for sending mail with STARTTLS
        
        # IMPORTANT: Replace these with a real email account and password hosted on techideas.co.za
        EMAIL_USERNAME = "no-reply@techideas.co.za" 
        EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")  # It's best practice to store sensitive information like passwords in environment variables

        FROM = "No Reply <no-reply@techideas.co.za>"
        TO = "techideas2@gmail.com"

        # Create a MIMEText object with the message body
        msg = MIMEText(f"Sender's Name: {name} \n\nEmail: {email}\n\nEnquiry: {enquiry}")

        # Set the headers
        msg['Subject'] = f"New Message From {name}"
        msg['From'] = FROM
        msg['To'] = TO

        try:
            # 1. Connect to the server using the designated port
            server = smtplib.SMTP(host, port)
            
            # 2. Secure the connection (Required before logging in)
            server.starttls()
            
            # 3. Authenticate with the server (This fixes the "Relay access denied" error)
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

            # 4. Send the email
            server.sendmail(FROM, TO, msg.as_string())

            # 5. Quit the server
            server.quit()

            return f"Thank you for contacting us {name}! We will get back to you soon. "
            
        except Exception as e:
            # If something goes wrong, it will print the exact reason here instead of a 500 error
            return f"<h1>Error sending email</h1><p>The server returned this error: <b>{e}</b></p>"

if __name__ == '__main__':
    app.run(debug=True)