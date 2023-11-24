#1.
"""def m_num(num) :
    n = len(num)
    e_sum = ((n*(n+1))//2)
    a_sum = sum(num)
    return e_sum - a_sum 
ls = [1, 0, 3, 5, 4]
missing_num = m_num(ls)
print("Missing number is :", missing_num)"""

#2. 
"""def r_a(a) :
    rev = a[::-1]
    return rev
array = [1,2,3,4,5]
rev_array = r_a(array)
print("Reversed array is :", rev_array)"""

#3.
"""def char_count(st):
    ch = {}
    for char in st :
        if char in ch :
            ch[char] += 1
        else:
            ch[char] = 1
    return ch
str = "google.com"
char_freq = char_count(str)
print(char_freq)"""

#4.
"""import re
def is_palin(st) :
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', st).lower()
    return cleaned_string == cleaned_string[::-1]

input_string = "A man, a plan, a canal, Panama"
if is_palin(input_string):
    print(f"'{input_string}' is a palindrome")
else:
    print(f"'{input_string}' is not a palindrome")"""

#5. 
"""def is_anagram(str1, str2) :
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
st1 = "listen"
st2 = "silent"
if is_anagram(st1, st2):
    print("Anagram")
else:
    print("Not Anagram")"""