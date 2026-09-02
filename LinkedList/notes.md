# Initial Thoughts

Originally my first thoughts were to use recursion to reach the end of the linked list, and then start deprecating from N while returning up. First we'd check the state of N, to see if it equals 0, then we are at the spot where we want to remove the node.

# What I actually did

Instead I initially thought that was kind of complicated and did a two pointer approach where I had a left/slow and a right/fast pointer which were N apart. Then I moved them at the same pace until the right side reached the end and the left pointer would be exactly where I need it to be to remove the node that we want.
