def palindrome(s):
    if not s:
        return ""
    def is_palindrome(string):
        return string == string[::-1]
    i = len(s)
    while i > 0 and not is_palindrome(s[:i]):
        i -= 1
    return s[i:][::-1] + s
s1 = "aacecaaa"
s2 = "abcd"
result1 = palindrome(s1)
result2 = palindrome(s2)
print(f"Input: {s1}\nOutput: {result1}")
print(f"Input: {s2}\nOutput: {result2}")
