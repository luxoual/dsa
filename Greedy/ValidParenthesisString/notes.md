# First Thoughts
The name of the question already rang a few bells in my head with previous valid parenthesis questions, which typically involved the usage of a stack to keep track of opening parenthesis, where we append one when we find one, and pop one when we find a closer.

The main difference here is the wildcard, which can be either a opener, closer, or an empty string. My initial thoughts were that I could just
keep track of how many we have and essentially use it if we need it (i.e, we get a closer without an opener, then we can use a wildcard), and initially I thought, at the end if we still have any openers then all we need to do is calculate wild - openers > 0.

This was incorrect though, because just because we have wildcards at the end, doesn't necessarily mean all of them can be applied to the openers.