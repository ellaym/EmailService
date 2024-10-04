# app/routes.py
from flask import Blueprint, request, jsonify
from app.email_service import send_email
import logging

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@main.route('/send', methods=['POST'])
def handle_message():
    """API endpoint to handle email sending.

    This function handles the POST request to send an email. It expects a JSON payload
    containing the following fields:
    - message: The content of the email message.
    - email: The target email address.
    - subject (optional): The subject of the email. If not provided, it defaults to 'No Subject'.

    Returns:
        A JSON response with the following structure:
        - If the email is sent successfully:
            {
                'message': 'Message sent to {email}'
            }
        - If there is an error sending the email:
            {
                'error': 'Failed to send email',
                'message': str(e)
            }
        - If the request payload is missing required fields:
            {
                'error': 'Message and target email address are required'
            }
    """
    data = request.get_json()
    message = data.get('message')
    email = data.get('email')
    subject = data.get('subject', 'No Subject')

    if not message or not email:
        logging.error('Missing email or message')
        return jsonify({'error': 'Message and target email address are required'}), 400

    try:
        logging.info(f'Sending email to {email}')
        send_email(to_email=email, subject=subject, message=message)
        return jsonify({'message': f'Message sent to {email}'}), 200
    except Exception as e:
        logging.error(f'Failed to send email: {str(e)}')
        return jsonify({'error': 'Failed to send email', 'message': str(e)}), 500
