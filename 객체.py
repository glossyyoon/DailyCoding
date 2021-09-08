#is는 객체의 id가 같은지 다른지를 리턴함.
#객체 = 파이썬에서 데이터를 추상화 한 것.
#파이썬의 모든 데이터는 객체 또는 객체 간의 관계로 표현한다다. 파이썬을 객체지향언어라고 부르는 이유도 여기 있다.
#모든 객체는 identity, type, value를 갖는다.
#id = 메모리 상의 주소

a = 1  #불변객체는 id가 항상 같다(값이 같을 때)
b = a

c = 1.0
d = 1
print(id(a))
print(id(b))
print(id(c))
print(id(d))

print(a == b)  #같음
print(a is b)  #같음
print(a == c)  #같음
print(a is c)  #다름

i = [1, 2, 3]  #가변객체는 id가 다르다.
k = [1, 2, 3]
i is k
print(id(i))
print(id(j))
print(id(k))

print(i == k)  #같음
print(i is k)  #다름

t = (1, 2, 3)
y = (1, 2, 3)
print(t is y)  #튜플이므로 불변

i = 2
j = 3
