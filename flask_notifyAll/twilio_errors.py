_twilio_cred_msg = """\
You don't add Twilio credentials into your config file or object
"""


class TwilioCredentialError(Exception):
    def __str__(self):
        return _twilio_cred_msg
