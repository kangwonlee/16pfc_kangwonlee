# coding: utf8
# http://learnpythonthehardway.org/book/ex47.html
# 각 행 주석 입력 후 commit

from nose.tools import *

from game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a door to the north.""")

    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
