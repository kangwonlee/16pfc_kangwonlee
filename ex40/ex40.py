# -*-coding: utf8
# http://learnpythonthehardway.org/book/ex40.html
# 각 행 주석 입력

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

import mystuff_module

mystuff_module.apple()
print(mystuff_module.tangerine)


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
# end class MyStuff


thing = MyStuff()
thing.apple()
print(thing.tangerine)
