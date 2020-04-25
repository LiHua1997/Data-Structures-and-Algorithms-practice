def an_agram_solution(s1, s2):
    alist = list(s1)
    blist = list(s2)
    alist.sort()
    blist.sort()
    pos = 0 
    match = True
    while pos < len(alist) and match:
        if alist[pos] == blist[pos]:
            pos += 1
        else:
            match = False
    return match

print(an_agram_solution("abc","cba"))
print(an_agram_solution("abd","ASd"))
