# coding: utf8
# 참고문헌: http://learnpythonthehardway.org/book/ex47.html
# 각 행 주석 입력 후 commit

from nose.tools import *

from game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
door to the north.""")

    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

# 각자 Study drills 시도 후 필요시 commit

# 열린게시판 / 오류노트 에 각자 오류노트 작성
