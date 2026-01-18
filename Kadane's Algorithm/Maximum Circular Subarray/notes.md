For this one, my main issue wasn't necessarily Kadane's Algo. but it was tackling Circular based questions at their core. From the bruteforce I knew that we just had to test both regular subarrays and wrapped subarrays. 

In hindsight, the correct way to approach circular based questions, is to one start with the regular version and then figure out what does "Circular" actually allow? 

Try classifying answers that would be valid if it wasn't circular, then consider circular (wrapped vs non-wrapped). Can we apply the regular approach for a regular subarray and then maybe reuse it for the wrapped ones?

# KEY - Reframing circular (wrapped) cases as something else (like "total - something (middle section)", or suffix + prefix)

Once we reframe, we try figuring out if that "excluded" thing is a known problem that we could tackle or reuse some pattern on it.