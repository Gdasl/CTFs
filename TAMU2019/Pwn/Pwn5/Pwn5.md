# Pwn5

## The problem

Straightforward follow up from pwn4, ls as a service. Basically send the arguments ```args``` you want and the shell will evaluate ```ls args```. Now here's the rub: in this one, you can only send up to 3 chars. So no fancy shmanzy stuff possible like in pwn4 where you simply concatenate commands. 

## The solving

There is obviously a buffer overflow here and you could probably have done something techincally complex and calculated offsets etc. etc. However, I gathered from the discord that there was another way that didn't involve anything other than a keyboard. Given the constraints, that meant that it had to be a 3 char command. 

I spent some time looking up different bash commands, secret shortcuts and dubious workarounds. I stumbled upon some personal page where some guy described how much he liked vim(!!!) and how he had a shortcut for that purpose (because typing ```vim``` instead of ```vi``` is sooooo exhausting).

That was the break I needed. Sends ```&vi``` opens the vim editor on the target machine. From there simply type ```:o flag.txt``` to open the flag and read it!
