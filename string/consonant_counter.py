'''
4. Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U

'''

s=input("Enter student name: ")
count = 0
i=0
while i<len(s):
    ch  = s[i]
    if ch not in "aeiou" and ch not in "AEIOU" and (65<=ord(ch)<=90 or 97<=ord(ch)<=122):
        count += 1
    i+=1
print(f"Total Consonants : {count}")