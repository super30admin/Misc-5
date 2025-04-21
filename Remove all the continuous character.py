#space: O(n)
#time:O(n)
#using stack to track count of characters
def remove_continuous_chars(s):
    stack=[]
    n = len(s)
    char=''
    cnt=0
    for i in range(n):      
        if stack:
            curr=stack.pop()
            char=curr[0]
            cnt=curr[1]
        if char==s[i]:
            if cnt+1==3:
                continue
            else:
                cnt+=1
            stack.append([char,cnt])
        else:
            stack.append([char,cnt])
            stack.append([s[i],1])
    result=''
    while stack:
        char,cnt=stack.pop()
        strng=''
        for i in range(cnt):
            strng= char+strng        
        result= strng+result    
    return result

# Test cases
print(remove_continuous_chars("abba"))        # abba
print(remove_continuous_chars("abbb"))        # a
print(remove_continuous_chars("abbbaa"))      # ''
print(remove_continuous_chars("abbacccaa"))   # abb
