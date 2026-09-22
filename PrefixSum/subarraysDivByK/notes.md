Prefix sums?

We were looking for (prefix[j] - prefix[i]) % k == 0
Now when is the difference between 2 numbers
divisible by k?
When 2 numbers have the same remainder after doing % k
then that means when you subtract those 2 numbers,
you'll get a value that is divisible by k

k = 5 a = 9 b = 4 c = 14
9 // 5 = 1 r-4
4 //  5 = 0 r-4
14 // 5 = 2 r-4

So we are just looking for prefixs that have matching
remainders, everytime we find a matching remainder, we
can make total times we saw that remainder - 1 new pairs
