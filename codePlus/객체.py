#is는 객체의 id가 같은지 다른지를 리턴함.
#객체 = 파이썬에서 데이터를 추상화 한 것.
#파이썬의 모든 데이터는 객체 또는 객체 간의 관계로 표현한다다. 파이썬을 객체지향언어라고 부르는 이유도 여기 있다.
#모든 객체는 identity, type, value를 갖는다.
#id = 메모리 상의 주소

a = "a"  #불변객체는 id가 항상 같다
b = a
c = "a"
print(id(a))
print(id(c))
print(type(a))

i = [1, 2, 3]  #가변객체는 id가 다르다.
j = i
k = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)