# Admin panel

> I think I've found something interesting, but I'm not really a PHP expert. Do you think it's exploitable?

# Solving

I didn's solve this challenge (or any others for that matter) during the competition but got relatively close. Basically, trying to access login.php would  immediately check if there was a cookie names otadmin set. If yes, it would check if it's in the correct format whis was ```{'hash':[some hex]}```. If the has equaled the stored hash, it would display the flag. If not but the cookie was still in the correct format, we'd get a hint namely the ```&``` between the hash of the password and a fixed char. This told us whether a character of the pass string was a digit (0-9) or a letter (a-f). Thus we saw that the md5 of the pass has the form ```d d d l l l d l d d l d d d l l l l d d d l d d l d l d l l d d```.

The exploit was precisely that: comoparison in php when comparing two thing, stop comparing as soon as it stops being digits (that's more or less the gist of it). So all we needed was to brutefore the all 3 digits numbers until we got a hit.
