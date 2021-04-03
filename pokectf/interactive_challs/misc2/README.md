# Description

Box outside the think.

# Provided

- network connection running boxed_in

# Solution

The AI is indeed a perfect player, that will never lose. It can at worst tie, which is not enough.
To exploit it, we need to think outside the box, and observe that while negative numbers are not properly read, we can still use an integer overflow to place something out of bounds of the grid that still counts for a win if we have 3 pieces in a row that way.
