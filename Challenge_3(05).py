def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        for a,b in [(i,i),(i,i+1)]:
            left,right = a,b
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1 > len(res):
                    res = s[left:right+1]
                left-=1
                right+=1
    return res
# Test cases
print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("racecar"))