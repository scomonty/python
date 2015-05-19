

cities = ['phoenix', 'greensburg', 'irvine', 'orange']
vowels = list('aeiou')
output = []


for names in cities:
  city_list = list(names.lower())

for vowel in vowels:
  while True:
    try:
      city_list.remove(vowel)
    except:
      break
  output.append(''.join(city_list).capitalize())		

print (output)