date = input()  #int는 직접 자르기가 안된다. string으로 잘라주자.
print(date[:2] + "년", date[2:4] + "월", date[4:] + "일")
print(date[:])