import requests
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import PIL as pillow
from PIL import Image
import io
import numpy as np
import network2

application = Flask(__name__)

#converts from 0 - 255 to 1 - 0
def convertImage(x):
	return abs((x - 255) / -255)


@application.route("/", methods=['GET'])
def frontpage():
	return 'For more information visit teeeest: the <a href="https://github.com/haynes1/neuralnets">github repo</a>'


@application.route("/receivemms", methods=['GET', 'POST'])
def sms_ahoy_reply():

	# Start our response
	resp = MessagingResponse()
	
	if request.values['NumMedia'] != '0':

		# Use the message SID as a filename.
		filename = request.values['MessageSid'] + '.png'
		image_url = request.values['MediaUrl0']

		image_file = io.BytesIO(requests.get(image_url).content)
		im = Image.open(image_file)


		#crop image to square
		width, height = im.size   # Get dimensions
		min_dimension = min(width, height)
		left = (width - min_dimension) / 2
		top = (height - min_dimension) / 2
		right = (width + min_dimension) / 2
		bottom = (height + min_dimension) / 2
		im.crop((left, top, right, bottom))

		#make image grayscale
		im = im.convert('L')

		#make 28/28
		im = im.resize((28,28), Image.ANTIALIAS)

		#up the contrast
		level = 140
		factor = (259 * (level + 255)) / (255 * (259 - level))
		def contrast(c):
			return 128 + factor * (c - 128)
		im = im.point(contrast)

		im  = im.transpose(Image.ROTATE_90)

		data = np.asarray(im, dtype="float")

		flattened = convertImage(np.reshape(data, (np.product(data.shape),1)))
		print flattened, flattened.shape

		#load network
		net = network2.load("savednet.txt")
		result = net.feedforward(flattened)

		resp.message("RESULT: " + str(result))
	else:
		resp.message("Try sending a picture message.")


	return str(resp)

if __name__ == "__main__":
	application.run(debug=True)