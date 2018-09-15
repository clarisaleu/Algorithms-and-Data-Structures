# Find the instructions below.
"""Write a function called "show_excitement" where the string
"I am super excited for this course!" is returned exactly
5 times, where each sentence is separated by a single space.
Return the string with "return".
You can only have the string once in your code.
Don't just copy/paste it 5 times into a single variable!

"""

def show_excitement():
    str = "I am super excited for this course!"
    res = ""
    for x in range(0,4):
        res+=str
        res+=" "
    res+=str
    return res

print (show_excitement())
