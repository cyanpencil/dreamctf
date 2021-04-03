# Description

Given the amount of rickrolling, I'm fairly sure this site is broken in some way. So that means it should be easy to become an admin, right?

# Provided

- `index.js`
- `package.json`
- A running instance of the site

# Solution

We can notice that the hash that is checked is actually the binary inverse of a fake flag, so it's very unlikely this is a real hash, and we certainly couldn't extract the flag from it.

What we see instead, is that the `whatsThis` function allows us to do prototype pollution. By sending the body `__proto__.is_admin=whatever`, and because there's an obvious typo in the `GET` handler, we can pass the condition and get the flag.

Most of the trickery is involved in making sure that all sessions have an individual prototype, since otherwise a single solver would make the flag appear for everyone.