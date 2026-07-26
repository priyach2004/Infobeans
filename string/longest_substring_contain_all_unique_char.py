'''
# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca


### Explanation:

dbca contains all unique characters: a,b,c,d
'''

s=input("Input: ")	#aabcbcdbca
chars=""
for i in s:
    if i not in chars:
        chars+=i
min_len=len(s)+1
result=""
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp+=s[j]
        if len(temp)==len(chars):
            if min_len>j-i+1:
                min_len=j-i+1
                result=s[i:j+1]
            break
print(f"Output: {result}")