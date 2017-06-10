from twilio.base.exceptions import TwilioException
from twilio.rest import Client

from .twilio_errors import TwilioCredentialError


class FlaskNotify:
    _config = {}

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self._config.update(twilio_sid=app.config.get('TWILIO_SID'),
                            twilio_token=app.config.get('TWILIO_TOKEN'),
                            twilio_number=app.config.get('TWILIO_NUMBER'),
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

    def send_mailtrap_email(self):
        pass

