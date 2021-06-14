


# initialize our dictionary of n=3 ([0,1][0,2][0,3])
# this is an encoded version of the partition information
exponent_dictionary = {
                        1 : 1,
                        2 : 1,  
                        3 : 2,
                        4 : 1,
                        5 : 1,
                        6 : 1
                      }

# Run this function to do the thing
# redundant call from doing google foobar
def solution(n):
        
          return distinct_partition(n)



# Main function
# We skip a few steps by initializing the loop at n=4
def distinct_partition(n):

        global exponent_dictionary

        
        for i in range(4, n + 1):
            expand_factors(i, n)

        return int(exponent_dictionary[n] - 1)
        


def expand_factors(a,n):
  global exponent_dictionary

  # here is where it gets a little spicy
  
  for i in range( len(exponent_dictionary), 0, - 1):
      
      if(i + a > n):
          continue
        
      elif exponent_dictionary.get(i + a) == None:
          exponent_dictionary[i + a] = exponent_dictionary[i]
          
      else:
          exponent_dictionary[i + a] += exponent_dictionary[i] 
      
  if exponent_dictionary.get(a) == None:
    exponent_dictionary[a] = 1
  else:
    exponent_dictionary[a] += 1



