# Functions for wordfinder

# Turn puzzle (string) into a list of rows || **was supposed to be list of strings**
def get_rows(puzzle_string):
   big_list = []
#   for c in puzzle_string:
#      big_list.append(c)
#   list_of_rows = [big_list[x:x+10] for x in range(0, len(big_list), 10)]
   x = 0
   while x < len(puzzle_string):
      big_list.append(puzzle_string[x:x+10])
      x+=10
   return big_list

# Turn puzzle (string) into a list of columns || **was supposed to be list of strings**
def get_columns(puzzle_string):
   big_list = []
   for c in puzzle_string:
      big_list.append(c)
   big_list_of_columns = []
   x = 0
   while x < 10:
      for i in range(x, len(big_list), 10):
         big_list_of_columns.append(big_list[i])
      x += 1
   list_of_columns = [big_list_of_columns[x:x+10] for x in range(0, len(big_list_of_columns), 10)]

   return list_of_columns

# Turn list of characters into a string
def convert_list(lst):
   return "".join(lst)

# Return index if word is in string
def search_string(str, wrd):
   if str.find(wrd) >= 0:
      return str.find(wrd)
   else:
      return False

# Takes a string and reverses it (to search for backward/up words)
def flip_string(str):
   index = len(str)-1
   lst1 = []
   while index >= 0:
      lst1.append(str[index])
      index -= 1
   return "".join(lst1)
