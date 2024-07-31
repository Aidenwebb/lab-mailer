# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install flask

# Expose ports for Flask and SMTP server
EXPOSE 5000 1025

# Start the SMTP server and the Flask application
CMD ["sh", "-c", "python email_sender/smtp_server.py & python email_sender/app.py"]
