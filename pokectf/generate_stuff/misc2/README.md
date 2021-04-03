# Description

My RSA's been tasting a bit bland, lately.

# Provided

- `out.txt`

# Solution

We see that the value for $e$ is extremely big. We might assume that the decryption exponent $d$ is not very large in this case, and that as such Wiener's attack or the attack of Boneh and Durfee applies.
This might work, but instead, upon further inspection, we observe that the ciphertext is in fact not encrypted at all.
As it turns out, $e = \lambda(N) + 1$, resulting in $m^e \equiv m \pmod N$.
