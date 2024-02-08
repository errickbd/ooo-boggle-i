import random
import string
from textwrap import wrap

class BoggleBoard:
  dice_list = ['AAEEGN','ELRTTY','AOOTTW','ABBJOO','EHRTVW','CIMOTU','DISTTY','EIOSST','DELRVY','ACHOPS','HIMNQU','EEINSU','EEGHNW','AFFKPS','HLNNRZ','DEILRX']

  def __init__(self, main_list="12345678abcdefgh"):
    self.main_list = main_list

  
  def shake(self):
    temp_list = []
    # num_rand = random.randint(0,5)
    for list in self.dice_list:
      temp_list.append(list[random.randint(0,5)])
      # for letter in list:
      #   print(letter)
       # temp_list.append(letter[num_rand])
    new_string = ''.join(temp_list) 
    result_string = new_string.replace(',', '')
    self.show_handle(result_string)

    return result_string

  def show_handle(self, string):
    arr = wrap(string, 4)
    for line in arr:
      print(line)


boggleboard=BoggleBoard()
boggleboard.shake()

  # def shake(self):
  #   new_string =''
  #   for i in range(len(self.main_list)):  
  #      #loops through each 4 lists
  #     # for j in range(len(self.main_list[i])):       #loops through each character in list
  #     new_char = self.main_list[i].replace(self.main_list[i] ,random.choice(string.ascii_uppercase))
  #     new_string += new_char
  #   self.show_handle(new_string)
  #   return new_string
  
  

  
#   def __str__(self):
#     return f"{self.main_list}"

# boggleboard = BoggleBoard()
# # print(boggleboard)
# print('----\n----\n----\n----')
# print(wrap(boggleboard.main_list, 4))
# boggleboard.shake()
