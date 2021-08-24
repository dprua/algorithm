class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s1 = "".join(c for c in s if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >=65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122))
        s1 = "".join(c for c in s if c.isalnum())
        s1 = s1.lower()
        return s1 == s1[::-1]
