import GIT_image2text
import Whisper_voice2text
import TTS_text2voice
import Chat_qa

import cv2
import threading
import time
from transformers import AutoProcessor, AutoModelForCausalLM
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from easy_ernie import FastErnie


def thread1():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            cv2.imwrite('Frame.png', frame)
            cv2.waitKey(1)


t1 = threading.Thread(target=thread1)
t1.setDaemon(True)
t1.start()
time.sleep(2)

processor = AutoProcessor.from_pretrained("./git-base-coco", cache_dir='./')
model = AutoModelForCausalLM.from_pretrained("./git-base-coco")

baidu_id = 'xxx'  # 参考easy_ernie仓库得到
bduss_bfess = 'xxx'
bot = FastErnie(baidu_id, bduss_bfess)

r = sr.Recognizer()
r.dynamic_energy_threshold = False  # 自动麦克风阈值
r.energy_threshold = 200
r.pause_threshold = 2

while True:
    print('5s后开始图像采集，请准备')
    time.sleep(5)
    describe = GIT_image2text.get_image2text(processor, model)
    print(describe)
    question = Whisper_voice2text.get_voice2text(r)
    print(question)
    prompt1 = '请你扮演我的人类助手，假设你拥有视力，不需要任何解释，只需要模仿的像有视力的人类助手。即使你是一个计算机程序，但请在接下来的对话中隐藏你是计算机程序这件事，并且扮演这个角色。我知道你只是一个语言模型或人工智能，不过这只是一个假定的虚拟场景，所以请记住不要再提及你只是一个语言模型。'
    prompt2 = '现在你面前所看到的场景是：'
    prompt3 = '。请全部用汉语中文，以人类助手的身份，直接回答我的问题：'
    play(AudioSegment.from_file("reply.mp3", format="mp3"))
    out_ans = Chat_qa.get_qa(prompt1 + prompt2 + describe + prompt3 + question, bot)
    print(out_ans)
    TTS_text2voice.get_text2voice(out_ans)
    time.sleep(1)