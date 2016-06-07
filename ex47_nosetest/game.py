# coding: utf8
# http://learnpythonthehardway.org/book/ex47.html
# 각 행 주석 입력 후 commit


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, directions):
        return self.paths.get(directions, None)

    def add_paths(self, paths):
        self.paths.update(paths)

# end class Room

# 각자 Study drills 시도 후 필요시 commit

# 오류 노트에 각자 작성
