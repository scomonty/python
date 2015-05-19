""""
list = [1, 2, 3]

def add_list():
  for num in list:
    print (num + num)
	
	
add_list()
"""

def match_ends(words):
  # +++your code here+++
  count = 0
  for x in words:
    if len(x) >= 2 and words[0] == words[-1]:
      count += 1
  print (count)
  
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])