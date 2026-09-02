# Solution

Similar to a Full Adder problem, where we need to handle a carry between digits. So for the scenarios where the number of digits would increase because of the extra 1, I made a results array that was 1 longer than the initial digits array. Then I started off with the least significant digit with a 1 in the results array. Then I would grab the carry from the results array, add it to the current digit, and see if there was an overflow, if there was, then I would add 1 to the next significant digit (via the results array).

Then simply I would return the entire results array if the first digit isnt a trailing 0, else I would return results[1::]
