# coding: utf8
# 참고문헌: http://learnpythonthehardway.org/book/ex41.html
#   https://wikidocs.net/27
# 각 행 주석 입력 후 commit

import random
import sys
from urllib import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "클래스 %%% 를 만든다. 부모클래스 %%% 로부터 상속받는다.",
    '''class %%%(object):
\tdef __init__(self,***)''':
        "클래스 %%% 는 __init__ 함수가 있고 그 매개변수는 self와 *** 이다.",
    "*** = %%%()":
        "*** 을(를) 클래스 %%% 의 인스턴스로 만든다.",
    "***.***(@@@)":
        "객체 ***로 부터 함수 *** 를 찾아 호출한다. 매개변수는 self 와 @@@이다.",
    "***.*** = '***'":
        "객체 ***로 부터 속성 *** 을 찾아 그 값을 '***' 으로 바꾼다",
}

PHRASE_FIRST = False
if (len(sys.argv) == 2) and (sys.argv[1] == "한글"):
    PHRASE_FIRST = True

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())



# 각자 Study drills 시도 후 필요시 commit

# 열린게시판 / 오류노트 에 각자 오류노트 작성
