# NACTF Write-up

## General skills

### 1. Intro to flags (10)
... just input the flag

### 2. Join the Discord (25) 
... flag is on the discord

### 3. What the hex (25)
The text to decode:
>49 20 77 61 73 2e 20 53 6f 72 72 79 20 74 6f 20 68 61 76 65 20 6d 69 73 73 65 64 20 79 6f 75 2e

Simply convert each hex to int and take the corresponding ASCII char. in python:

```''.join(chr(int(i,16)) for i in text.split(' '))```

### 4. Off-base (25)
The text to decode:
>bmFjdGZ7YV9jaDRuZzNfMGZfYmE1ZX0=

Simply convert from base64

### 5. Cat over wire (50)
Designed to teach the basics to ```netcat```. You can just ```nc``` to the server which will give you the flag.

### 6. Grace's hashbrowns
What we get:
>f5525fc4fc5fdd42a7cf4f65dc27571c

That looks supsiciously like an md5. And even if it doesn't, always google what you get, in many cases you will get an answer. In this case you get the inverse hash from a multitude of websites.

