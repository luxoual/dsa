# Beginning

First off, I didn't really time this one, but I honestly should have. Bit Manipulation questions are often just knowing certain tricks and etc. that make it sort of hard or impossible to do if you didn't have some knowledge ahead of time.

Looking at this question, it was a simple Full Adder question, until it got into negatives and that's when I forgot what to do there.

One mistake I was making was not calculating the carry correctly based on shifted bits. Also took a little bit to remember/get used to using boolean operators and masks to find certain bits or check things.

One repeatable pattern from this was how to convert from Python's number which has infinite bits into a fixed bit amount and then how to convert it back into the negative version.

Specifically, we always do (a & mask) to limit the number of bits we are working with (in this question it was 32). So if we have a negative number that has 11111... , then this way we are technically converting it to a positive in Python but still addressing it as a negative number.

Once we are done operating on it, we can check if its a negative number if the value of it is greater than the max positive Int in our range (which is the biggest number without a 1 in the 32nd bit -> 0x7FFFFFFF). If its greater than the max int, we know its negative and we can convert back by subtracting 2**32.

# The pattern

For other ranges here is the basic idea:

# Forcing into N Bits

x & ((1 << N) - 1)
       ^ Mask ^

# Converting back to negative

if x >= (1 << (N - 1)): // The start of the range of negatives
    x -= (1 << N)
