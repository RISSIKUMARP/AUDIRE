import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a web driver object for Chrome
driver = webdriver.Chrome()

# navigate to the web page with the button
driver.get("https://www.example.com/")

# define a function to click the button
def click_button():
    # find the button element by ID (replace "button-id" with the ID of the button you want to click)
    button = driver.find_element_by_id("button-id")

    # click the button
    button.click()

# create a speech recognizer object
r = sr.Recognizer()

# define a function to listen for voice commands and click the button
def listen_for_command():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)

        # click the button if the command matches
        if "click button" in command.lower():
            click_button()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# call the function to listen for commands
listen_for_command()

# quit the driver
driver.quit()
