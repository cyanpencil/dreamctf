# Description

If at once you don't solve a challenge, ask your parents to solve for you :D

# Provided

- A link to a running version of the website, serving its own source code with access to the flag

# Solution

A simple path traversal, trying to highlight a directory gives us a directory listing. Traversing up the directory tree, we see `flag.txt` in the listing of the parent directory, so we can just highlight that. `?highlight=../flag.txt`
