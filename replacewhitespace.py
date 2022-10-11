import re
def whitespace():
    str1="nabeel ak_gmail"
    d={" ":"_","_":" "}
    print(re.sub(r'[ _]',lambda m:d[m[0]],str1))
whitespace()