s = input().lower()
vowelCount = 0
for char in range(len(s)):
    if s[char] == "a" or s[char] == "e" or s[char] == "i" or s[char] == "o" or s[char] == "u":
        vowelCount += 1
print(vowelCount)
