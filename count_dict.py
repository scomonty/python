my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']


def members(my_dict, my_list):
  count = 0
  for words in my_list:
    if words in my_dict.keys():
      count += 1
  print(count)

members(my_dict, my_list)
  
