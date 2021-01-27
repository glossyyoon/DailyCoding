def palindrome():
    num = int(input())
    for i in range(num, 1000001):
        if num==2 or num==1 or num==3 or num==5 or num==7:
            return num

        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
            for j in range(len(str(i))):
                number = str(i)
                length = len(number)//2
                if len(number)%2!=0:
                    length = (len(number)-1)
                for k in range(length):
                    if number[k] != number[len(number)-1-k]:
                        break
                    elif k==length-1 and number[k] == number[len(number)-1-k]:
                        return number
            
print(palindrome())