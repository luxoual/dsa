# First Thoughts
The name of the question already rang a few bells in my head with previous valid parenthesis questions, which typically involved the usage of a stack to keep track of opening parenthesis, where we append one when we find one, and pop one when we find a closer.

The main difference here is the wildcard, which can be either a opener, closer, or an empty string. My initial thoughts were that I could just
keep track of how many we have and essentially use it if we need it (i.e, we get a closer without an opener, then we can use a wildcard), and initially I thought, at the end if we still have any openers then all we need to do is calculate wild - openers > 0.

This was incorrect though, because just because we have wildcards at the end, doesn't necessarily mean all of them can be applied to the openers.

# Post First Hint

The hint is what told me that my current wild - openers > 0 logic was flawed. It brought to my attention the importance of knowing if a wildcard comes after a opener. In this case, that means we need some way of tracking the indexes of the wildcards so that we know if they come after an opener.

My solution from here was to keep 2 arrays: stack and wild, which contained indices of openers and wildcards.

After going through the entire string, if we still have openers and we have some wildcards, we start from the back of the arrays to see if we can apply any wildcards to any openers (wild[-1] > stack[-1]). If we can apply one, then we pop them from their arrays, which represents closing up an opener. At the end, we'll either have wild be empty or stack be empty, and at that point if we still have openers then we return False, else we are chilling.