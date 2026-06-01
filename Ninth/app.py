from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Gmail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'parthbadgujar1@gmail.com'
app.config['MAIL_PASSWORD'] = 'yjkz hkln jlfp flxp'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        receiver = request.form['email']

        msg = Message(
            subject='Test Email from Flask',
            sender=app.config['MAIL_USERNAME'],
            recipients=[receiver]
        )

        msg.body = "Hello! This email was sent using Flask."

        mail.send(msg)

        return "Email Sent Successfully!"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)