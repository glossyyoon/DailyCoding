vowel = "aeiou"
while True:
    s = input()
    if s == "end":
        break
    v_repeat = 0
    m_repeat = 0
    v_count = 0
    temp = ""
    flag = True
    for i in range(len(s)):
        if s[i] in vowel:
            m_repeat = 0
            v_count += 1
            v_repeat += 1
            if v_repeat >= 3:
                print("<" + s + ">" + " is not acceptable.")
                flag = False
                break
        if s[i] not in vowel:
            m_repeat += 1
            v_repeat = 0
            if m_repeat >= 3:
                print("<" + s + ">" + " is not acceptable.")
                flag = False
                break
        if s[i] == temp:
            if s[i] == "e" or s[i] == "o":
                pass
            else:
                print("<" + s + ">" + " is not acceptable.")
                flag = False
                break
        temp = s[i]
    if v_count == 0 and flag == True:
        print("<" + s + ">" + " is not acceptable.")
        continue
    elif flag == True:
        print("<" + s + ">" + " is acceptable.")
