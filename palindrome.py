def isPalindrome(s):
    rev = ''.join(reversed(s))
    return s == rev
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
