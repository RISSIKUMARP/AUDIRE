from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3

from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Dharshini I\\Downloads\\chromedriver_win32")
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
    if 'open google' in voice:
        speak('Opening google..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://google.com')
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