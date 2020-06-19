#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    If n > 0 input size n is going to always be bigger than a by *n so with a really big input its the operations are going to increase linearly so it can be greater than n^3. n^3/n^2 = n, O(n) time complexity.

b)
    The first loop is O(n) because each operation increases linearly based on input size. The second, while loop, is O(log(n)) because it talks half of the operations to run. For this reason its total this is O(n log(n)) time complexity.

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
