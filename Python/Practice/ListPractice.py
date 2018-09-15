# Looping through list
squares = [1,4,9,16]
sum=0
for num in squares:
  sum+=num
print(sum) ##30

# Test if element appears in list (or other collection)
list=['mary','joe','bob']
if 'mary' in list:
  print('yay')

# Traditional numeric loop
for i in range(10):
  print(i)

# Access every 3rd element in a list
i=0
a=['bob','carry',2,3.6,4,2,'claire']
while i<len(a):
  print(a[i])
  i = i  +3

# Common list commands
list=['larry','curly','moe']
list.append('shemp')  ## Append element at end
list.insert(0,'xxx')  ## Insert element at index 0
list.extend(['yyy','zzz'])  ## Add list of elements at end
print(list) ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly')) ## 2

list.remove('curly')   ## Search and remove that element
list.pop(1)   ## removes and returns 'larry'
print(list)   ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

# List Slices
list =['a',2,3,5,1]
print (list[1:-1]) ##[2,3,5]
list[0:2] ='z'##['a',2]='z'
print(list) ##['z',3,5,1]