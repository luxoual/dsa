# Initial Thoughts

A question that Vincent apparently did for Vanguard OA, started with noticing that we wanted to create a non-palindrome from a palinedrome that would be the lexicographically smallest string. This instantly made me think about changing a singular letter of the palindrome to the letter 'a'. I then thought about the edge cases, like "when would turning a letter to an a, not work?". I came up with the situation where we have a palindrome of all 'a's, thus we'd need to change a letter to the letter 'b' instead.

But which letter would we change? Initially I thought it'd be the first letter, but after running my original code, I realized that we actually needed to change the last letter, since 'aaaaab' comes before 'baaaaa'. Something else I noticed was that, since we were using palindromes, I didn't need to actually loop through the whole string, because I would know the 2nd half would be the same as the 1st half.

Thus, I looped through half way through the string, it didn't matter if it was odd or even length, because I was only grabbing the half I actually needed to check. If i find a letter that wasn't an 'a', id change that letter and return. If I never found an 'a', I would change the last letter to a 'b' and return.
