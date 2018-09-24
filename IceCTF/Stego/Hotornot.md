# Hotornot

>According to my friend Zuck, the first step on the path to great power is to rate the relative hotness of stuff... think Hot or Not.

## The setup
Oh boy this was a good one. We get a huge (68mb) file which upon closer examination reveals itself to be a patchwork of pictures of hot dogs and cute doggos of all sorts. Looking at it from afar, you distinguish some pattern. The reference in the challenge is actually not Zuck (hot or not was the first app that Zuckerberg coded while at Harvard where he basically dumped all the pictures from female undergrads and put them on a website where you could rate them, thus creating the ancestor of both facebook and Tinder). The giveaway was the hot dog pictures: in the HBO show Silicon Valley, Jin Yiang creates and app to detect hot dogs or not, which incedentally, while absolutely useless in its original scope, turns out to be great to filter out NSFW pictures on social apps. It works using machine learning, i.e. (simplified) you give the algo 10000 pictures of hot dogs, 10000 pictures of not-hot-dogs and trains it to recognize what is what.

## The bruteforcing
The size of the picture is 18710 x 18710. Assuming the pictures are also square, it left only a few possibilities, yielding a size of 210x210 pixels for each picture. A simple script to split them yields the 7569 individual ones. Now remained the matter of identiying them. I used a script frmo some silicon valley fan who recreated Jin Yiangs Algorithm and even provided a trained model. After a few small alterations and switching from my laptop to my main desktop, it took only around 20min to identify each as hotdog (=1) or not (=0).

## The solving
Once done, you get a binary sequence of length 7569. I first thought it could be a file but no dice. I then went back to the original image and the original split. the 87x87 tipped me off: QR code! It also made sense in light of machine models being only accurate of to a point (meaning even a 1% deviation, which is awesome, would yield ~70 wrong results). So basically, split the array in lines of 87 and write to csv, open in Excel. The QR is broken in that the 3 identifying squares (Top right/top left/bottom left) are missing but can be easily added manually. Scanning it gives the flag.

In short, it was a great challenge but it requires some familiarity with machine learning as well as some intuituion.
