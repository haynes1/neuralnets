from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

application = Flask(__name__)

@application.route("/", methods=['GET'])
def frontpage():
    return 'For more information visit: the <a href="https://github.com/haynes1/neuralnets">github repo</a>'


@application.route("/receivemms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    application.run(debug=True)