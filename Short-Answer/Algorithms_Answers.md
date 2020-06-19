#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    If n > 0 input size n is going to always be bigger than a by n. So at worst it'll loop over one more time and it'll do this constantly no matter how large the input which is O(1) time complexity.

b)
    The first loop is O(n) because each operation increases linearly based on input size. The second, while loop, is also O(n) for the same reason so in total this is O(n^2) time complexity.

c)
    The function is being called recursively n times before reaching the base case so its O(n).

## Exercise II

while n > 1:
  start at middle building
  drop egg
  if egg is broken:
    remove all values > n
  else:
    remove all values =< n
  n/2,repeat above code

return n

time complexityL O(log n) because it's a binary search each call halves the input.
