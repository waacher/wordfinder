from math import sqrt

'''
# Hardcoded for testing purposes
puzzle = """ qwert
             asdfg
             zxcvb
             yuiop
             ghjkl"""
''' 

# turn input puzzle (all one line) into list of rows
# (string, int) -> list
def get_rows(pzl, sidelen):
    return [pzl[x:x+sidelen] for x in range(0, sidelen*sidelen, sidelen)]

# For all grab functions, assume start is within puzzle 
#   - main loops through each index 
#   - return None if out of bounds

# one row as string, index (in row) to start and length to grab -> string
def grab_left(row, start, length):
    if length == 1:
        return row[start]
    # check row is big enough
    stop = start - length
    if stop < -1:
        return None
    elif stop == -1: # string slice shenanigans
        stop = None
    return row[start : stop: -1]

def grab_right(row, start, length):
    if start + length > len(row): # check row is long enough
        return None
    return row[start: start+length]
    
# puzzle as list of rows, sidelength, start (in puzzle), length to grab -> string
def grab_up(pzl, sidelen, start, length):
    # check enough columns above
    if (start // sidelen) - length < -1:
        return None
    result = ""
    while length > 0:
        result += pzl[start // sidelen][start % sidelen]
        start -= sidelen
        length -= 1
    return result
    
def grab_down(pzl, sidelen, start, length):
    # check enough columns below
    if (start // sidelen) + length > sidelen:
        return None
    result = ""
    while length > 0:
        result += pzl[start // sidelen][start % sidelen]
        start += sidelen
        length -= 1
    return result

# diagonals 

def grab_up_left(pzl, sidelen, start, length):
    # not enough rows above OR not enough columns to left
    if (start // sidelen) - length < -1 or (start % sidelen) - length < -1:
        return None

    result = ""
    while length > 0:
        result += pzl[start // sidelen][start % sidelen]
        start -= (sidelen + 1)
        length -= 1
    return result
    
def grab_up_right(pzl, sidelen, start, length):
    # not enough rows above OR not enough columns to right
    if (start // sidelen) - length < -1 or (start % sidelen) + length > sidelen:
        return None
    
    result = ""
    while length > 0:
        result += pzl[start // sidelen][start % sidelen]
        start -= (sidelen - 1)
        length -= 1
    return result

def grab_down_left(pzl, sidelen, start, length):
    # not enough rows below OR not enough columns to left
    if (start // sidelen) + length > sidelen or (start % sidelen) - length < -1:
        return None
        
    result = ""
    while length > 0:
        result += pzl[start // sidelen][start % sidelen]
        start += (sidelen - 1)
        length -= 1
    return result
    
def grab_down_right(pzl, sidelen, start, length):
    # not enough rows below OR not enough columns to right
    if (start // sidelen) + length > sidelen or (start % sidelen) + length > sidelen:
        return None
        
    result = ""
    while length > 0:
        result += pzl[start // sidelen][start % sidelen]
        start += (sidelen + 1)
        length -= 1
    return result

def main():
    puzzle = input("Enter puzzle as non-space characters on one line (left to right by row):\n")
    pzl = ''.join([line.strip() for line in puzzle])

    pzl_sidelen = sqrt(len(pzl))
    if not pzl_sidelen.is_integer():
        print("Puzzle is not a square \n")
        return
        
    sidelen = int(pzl_sidelen)    
    rows = get_rows(pzl, sidelen)

    print("\nPuzzle:\n")
    for row in rows:
        print(" ".join(row))
    print()
  
    words = input("Enter words to search for, separated by a space: \n").split()

    for wrd in words:
        length = len(wrd)
        if length > sidelen:
            print("'{}' is too long".format(wrd))
            continue

        found = ""
        
        for i in range(sidelen * sidelen):
            ro, col  = i // sidelen, i % sidelen
            row_str = rows[ro]
            if row_str[col] == wrd[0]:
                if len(wrd) == 1:
                    found = "1st instance"
                    break
                
                if wrd[1] == grab_left(rows[ro], col-1, 1):
                    if length == 2 or grab_left(row_str, col-2, length-2) == wrd[2:]:
                        found = "LEFT"
                        break
                    
                elif wrd[1] == grab_right(rows[ro], col+1, 1):
                    if length == 2 or grab_right(row_str, col+2, length-2) == wrd[2:]:
                        found = "RIGHT"
                        break
                        
                elif wrd[1] == grab_up(rows, sidelen, i-sidelen, 1):
                    if length == 2 or grab_up(rows, sidelen, i-(sidelen*2), length-2) == wrd[2:]:
                        found = "UP"
                        break
                        
                elif wrd[1] == grab_down(rows, sidelen, i+sidelen, 1):
                    if length == 2 or grab_down(rows, sidelen, i+(sidelen*2), length-2) == wrd[2:]:
                        found = "DOWN"
                        break     

                # check diagonals

                elif wrd[1] == grab_up_left(rows, sidelen, i-sidelen-1, 1):
                    if (length == 2 or 
                        grab_up_left(rows, sidelen, i-(sidelen*2)-2, length-2) == wrd[2:]):
                            found = "DIAGONAL (up+left)"
                            break
                            
                elif wrd[1] == grab_up_right(rows, sidelen, i-sidelen+1, 1):
                    if (length == 2 or 
                        grab_up_right(rows, sidelen, i-(sidelen*2)+2, length-2) == wrd[2:]):
                            found = "DIAGONAL (up+right)"
                            break
                            
                elif wrd[1] == grab_down_left(rows, sidelen, i+sidelen-1, 1):
                    if (length == 2 or 
                        grab_down_left(rows, sidelen, i+(sidelen*2)-2, length-2) == wrd[2:]):
                            found = "DIAGONAL (down+left)"
                            break
                            
                elif wrd[1] == grab_down_right(rows, sidelen, i+sidelen+1, 1):
                    if (length == 2 or 
                        grab_down_right(rows, sidelen, i+(sidelen*2)+2, length-2) == wrd[2:]):
                            found = "DIAGONAL (down+right)"
                            break
                else:
                    continue
                    
        if found:
            print("'{}' : {} @ row {} col {}".format(wrd, found, ro+1, col+1)) 
        else:
            print("'{}' not found".format(wrd))
               
               
if __name__ == '__main__':
    main()