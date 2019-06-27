# FriendSpaceBookPlusAllAccessRedPremium.com

>Having snooped around like the expert spy you were never trained to be, you found something that takes your interest: "Cookie/www.FriendSpaceBookPlusAllAccessRedPremium.com"  But unbeknownst to you, it was only the  700nm Wavelength herring rather than a delicious cookie that you could have found.   It looks exactly like a credential for another system.  You find yourself in search of a friendly book to read.

>Having already spent some time trying to find a way to gain more intelligence... and learn about those fluffy creatures, you (several)-momentarily divert your attention here.  It's a place of all the individuals in the world sharing large amounts of data with one another. Strangely enough, all of the inhabitants seem to speak using this weird pictorial language. And there is hot disagreement over what the meaning of an eggplant is.

>But not much Cauliflower here.  They must be very private creatures.  SarahH has left open some proprietary tools, surely running this will take you to them.  Decipher this language and move forth!

## The problem

This is a typical reversing task. We get 2 files: one python script and one file containing a bunch of hex strings separated by newlines. Looking at the script we see that the script is a virtual stack emulator (probably even turing complete) that takes commands in the form of emojis. From a structural point of view we have 2 accumulators (1,2) and 1 stack. The available instructions are:

- add (add the last two values of the stack)
- sub (substract last two values of the stack)
- multiply (multiply last two value of stack)
- divide (divide second last value of stack by top of stack)
- modulo (modulo last second value of stack by top of stack)
- xor (xor last two values of stack)
- load (set selected accumulator to given value)
- pop (set selected accumulator to top value in stack)
- pop_out (pop last value in stack)
- clone (append last value of stack to stack)
- push (append value of selected accumulator to stack)
- jump_to (jump to address)
- jump_top (jump to location at top of stack)
- print_top (print top value of stack)
- if_zero, if_not_zero, find_first_endif (loop controls

To make it simpler, I wrote a small snippet that converts the emojis to plain english, making it easier to read. I also manually edited the jump_to adresses (denoted by a basketball) and return addresses (denoted by a pencil/cigarette).

## Approach

After running the code it becomes clear that something increments and it takes longer for each loop to print each letter. We clearly sees it's a url. To better understand exactly what is the limiting factor, I first tried to read the code as one would for an assembly dump, manually keeping track of the stack and accumulators. I especially tried to backtrack from the first printed character and that's when I noticed the following:

```
389:xor
390:printop
```

Aha, so immediately prior printing, the top two values of the stack are xored and the result is printed. I set a breakpoint of sort immediately beforehand to see what is in the stack before each letter is printed and got the following result as top 2 stack values:

h: 106, 2
t: 119, 3
t: 113, 5
p: 119, 7
:: 49, 11
/: 74, 101
/: 172, 131
e: 242: 151

Ok, this is interesting. I'm a simple guy, I see increasing numbers, I think mathematical series. A quick google search reveals that this is the [palindromic primes](https://en.wikipedia.org/wiki/Palindromic_prime) series. A palindromic prime is a prime number that reads identically from left to right. There are several ways to construct them but you can also just copy them. 

But where do the numbers come from? A quick look at the pseudo-assembly dump reveals a series of load operations at the very beginning of the program. The stack after the last load looks like this:

```[0, 17488, 16758, 16599, 16285, 16094, 15505, 15417, 14832, 14450, 13893, 13926, 13437, 12833, 12741, 12533, 11504, 11342, 10503, 10550, 10319, 975, 1007, 892, 893, 660, 743, 267, 344, 264, 339, 208, 216, 242, 172, 74, 49, 119, 113, 119, 106]```

Thus all we need to do is to reverse the list and xor each element with the palindromic prime at that index, yielding:

```http://emoji-t0anaxnr3nacpt4na.web.ctfco```

So definitely on the right track. I assumed that the end was going to be ```mpetition.com``` and it actually does directs us to a website that looks like a website for cats.

## Going off on a tangent

I spent the better part of 2 hours mapping the webiste (using one of my earlier scripts, basically DFS) and trying to find the hidden meaning, which I still think exists, but got nowhere. I hope to expand this section in the future and prove myself right.

## Solving

I went back to the code and noticed that there are 2 more sections of loading. The first one between instructions 404 and 557 and the second between 583 and 997. Essentially, these are the thrid and second part of the url which we need. The trick however, is that the palindromic primes series skips several numbers a few times and we to identify which one.

First we reset the stack, set the instruction pointer to the respective sections and then let it run until the section end to look at our stack. Second and third part look like this:

```
part 2: [98426, 97850, 97604, 97280, 96815, 96443, 96354, 95934, 94865, 94952, 94669, 94440, 93969, 93766]
part 3: [101141058, 101060206, 101030055, 100998966, 100887990, 100767085, 100707036, 100656111, 100404094, 100160922, 100131019, 100111100, 100059926, 100049982, 100030045, 9989997, 9981858, 9980815, 9978842, 9965794, 9957564, 9938304, 9935427, 9932289, 9931494, 9927388, 9926376, 9923213, 9921394, 9919154, 9918082, 9916239]
```

Now we know that the first letter of the second part will be ```m```. So all we need to di is find the index of ```ord(m)^93766``` in our palindromic primes list, which turns out to be index 98. So we simply repeat the operation for part 1 but take 98 as our starting point in the palindromc primes list, xor pairwise and promptly get:

```mpetition.com/```

Ok, great job but now we don't know what the first letter of the third part is. Well, we do know there is a palindromic prime somewhere so how about trying to xor the first item of part 4 (```9916239```) which each char and see if we get a palindrome? Jackpot! The first letter is ```h``` and the corresponding palindrome is ```9916199```.

Now at this point I ran into a problem with mz palindromic primes generator because a) it sucked, b) the numbers were too large so I had to resort to downloading a prime list (first 10mio) and then getting all palindromic ones. But pretty soon it emerged that the index of our last first palindormic primes was 764. Repeat what we did in the prvious 2 steps and we get the final part:

```humans_and_cauliflowers_network/```

So our final url is : ```http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/````

And voila, visiting the site and clicking the few profiles finally yields the flag! It was a great challenge, one of the better ones in recent memory and I wish there were more like this!



