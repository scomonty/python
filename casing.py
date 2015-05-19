def stringcases(x): 
    a = x.upper()
    b = x.lower()
    c = x.title()
    d = x[::-1]
    tup = (a, b, c, d)
    print(tup)
	
stringcases('apple')



my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
count = 0

for letter in my_alphabet_list:
    print('{}: {}'.format(count, letter))
    count += 1
	
	
	
for index, letter in enumerate(my_alphabet_list):
    print('{}: {}'.format(index, letter))
	
	
for step in enumerate(my_alphabet_list):
    print('{}: {}'.format(*step))
	

