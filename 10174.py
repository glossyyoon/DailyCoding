num = int(input())
palindrome = []
for i in range(num):
    palindrome.append(str(input()).lower())
for j in range(len(palindrome)):
    word = palindrome[j]
    length = len(palindrome[j])//2
    if len(palindrome[j])%2==0:
        for k in range(length):
            result = "Yes"
            if word[k] != word[len(word)-1-k]:
                result = "No"
                break
        print(result)
    else:
        length = (len(palindrome[j])-1)
        for k in range(length):
            result = "Yes"
            if word[k] != word[len(word)-1-k]:
                result = "No"
                break
        print(result)