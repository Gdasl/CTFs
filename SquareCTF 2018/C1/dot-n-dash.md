# dot-n-dash

>The instructions to disable C1 were considered restricted. As a result, they were stored only in encoded form.
The code to decode the instructions was regrettably lost due to cosmic radiation. However, the encoder survived.
Can you still decode the instructions to disable C1?

## Understanding the code

The challenge was written as a simple javascript. It took me way too long to understand how it worked to be honest. The belle of the ball was the encode function:

```javascript
function _encode(input) {
  var a=[];
  for (var i=0; i<input.length; i++) {
    var t = input.charCodeAt(i);
    for (var j=0; j<8; j++) {
      if ((t >> j) & 1) {
        a.push(1 + j + (input.length - 1 - i) * 8);
      }
    }
  }

  var b = [];
  while (a.length) {
    var t = (Math.random() * a.length)|0;
    b.push(a[t]);
    a = a.slice(0, t).concat(a.slice(t+1));
  }

  var r = '';
  while (b.length) {
    var t = b.pop();
    r = r + "-".repeat(t) + ".";
  }
  return r;
}
```

I saw relatively quickly that the returned string was simply an array of ints whereby the dots are delimiters and the number of dashes represent the int. So ```-----.---.``` would be ```[5,3]```. I worked my way back from there and what stumped me for a tremendous amount of time was the presence of Math.random(). I felt like however the string was transformed in the first part of the function, reshuffling the resulting array to the actual output array using random would be, well, random and non-deterministic. I first thought there was a seed but playing around with the encode function in the browser swed me the array was different every time.

## Understanding the code 2

I took a few hours off and went back at it. Specifically the first part. The presence of an 8 immediately made me think of binary but I didn^t see it immediately. After playing around some more, I realised that the function just transforms the char into binary, then either adds an element to the array or not depending on whether it's a 0 or 1. The element is dependent on 2 things:

1) The position in the binary array
2) The position of the char in the input string

That meant that as a general rule, the array as first translated is rising steadily. It also meant that per char, there would be as many elements in the array as there are non-zero bits in its binary representation. So the trick was to figure out, where does one character stop and another begin? Well, if you look at the first part of the function, j is added to the array. That means that j%8 would theoretically indicate which bit would be represented by an element in the array.

## Solving

Ultimately the solution was to:

1) Convert the dash-n-dot array to a normal array representation

2) Order values in descending order

3) Find j for each value

4) Split array in sub-arrays, 1 per char

5) Convert sub-array back to char (easily done since we know j so if j is not None for i we know that the i-th bit is 1, all others are 0)

And voila, done
