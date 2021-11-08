"""
DISTINCT PARTITIONS: This is basically the answer to the question of "how many ways
are there to represent an integer as a sum of unique integers?"

For example if we want to find the answer for 6, we have

            6
            5 + 1
            4 + 2
            ------
  (illegal example: 3 + 3)


We have two possible combinations, so the answer of q(6) is 3.


    There is a generating function for calculating q(n), a modified version of
the Euler function. It's equal to the repeated product of (1 + x^k)

In action, it looks like this:
    q(4) = (1+x^1)(1+x^2)(1+x^3)(1+x^4)

    Once you perform the full expansion, the answer is encoded in the [coefficient]
of the summand with your desired degree (in the case of q(4), we look for ax^4,
where a is our final value).

    The final summation will be full of redundant information:
        x^10 + x^9 + x^8 + 2x^7 + 2x^6 + 2x^5 + 2x^4 + 2x^3 + x^2 + x + 1

Doing this on a computer is extremely inefficient due to its recursive nature.
We only really need 2 pieces of information: the exponent, and the coefficient.
Therefor, we can cut out a lot of the unnecessary work with a few shortcuts.


For example, instead of fully representing (1 + x^k), we can make a tuple, [0,k].
We use 0 because in this context its better to look at 1 as x^0

"""

# Encoded partition info showing only exponent/coeffients for current expanded sum!
# initialize our dictionary of n=3 using the tuples concept ([0,1][0,2][0,3])
# in full form it would look like x + x^2 + 2x^3 + x^4 + x^5 + x^6
# [exponent, coefficient]
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



# Main function that handles the overarching process
# We skip a few steps by initializing the loop at n=4
def distinct_partition(n):

        global exponent_dictionary

        # starting at 4 because exponent map is initialized at 3
        # needs to run up to and including n
        for i in range(4, n + 1):
            expand_factors(i, n)

        return int(exponent_dictionary[n] - 1)


  """
  here is where it gets a little spicy
  The short answer here is that we are trying to keep the dictionary as lean as
  possible we do this by filtering redundant information. First and foremost,
  if the expansion of 2 terms yields an exponent higher than n, the step is skipped
  and the information is omitted.

  for instance, in q(4), we would end up having to expand (x^4)(x^1) = x^5
  Since we only want information regarding x^n, anything > n will NEVER be
  relevant, as further expansion can only yield higher values.

  In terms of optimization, we bring the time complexity down by several orders
  of magnitude, especially when values of n reach high numbers (n>50)
  """
def expand_factors(a,n):
  global exponent_dictionary


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
