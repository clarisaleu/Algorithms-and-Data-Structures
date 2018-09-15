# Find the instructions below.
"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []

    # My code.
    def addItem(self,item):
        self.items.append(item)

    # My code.
    def getClassiness(self):
        fanciness=0
        if len(self.items)<1:
            return 0
        for x in range(0,len(self.items)):
            if self.items[x]=="tophat":
                fanciness+=2
            elif self.items[x]=="bowtie":
                fanciness+=4
            elif self.items[x]=="monocle":
                fanciness+=5
            else:
                fanciness+=0
        return fanciness

# Test cases
me = Classy()

# Should be 0
print (me.getClassiness())

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())
