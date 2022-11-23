import re
string ='hello 33 hi 45'
pattern ='\d+'

result =re.findall(pattern, string)
print(result)

result =re.split(pattern, string)
print(result)

string='abc 98\
   de 76 \n f54 3'
pattern='\s+'

replace=''
# here 4 is parameter used as count
new_string= re.sub(pattern, replace, string,4)
print(new_string)
# it returns a tuple of 2 items containing the new string and the number of substitutions made.
new_string= re.subn(pattern, replace, string)
print(new_string)

string ="I am learning Python"

match=re.search('\AI',string)

if match:
    print(match.group())
    print("Pattern found inside the string")
else:
    print("Pattern not found")

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)