# Beginning

First, since we were only dealing with 32 bit integers and we wanted to check for overflow, we had to define the borders (-0x80000000 and 0x7fffffff).

So when do we know when we are going to overflow? Well, if the current result is already greater than MAX // 10, then no matter what digit we add next its going to overflow. We deal with the negative side by doing something similar but instead of MAX // 10, we are dealing with -(abs(MIN) // 10), we use absolute value because we are dealing with integer division with negatives.

Shockingly, if we don't do integer divsion, this still actually works and is actually the only check we need.

If the result isn't past the boundaries, then we can multiply it by 10 and add the latest digit. We also have a check for if the number we are dealing with is negative so we know if we want to turn the digit we are working with negative.
