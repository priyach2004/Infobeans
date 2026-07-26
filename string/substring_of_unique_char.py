'''
5. Social Media Hashtag Trend Window

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

s=input("Input: ")
r=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        r.append(s[i:j])
res=""  
for i in s:
    if i not in res:
        res=res+i

for i in r:
    if sorted(res)==sorted(i):
        print(i)
        break