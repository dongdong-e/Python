# Regular Expressions(정규표현식)

import re
p = re.compile('[a-z]+')
m = p.match("youngdong")

if m:
    print('Match found:', m.group())
else:
    print('Not Match')

#####

Match와 Search의 차이점 => Match는 순서대로 검색 Search는 전체를 검색

m = p.search("python")
print(m)

n = p.search("3 python")
print(n)

#####

findall 메서드는 p = re.compile('[a-z]+') 정규식과 매치되어 리스트로 리턴

result = p.findall("life is too short")
print(result)

#####

finditer 메서드는 findall과 동일하지만 그 결과로 반복 가능한 객체를 리턴한다.

result = p.finditer("life is too short")
print(result)

for r in result: print(r)

##### match 객체의 메서드

import re
p = re.compile('[a-z]+') => re.compile('\D+')
m = p.match("python")

m.group() -> 매치된 문자열을 리턴
m.start() -> 매치된 문자열의 시작 위치를 리턴
m.end() -> 매치된 문자열의 끝 위치를 리턴
m.span() -> 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴
