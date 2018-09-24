# Anticaptcha

> Wow, this is a big captcha. Who has enough time to solve this? Seems like a lot of effort to me!

## The setup
We are given a webpage with a bunch of captchas (around 600), where you have to find gcd, primality or other asinine stuff. 

## The solving
Looking back, submitting an empty form always returned ```6 questions wrong``` which should have tipped me off that there were only 6 special questions to be answered. However, I went the hard way and scripted an auto parser that splits the initial response when calling the website into it's parts, analyses each question and adds the answer to an array (I had all the scripts already). There were 6 sepcial questions about capitals and mountains which I hardcoded like a dumbass. Running the script then returned the flag. Easy as pie.
