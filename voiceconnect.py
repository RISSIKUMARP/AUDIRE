from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3
from selenium.webdriver.chrome.service import Service
from twilio.rest import Client
from flask import Flask, request, render_template
import geocoder

service = Service("C:\\Users\\Dharshini I\\Documents\\github\\IATRO\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response

time.sleep(3)
speak("Hello master! I am now online..")

while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)

    if 'save a new contact' in voice:
        # Initialize dictionary
        contact_info = {}

        # Function to get contact information
        def get_contact_info(field_name):
            with sr.Microphone() as source:
                print("Please say your " + field_name + ":")
                engine.say("Please say your " + field_name + ":")
                engine.runAndWait()
                audio = recognizer.listen(source)

            try:
                field = recognizer.recognize_google(audio)
                print("Your " + field_name + " is: " + field)
                contact_info[field_name] = field
            except:
                print("Sorry, could not recognize your " + field_name + ".")
                engine.say("Sorry, could not recognize your " + field_name + ".")
                engine.runAndWait()

        # Get name and phone number
        get_contact_info('name')
        get_contact_info('phone')

        # Print contact info
        print(contact_info)
        engine.say("Your contact information has been successfully stored.")
        engine.runAndWait()


    elif 'emergency' in voice:
        # Set up your Twilio account SID and auth token
        account_sid = 'ACa3c39edcfcba2a1cf0a82ef770ae556a'
        auth_token = '8a29a17a6f48e4acd263a4b184d2f64f'

        # Initialize the Twilio client
        client = Client(account_sid, auth_token)

        # initialize Twilio client with your account SID and auth token
        client = Client("ACa3c39edcfcba2a1cf0a82ef770ae556a", "8a29a17a6f48e4acd263a4b184d2f64f")

        # define the emergency number to call
        emergency_number = "+919841570900"  # Change this to the appropriate emergency number in your country.

        # make the call
        call = client.calls.create(
            to=emergency_number,
            from_="+15074686035",
            url="http://demo.twilio.com/docs/voice.xml" # This is a TwiML URL that plays a message when the call is answered. You can replace it with your own TwiML URL.
        )

        # print the call SID
        print(call.sid)   

        app = Flask(_name_)
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

        if _name_ == '_main_':
            app.run(debug=True)

    elif 'search google' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)

    elif 'mail option' in voice:
        def send_otp(to_email):
            # Generate a random OTP
            otp = str(random.randint(1000,9999))

            # Sender's email and password
            gmail_user = "201501041@rajalakshmi.edu.in"
            gmail_password = "kavirissi@747587"

            # Email subject and body
            subject = 'OTP for your  account'
            body = 'Your OTP for verification is: ' + otp

            # Prepare the email
            email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (gmail_user, to_email, subject, body)

            try:
                # Send the email
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(gmail_user, to_email, email_text)
                server.close()

                print('Email sent!')
            except Exception as e:
                print(e)
                print('Something went wrong...')

        # Example usage
        send_otp('201501010@rajalakshmi.edu.in')   

    elif 'open youtube' in voice:
        speak('Opening youtube..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(window_list[-1])
        driver.get('https://youtube.com')
    elif 'search youtube' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('search_query')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'switch tab' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver.switch_to_window(driver.window_handles[cur_tab])
    elif 'close tab' in voice:
        speak('Closing Tab..')
        driver.close()
    elif 'go back' in voice:
        driver.back()
    elif 'go forward' in voice:
        driver.forward()
    elif 'exit' in voice:
        speak('Goodbye Master!')
        driver.quit()
        break
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(2)