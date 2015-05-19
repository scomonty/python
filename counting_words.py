

def word_count(str):
  strLower = str.lower()
  strItems = strLower.split()
  d = {}
  for words in strItems:
    if words in d:
      d[words] += 1
    else:
      d[words] = 1    
  print(d)
  
  
word_count('My name is scott')