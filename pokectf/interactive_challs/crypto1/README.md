# Description

I feel like I'm forgetting a few things. It's probably not important, just ship it!

# Provided

- almost_encryption_standard.py
- Connection to the python file running, with access to flag.txt

# Solution

It's an implementation of AES, without the SBOX/SubBytes step, and without MixColumns (and a weird key derivation because I'm lazy).

For a first solution (that was unintended initially, because I wanted to make the source shorter and not implement mixcolumns), we can observe that the composition of all ShiftRows and AddKey operations overall simply results in a single key addition (when we consider the round keys as totally) and transposition.
On top of that, we can also separate this into the action on each row of the matrix.

The way the reference solution then approaches this might not be optimal, but it works:
we try all permutations of both the row of the IV and the row of the ciphertext, derive the corresponding part of the keystream, and check against a second known plaintext/ciphertext pair if this would be correct.
Once we can solve a single block like this, from IV and ciphertext block, we can simply use this in a cbc decryption format to recover the entire flag.

See `solve_no_mixcolumns.py` for an implementation of this approach.

Fun fact: I realised and implemented this version only some time after the challenge was released. I was happy to be able to solve it still before someone else got first blood.

In the original solution, we take a more math-based approach, and we notice that the absence of the S-box gives us some very nice properties. Notice that the ShiftRows operation is a linear transformation when regarded over the individual bits of the state (in particular, it's a permutation, which can be seen as a $128 \times 128$ row-permutation of the identity matrix). The AddKey operation in turn is simply addition mod 2.

So here we introduce the form we'll be working with for our state: a vector of length 128 over $\mathbb{F}_2 = \{0, 1\}$. In short, this just means that addition is performed modulo 2, aka as xor.
Then if we write the round keys as $\mathbb{k}_i$ (boldface indicates a vector), the ShiftRows matrix as $\mathsf{SR}$, encryption round $i$ for state $\sigma_i$ comes down to: $$\sigma_{i + 1} = SR \times (\sigma_i + \mathbf{k}_i),$$
and when we look at this more closely, we can see that multiple rounds can still be expressed in the form $$\mathrm{ciphertext} = M \times (\mathrm{plaintext} + \mathbf{\kappa}) = M \times \mathrm{plaintext} + M \times \mathbf{\kappa} = M \times \mathrm{plaintext} + \mathbf{\kappa'},$$
for some $\mathbb{F}_2$ matrix $M$ and vectors $\mathbf{\kappa}$ and $\mathbf{\kappa'}$.

So overall, this block cipher is an affine transformation, and those can be solved by linear algebra. We need 129 plaintext/ciphertext pairs (128 for the bits of a block + 1 for the affine constant). To get these, even though we can't query the oracle 129 times, we can just send longer messages and extract pairs from the CBC ciphertext. With those, we can solve a system of $\mathbb{F}_2$-linear equations to recover a matrix that can decrypt any arbitrary block for us.

With that matrix in hand, we can then apply regular CBC decryption techniques to recover the flag. This approach, as I implemented in sage, can be found in `solve_affine.sage`.
