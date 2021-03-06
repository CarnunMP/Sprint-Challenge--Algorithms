#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Each loop of the while, a increases by n^2. Once a is larger than n^3, it stops. n^3 / n^2 = n, so this will mean an average of n loops. So O(n).


b) Outer loop runs n times. Inner loop runs n / 2 times. So time complexity is O(n^2), as we can disregard constants.


c) The function recurses n times, so time complexity = O(n).

## Exercise II

Seems like a perfect candidate for a binary search! As we're essentially looking for the first floor _smaller than_ a certain, unspecified amount, in a sorted list of floors (a.k.a. a building).

So, if the number of floors is n (and we suppose ground = 1, the floor above it = 2, and so on), I'd start out at floor ceil(n/2) and drop an egg. If it doesn't break, I'd move to floor current_floor + ceil( (n - current_floor ) / 2 ) — the half-way point between myself and the roof! — as I know the egg won't break on any of the floors below me, so I can eliminate them. If the egg _does_ break, I do the same in reverse: move to floor ceil(current_floor / 2), eliminating the floors above me. And I continue like this, eliminating half of the remaining floors each loop through the algorithm, until either:
  - I move down _one floor_ from a floor on which the egg breaks to a floor where it doesn't. I then know the first of those (the floor I moved _from_) is floor f.
  - I move up _one floor_ from a floor on which the egg doesn't break to a floor on which it does. I then know the second of those (the floor I moved _to_) is floor f.

More or less! :)

  As for runtime complexity, I expect O(log(n)), as it's not constant, but like any divide-and-conquer algorithm it should be sub-linear.