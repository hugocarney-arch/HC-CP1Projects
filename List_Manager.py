# Shopping List HC 1st


shopping_list = input("Enter your initial shopping list items separated by commas: ")
shopping_list = shopping_list.split(",")
shopping_list = [item.strip() for item in shopping_list]
print(f"Initial shopping list:")
print(*shopping_list)


def add_item(item):
           shopping_list.append(item)
           print(f"Added item: {item}")


def remove_item(item):
           if item in shopping_list:
               shopping_list.remove(item)
               print(f"Removed item: {item}")
           else:
               print(f"Item not found in the list: {item}")


def view_list():
           if shopping_list:
               print("Current shopping list:")
               for item in shopping_list:
                   print(f"- {item}")
           else:
               print("Shopping list is empty.")


while True:


       print("Do you want to add, remove, view, or exit shopping list items in your shopping list?")
       action = input("Enter your choice (add/remove/view/exit: ")
       if action == "add":
           item = input("Enter the item to add no spaces at beginning: ")
           add_item(item)
       elif action == "remove":
           item = input("Enter the item to remove no spaces at beginning: ")
           remove_item(item)
       elif action == "view":
           view_list()
       elif action == "exit":
           break
       else:
           print("Invalid action please enter: add, remove, view, or exit")
