# Poke A Mango

>Gotta get them mangos

## The setup
You get an apk package which can be easily opened and its juicy contents accessed. There are a few important files (all written in js, the poor man's python): server.js, map.js and score.js

## The solving
The idea of the game is basically the following:
```
1) Get user location
2) Send user location to server
3) Get List of Mangos in vicinity
4) User somehow catches mangos
5) "Catch" command is sent to server along with user uuid and mango uuid
6) Check if total mangos caught is higher than 137, if yes, return the flag
```

This implies that once a mango is caught, it can't be recaught. This was actually a very straight-forward solved. All you needed was to rewrite some of the code in python, get yourself a constant uuid, and send different locations to find mangos. I ended up bruteforcing it by downloading a list of major city with longtitude and latitue, and feeding it to the script until the total caught was high enough to get the flag.
