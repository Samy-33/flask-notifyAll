import smtplib
from email.mime.text import MIMEText

from twilio.base.exceptions import TwilioException
from twilio.rest import Client

from .error import FlaskNotifyEmailError, TwilioCredentialError

"""
Notice: Add helper functions to the twilio service.
"""


class FlaskNotify:
    _config = {}

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self._config.update(twilio_sid=app.config.get('TWILIO_SID'),
                            twilio_token=app.config.get('TWILIO_TOKEN'),
                            twilio_number=app.config.get('TWILIO_NUMBER'),
                            test_email=app.config.get('TEST_EMAIL'),
                            mailtrap_user=app.config.get('MAILTRAP_USER'),
                            mailtrap_pass=app.config.get('MAILTRAP_PASSWORD'))

    def send_sms_notification(self, to_user, body):
        try:
            client = Client(
                self._config.get('twilio_sid'),
                self._config.get('twilio_token')
            )
        except TwilioException:
            raise TwilioCredentialError

        client.messages.create(from_=self._config.get('twilio_number'),
                               to=to_user,
                               body=body)

    def send_verification_code(self, to_user, code):
        self.send_sms_notification(
            to_user=to_user,
            body='Your verification code is {}'.format(code))
        return code

    def send_mailtrap_email(self, to_user, message, subject, email_port=2525):

        if not isinstance(to_user, list):
            raise FlaskNotifyEmailError('Argument \'to_user\' must be a list')

        user_name = self._config.get('mailtrap_user')
        password = self._config.get('mailtrap_pass')
        test_email = self._config.get('test_email')

        emails_to_string = ', '.join(to_user)

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = test_email
        msg['To'] = emails_to_string

        mail = smtplib.SMTP('smtp.mailtrap.io', email_port)
        mail.login(user_name, password)
        mail.sendmail(test_email, to_user, msg.as_string())
        mail.quit()
