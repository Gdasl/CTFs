 # Unagi (200)
 
 > come get me
http://web.chal.csaw.io:1003

### Intro

Full disclosure: didn't solve this during the competiton. I had the 90% correct payload and also the right idea but for some reason it didn't work when I did it. I just retried and now it works. Oh well :(

### Solution

What we have is essentially an xxe vulnerability that allows us to access arbitrary entities outside of the scope of the xml. It's very useful and there is literature aplenty. We can upload an xml on the server whill will parse it and display the parsed results, provided they're in the right format, as indicated by the website.

The added twist here was the WAF protection which blocked crude attempts. There are several ways to bypass such checks, as outlined in [this excellent post](https://lab.wallarm.com/xxe-that-can-bypass-waf-protection-98f679452ce0). I tried all of them but apparently not diligently enough since the change in encoding should have worked: by leaving the header unencoded but then adding an encoded body, e.g. in ```UTF-16```, the WAF checker will assume it's ```UTF-8```, read the encoded part as junk so disregarding it and thus letting us input anything we want. In the end the payload was very straightforward:

```xml
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///flag.txt'>]>
<users>
    <user> 
        <intro>&test;</intro>
    </user>
</users>

```

Write that in a file, then convert to ```UTF-16```: ```cat pay.xml | iconv -f UTF-8 -t UTF-16BE > pay16.xml```. Upload it and the flag is displayed.
