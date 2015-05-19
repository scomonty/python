shopping_list = []

def show_help():
  print("What should we pick up at the store? \n\nEnter: \nDONE to stop adding items. \nHELP to show the help menu. \nSHOW to show your current list. \nREMOVE to remove an item from your list")

def add_to_list(item):
  shopping_list.append(item)
  if len(shopping_list) == 1:
    print("Added! There is now {} item in your shopping list.".format(len(shopping_list)))
  else:
    print("Added! There are now {} items in your shopping list.".format(len(shopping_list)))

def show_list():
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1
	
def remove_item(item):
  print("enter the item you would like to remove.")
  show_list()
  lose_item = input("> ")
  shopping_list.remove(lose_item) 
  if len(shopping_list) == 1:
    print("{} has been removed, there is now {} item in your shopping list.".format(lose_item, len(shopping_list)))
  else:
    print("{} has been removed, there are now {} items in your shopping list.".format(lose_item, len(shopping_list)))
	
	
	
show_help()

while True:
  new_item = input("> ")
  if new_item.upper() == 'DONE':
    break
  elif new_item.upper() == 'HELP':
    show_help()
    continue
  elif new_item.upper() == 'SHOW':
    print("here's your list:")
    show_list()
    continue
  elif new_item.upper() =='REMOVE':
    remove_item(new_item)
    continue
  else:
    add_to_list(new_item)
    continue
	
	
show_list()


