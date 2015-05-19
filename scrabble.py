score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        if letter in score.keys():
            total += score[letter]
    print(total)
	
	
scrabble_score('key')



def censor(text, word):
    if word in text:
        ast = len(word)
    for letter in word:
        letter = '*'
    print(text, letter)
	

	
censor('poop peep poop', 'peep')


def purify(lists):
    a = []
    for x in lists:
        if x % 2 == 0:
            a.append(x)
    print (a)
	
purify([5,4,5,4,6,9,23])	


def product(x):
    total = 1
    for i in x:
        total *= i
    print(total)
	
product([4,5,5])


def remove_duplicates(x):
    a = []
    for i in x:
	    if i not in a:
             a.append(i)
    print(a)
	
remove_duplicates([4,5,5,4])



grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total=0
    for x in scores:
        total += x
    return total
    
print (grades_sum(grades))

def grades_average(grades):
    total = 0
    number = float(len(grades))
    for x in grades:
        total += x
    average = total / number
    print(average)
	
grades_average(grades)

  

