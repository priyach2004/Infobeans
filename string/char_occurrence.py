'''
3. Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
'''

s=input("Enter product review: ")
ch=input("Enter character to check: ")
count = 0
i=0
while i<len(s):
    if s[i]==ch:
        count += 1
    i+=1
print(f"Character '{ch}' occurs: {count} times")