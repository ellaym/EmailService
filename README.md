
# EmailService

EmailService is a Flask-based application that allows users to send emails via an API. It uses Flask-Mail to handle email delivery and is Dockerized for ease of deployment.

## Features
- Send emails with customizable subjects and messages via a simple POST request.
- Configurable SMTP settings via a `.env` file.
- Dockerized for easy deployment and scaling.

## Project Structure
```bash
EmailService/
├── app
│   ├── email_service.py  # Handles email sending logic
│   ├── __init__.py       # Initializes Flask and Flask-Mail
│   ├── __pycache__/      # Python cache files (ignored in Git)
│   └── routes.py         # Defines API endpoints for sending emails
├── Dockerfile            # Docker image setup
├── docker-compose.yml    # Docker Compose setup
├── main.py               # Entry point for the Flask application
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (excluded from Git)
```

## Prerequisites

1. Python 3.9 or higher
2. Docker (optional for running the app in a container)
3. Docker Compose (optional, simplifies Docker setup)
4. A valid SMTP server and credentials

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/EmailService.git
cd EmailService
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory with the following content:
```
# SMTP Configuration
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
EMAIL_USER=your-email@example.com
EMAIL_PASS=your-email-password

# Flask Configuration
FLASK_PORT=5501
```

### 3. Install Dependencies (if not using Docker)
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application (without Docker)
```bash
python main.py
```

The app will be accessible at `http://localhost:5501`.

## Docker Setup

### 1. Build the Docker Image
```bash
docker build -t emailservice .
```

### 2. Run the Docker Container
```bash
docker run -d -p 5501:5501 --env-file .env emailservice
```

The application will now be accessible at `http://localhost:5501` in the Docker container.

## Docker Compose Setup (Recommended)

For easier setup and management, you can use Docker Compose. A `docker-compose.yml` file is provided.

### 1. Run the Application with Docker Compose
```bash
docker-compose up
```

Docker Compose will:
- Build the Docker image
- Expose the app on port 5501
- Load environment variables from the `.env` file

The application will be accessible at `http://localhost:5501`.

### 2. Stopping the Application
To stop the application, run:
```bash
docker-compose down
```

This will stop and remove the container.

## API Endpoints

### POST `/send`
Sends an email to the specified recipient.

**Payload**:
```json
{
    "email": "recipient@example.com",
    "message": "This is the email body.",
    "subject": "Optional subject (defaults to 'No Subject')"
}
```

**Response**:
- Success: `200 OK` with a message confirming the email was sent.
- Failure: `400 Bad Request` if the email or message fields are missing, or `500 Internal Server Error` if an issue occurs when sending the email.

## Environment Variables

This project uses a `.env` file to manage sensitive information such as SMTP credentials. Ensure you do not share this file or its contents.

### Required Variables:
- `SMTP_SERVER`: Your SMTP server (e.g., `smtp.gmail.com`).
- `SMTP_PORT`: SMTP server port (usually `587` for TLS).
- `EMAIL_USER`: Your email username (e.g., `example@gmail.com`).
- `EMAIL_PASS`: Your email password or app-specific password.

### Optional Variables:
- `FLASK_PORT`: Port on which the Flask app runs (default: `5501`).

## License
This project is licensed under the MIT License.
