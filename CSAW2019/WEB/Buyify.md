# Buyfy (500)

>We know other other e-commerce sites have had horrible bugs recently, but our IT department says with the new versions of our dependencies, everything will be fine...

>HINT: Templates are a prototype for fun and also, don't worry, you don't need rce

>By: itszn (ret2 systems)

>http://web.chal.csaw.io:1002

# TLDR and link

I didn't solve this one and apparently was very far from the solution. It did however really not involve any RCE. A good writeup is [here](https://github.com/terjanq/Flag-Capture/tree/master/CSAW%20CTF%20Qualification%20Round%202019/buyify#buyify-web-500-15-solves-by-terjanq). The TLDR was a ```handlebar``` zero day that apparently still works. There was a semi-red herring [here](http://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html) which I spent some time reading during the competition in an attempt to solve but it turns out this was patched, albeit only half-heartedly, hence the exploit here still worked without needing a constructor but using handlebar's helper functions syntax.
