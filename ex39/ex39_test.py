# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex39.html
# http://eclass.kpu.ac.kr/ilos/pf/course/lecture_material_view_form.acl?ARTL_NUM=373490&SCH_KEY=&SCH_VALUE=&display=10&start=1
#  각 행 주석 입력
import hashmap

# create a mapping of states to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Hawaii', 'HI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'Los Angeles')
hashmap.set(cities, 'HI', 'Honolulu')
hashmap.set(cities, 'OR', 'Orlando')

# added some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# 여기까지 입력 후 add, commit

# 각자 Study drills 시도 후 필요시 commit

#  오류노트 에 각자 오류노트 작성
