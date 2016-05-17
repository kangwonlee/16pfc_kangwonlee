# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/book/ex32.html

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# 여기까지 입력 후 add, commitS

# 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit

# 오류노트 에 각자 오류노트 작성
