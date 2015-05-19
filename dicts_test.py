"""
dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
  new_list = []
  for person in dicts:
      new_list.append(string.format(**person))
  return new_list
  
print(string_factory(dicts, string))
"""


# The dictionary will be something like:
d = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
 'Kenneth Love': ['Python Basics', 'Python Collections'],
 'Dickey Dickums': ['Science', 'Math']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

def most_classes(d):
  max_count = 0
  t = []
  for classes in d:
    if len(d[classes]) > max_count:
      max_count = len(d[classes])
      t = classes
  print(t)

  
most_classes(d)

def num_teachers(d):
  teachers = 0
  for i in d:
     teachers += 1
  print(teachers)
  
num_teachers(d)

def stats(d):
  y = []
  x=0
  for prof in d:
    y.append(prof)
  for numbers in d.values():
    x += 1
    print(x)
    print(y)
	
stats(d)