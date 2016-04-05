# -*-coding:utf-8
# http://learnpythonthehardway.org/book/ex11.html

print "How old are you?",
# Python 3
# print("How old are you?", end= ' ')
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print("So you're %r old, %r tall and %r heavy." % (
    age, height, weight))
