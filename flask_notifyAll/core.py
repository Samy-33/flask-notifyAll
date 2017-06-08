from twilio.rest import Client


class FlaskNotify:
    _config = {}

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        twilio_sid = app.config.get('TWILIO_SID')
        twilio_token = app.config.get('TWILIO_TOKEN')
        twilio_number = app.config.get('TWILIO_NUMBER')
        self._config.update(TWILIO_SID=twilio_sid,
                            TWILIO_TOKEN=twilio_token,
                            TWILIO_NUMBER=twilio_number)

    def send_sms_notification(self, to_user, body):
        client = Client(
            self._config.get('TWILIO_SID'),
            self._config.get('TWILIO_TOKEN')
        )

        client.messages.create(from_=self._config.get('TWILIO_NUMBER'),
                               to=to_user,
                               body=body)
