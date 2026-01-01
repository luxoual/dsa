# House Robber I

Top - Down: 

Start with the bruteforce recursive approach, figure out our basecases that we want to stop at;
Look for the repeatable calculation or state that we always return to, using memoization to save calculations;

Bottom - Up:

Similar but without the recursion, we are starting from the base cases instead of from the "top".
Using the same repeatable calculation or state that we found earlier, but noticing what information do we really need;
Tabulation instead of memoization to save space;

*** Stating what this current position represents in the scale of the entire problem (similar to recursion), lets you address what each value really represents

# House Robber II

Goes back to the idea of what this current position (or input) represents, where the clever trick here is that we can use the same approach/algorithm as "House Robber I", except juggle our results of an array with [0, n-1] and [1,n], since we don't want to include the first and last houses together.