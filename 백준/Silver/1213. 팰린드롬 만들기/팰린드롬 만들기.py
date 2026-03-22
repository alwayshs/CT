name = input()

counts = [0] * 26
for char in name:
    counts[ord(char) - ord('A')] += 1

half_palindrome = ""
odd_char = ""
odd_count = 0

for i in range(26):
    char = chr(i + ord('A'))
    count = counts[i]
    
    if count % 2 == 1:
        odd_count += 1
        odd_char = char
        
    half_palindrome += char * (count // 2)

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(half_palindrome + odd_char + half_palindrome[::-1])