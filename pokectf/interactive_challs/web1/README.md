# Description

Check out my new Redirect as a Service website! 

# Provided

- A link to the website, highlighting its own source code, with access to flag.txt

# Solution

In general, we've got an ssrf vulnerability, with some filtering we need to bypass (we can't immediately inject `127.0.0.1` or `localhost`).

We have 2 alternative solutions:

- Make the ssrf to a website you control serving a redirect to `http://localhost:5000/flag`
- Bypass the localhost checks by using alternative IP encodings (as a single integer for example) or alternative IPs (like `0.0.0.0`), bypass the flag check through a double url encoding (e.g. `fl%2561g` for flag).
