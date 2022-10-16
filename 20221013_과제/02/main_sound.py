# 02. 다음과 같은 패키지, 모듈이 있다고 할 때 다음 코드를 바탕으로 빈 칸의 내용을 작성 하시오.
import py_compile
from sound.formats import mp3_read.py
from sound.formats import wav_wirte.py as ww
import sound.effects.echo
mp3_read.play("bgm.mp3")
ww.save("effect.wav")
sound.effects.echo.play()
