# Tux Kitchen

>I need to bake it!

## Problem

The function works as follows:

1) Get a random key

2) Create a random list of numbers based on the key and 3 other random constants that is as long as the flag

3) Multiply each number by the order of the character of the flag

4) Xor each resulting number by ```MY_LUCKY_NUMBER``` then add ```MY_LUCKY_NUMBER * len(flag)``` to the last number in the list

## Solving

All we need is to reverse the last function, which is trivial. After this, we know that each number is a random number ```r_n``` multiplied by the order of the character. The point here is that ```r_n``` never matters since, over several runs, it will change but the order of the character wont. Thus, all ```r_n``` for equal n over serval runs will have the same value.

So over 5 runs we will have, at position 0:

```
f_0_0 = r_0_0 * ord(f[0])
f_0_1 = r_0_1 * ord(f[0])
f_0_2 = r_0_2 * ord(f[0])
f_0_3 = r_0_3 * ord(f[0])
f_0_4 = r_0_4 * ord(f[0])
```

Here ```f_0_k``` is the reversed number at position 0 and ```r_0_k``` the random number for round ```k``` at index 0. What we see is that those 5 nubers will have ```ord(f[0])``` as a common multiple. Therefore all we need is to get a large enough sample size, calculate the gcd for each position.

