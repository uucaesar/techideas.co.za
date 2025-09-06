from flask import Flask, render_template, request, redirect
import smtplib, ssl
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

        host = "mail.apsystems.africa"
        server = smtplib.SMTP(host)
        FROM = "No Reply <no-reply@apsystems.africa>"
        TO = "cgama@apsystems.africa"

        #Create a MIMEText object with the message body
        msg = MIMEText(f"Sender's Name: {name} \n\nEmail: {email}\n\nEnquiry: {enquiry}")

        # Set the headers
        msg['Subject'] = f"New Message From {name}"
        msg['From'] = FROM
        msg['To'] = TO

        #Send the email
        server.sendmail(FROM, TO, msg.as_string())

        server.quit()

        return f"Thank you for contacting us {name}! We will get back to you soon. "

if __name__ == '__main__':
    app.run(debug=True)