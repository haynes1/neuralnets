from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

application = Flask(__name__)

@application.route("/", methods=['GET'])
def frontpage():
	return 'For more information visit: the <a href="https://github.com/haynes1/neuralnets">github repo</a>'


@application.route("/receivemms", methods=['GET', 'POST'])
def sms_ahoy_reply():
	
	if request.values['NumMedia'] != '0':

		# Use the message SID as a filename.
		filename = request.values['MessageSid']   '.png'
		with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
		   image_url = request.values['MediaUrl0']
		   f.write(requests.get(image_url).content)

		resp.message("Thanks for the image!")
	else:
		resp.message("Try sending a picture message.")
	

	# Start our response
	resp = MessagingResponse()

	# Add a message
	resp.message("Ahoy! Thanks so much for your message.")

	return str(resp)

if __name__ == "__main__":
	application.run(debug=True)