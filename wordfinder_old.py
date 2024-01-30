# MAIN

import finder_funcs

def main():
   puzzle = input()
   list_of_rows = finder_funcs.get_rows(puzzle)
   list_of_columns = finder_funcs.get_columns(puzzle)

   print("Puzzle:\n")
   for row in list_of_rows:
      print("".join(row))
   print()

   words = input().split()
   for word in words:
      wrd1 = word
      ro = 0
      w = 0

      for row in list_of_rows:
         row_str = finder_funcs.convert_list(row)  
         column = finder_funcs.search_string(row_str,wrd1)
         if column is False:
            search_backward = finder_funcs.search_string(finder_funcs.flip_string(row_str),wrd1)
            if search_backward is False:
               w += 1
            else:
               print ("{:s}: (BACKWARD) row: {:d} column: {:d}".format(wrd1,ro,9-search_backward))            
         else:
            print ("{:s}: (FORWARD) row: {:d} column: {:d}".format(wrd1,ro,column))
         ro += 1

      while w > 9:
         co = 0
         for col in list_of_columns:
            col_str = finder_funcs.convert_list(col)
            row = finder_funcs.search_string(col_str,wrd1)
            if row is False:
               search_up = finder_funcs.search_string(finder_funcs.flip_string(col_str),wrd1)
               if search_up is False:
                  if co == 9:
                     print("{:s}: word not found".format(wrd1))
                     break
               else:
                  print("{:s}: (UP) row: {:d} column: {:d}".format(wrd1,9-search_up,co))
                  break
            else:
               print("{:s}: (DOWN) row: {:d} column: {:d}".format(wrd1,row,co))               
               break
            co += 1
         w =-1    

if __name__ == '__main__':
   main() 
