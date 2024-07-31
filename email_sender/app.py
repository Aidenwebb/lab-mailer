from flask import Flask, render_template, request
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtpd import SMTPServer
import asyncore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    sender_email = "your_email@example.com"
    receiver_email = email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('localhost', 1025) as server:
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return "Email sent successfully!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
