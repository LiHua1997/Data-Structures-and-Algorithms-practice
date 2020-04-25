def an_agram_solution(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    j = 0 
    still_ok = True
    while j < 26 and still_ok == True:
        if c1[j] == c2[j]:
            j = j+1
        else:
            still_ok = False
    return still_ok

print(an_agram_solution("abc", "acb"))
print(an_agram_solution("abc", "asb"))


