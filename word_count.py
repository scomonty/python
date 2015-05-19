""""d = {}

def word_count(x):
  word = x.lower()
  word = word.split()
  for names in word:
    d.keys()
	  
  print(names)
  
  
word_count("Hello Im stupid")



shopping_list = ["banana", "orange", "apple"]
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0


for item in prices:
  print (item)
  print ('price: {}\nstock: {}\n'.format(prices[item], stock[item]))
  
  
for item in prices:
  total = total + prices[item] * stock[item]


def compute_bill(food):
  amount = 0
  for item in food:
    if stock[item] > 0:
      amount = amount + prices[item]
      stock[item] = stock[item] - 1
  print (amount)
	
print (total)
compute_bill(shopping_list)

"""

n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print (double_list(n))

def my_function(x):
    for i in range(0, len(x)):
      x[i] = x[i] * 2
    print (x)

my_function(list(range(3)))



n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
    result = ''
    for word in words:
        result = result + word
    print (result)
	

i = 'O' * 5

print(i)


join_strings(n)