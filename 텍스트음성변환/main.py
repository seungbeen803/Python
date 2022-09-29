from gtts import gTTS # 텍스트를 음성으로 변환(모듈)
# 버전이 안 맞으면 실행이 안될 수도 있다.
from playsound import playsound # mp3 파일 파이썬으로  재생하기 위한 라이브러리(모듈)

# 텍스트를 음성으로 변환
# 파일 경로
file_path = "Mydata.txt"
# 암기 파일 읽어오는 것은 암기
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()
# text = "안녕. 미림."
tts = gTTS(text=read_file, lang='ko')
mp = ("mp3\schoolsong.mp3")
tts.save(mp) # 만들어진 파일을 저장하기 위해 save를 사용한다

# mp3 파일 파이썬으로  재생하기 위한 라이브러리(모듈)
# 재생
playsound(mp)


