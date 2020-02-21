#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Each loop of the while, a increases by n^2. Once a is larger than n^3, it stops. n^3 / n^2 = n, so this will mean an average of n loops. So O(n).


b) Outer loop runs n times. Inner loop runs more than once, but less than n times. So time complexity is O(nlog(n)).


c) The function recurses n + 1 times, so time complexity = O(n).

## Exercise II

Seems like a perfect candidate for a binary search! As we're essentially looking for the first floor _smaller than_ a certain, unspecified amount, in a sorted list of floors (a.k.a. a building).

So, if the number of floors is n (and we suppose ground = 1, the floor above it = 2, and so on), I'd start out at floor ceil(n/2) and drop an egg. If it doesn't break, I'd move to floor current_floor + ceil( (n - current_floor ) / 2 ) — the half-way point between myself and the roof! — as I know the egg won't break on any of the floors below me, so I can eliminate them. If the egg _does_ break, I do the same in reverse: move to floor ceil(current_floor / 2). And I continue like this, until either:
  - I move down _one floor_ from a floor on which the egg breaks to a floor where it doesn't. I then know the first of those is floor f.
  - I move up _one floor_ from a floor on which the egg doesn't break to a floor on which it does. I then know the second of those is floor f.

  As for runtime complexity, I expect O(logn), as it's not constant, but it like any divide-and-conquer algorithm it would be sub-linear.
