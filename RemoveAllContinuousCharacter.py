def removeDuplicates(s , k):
    st = []
    numst = []
#     process characters
    for c in s:
        if st and st[-1] == c:
            #check frequencey
            freq = numst.pop()
            freq+=1
            if freq == k:
                st.pop()
            else:
                numst.append(freq)
        else:
            st.append(c)
            numst.append(1)
    res = []
    while st:
        c = st.pop()
        cnt = numst.pop()
        for i in range(cnt):
            res.append(c)
    return "".join(res[::-1])
    
s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s,k))
    