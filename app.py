from flask import Flask, request, render_template
from twilio.rest import Client
from selenium import webdriver
import geocoder

app = Flask(__name__)
# driver = webdriver.Chrome()
# initialize Twilio client with your account SID and auth token
client = Client("AC29088dc1efc7599a6bf9b5e99bee4089", "8d37cbe600ecd661aa168113df2b75b7")

# define message to be sent
message = "Emergency! Please help! My location is: "

# define emergency contacts
contacts = {"Someone": "+919025740216","Rissi":"+919841570900"}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # name = request.form['name']
        # phone_number = request.form['phone_number']

        # get current location
        g = geocoder.ip('me')
        location = g.latlng

        # add location to message
        message_with_location = message + str(location)

        # send message to emergency contacts
        for name, number in contacts.items():
            client.messages.create(
                to=number, 
                from_="+15855221257", 
                body="Emergency alert from " + name + "! " + message_with_location
            )

        return 'Emergency alert sent to contacts!'

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)