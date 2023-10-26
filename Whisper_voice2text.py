import speech_recognition as sr
import time


def get_voice2text(r):
    # r = sr.Recognizer()
    # time.sleep(1)
    with sr.Microphone() as _source:
        # r.dynamic_energy_threshold = True
        # r.energy_threshold = 50
        # r.pause_threshold = 1.4
        print("I am listening, please speak")
        audio = r.listen(_source)

    text_input = ''
    print('语音识别中......')
    try:
        text_input = r.recognize_whisper(audio, language="chinese")
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as _error:
        print("Could not request results from Whisper")
        print(_error)

    return text_input
