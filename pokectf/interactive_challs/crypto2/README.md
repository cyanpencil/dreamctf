# Description

I had some bad food. Please help me digest it.

# Provided

- `indigestion.py`
- a network connection running `indigestion.py`, with `flag.txt`

# Solution

We can construct an arbitrary hash output by appending a single block to an arbitrary message $m$:

Let $h_1 = H(m)$, $m'$ our appended block, and $h_2$ our target. Then we want that $S(h_1 \oplus m') = h_2$. Since the SBOX is a permutation, so is $S$, and as such we know $S^{-1}$ exists and we are able to simply compute it.
From there, we can very easily compute $m' = S^{-1}(h_2) \oplus h_1$.
Now by construction, $H(m || m') = h_2$.
