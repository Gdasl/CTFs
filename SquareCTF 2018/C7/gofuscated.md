# Gofuscated

>The very first settlers didn’t have a lot of confidence in their hand-assembled C6 system. They therefore built C7, an advanced defense system written in Golang.
Given the source code, can you find the correct input?

## Examining the code

This challenge took me a little while, mostly because I am not familiar with golang at. all. I got stuck on the large numbers of rounds and basically just tried debugging randomly. All the while I was transcribing the code to python to better understand it. One line struck me as interesting:

```
input = compute4(input)
if !another_helper(input) {
		panic("invalid input!")
	}
```

Looking through the code, it didn't seem like anything else was being done to input. So this looked like the only gateway. I looked at the compute4 function more closely:

```
func compute4(input string) string {
	rand.Seed(42)
	m := make(map[int]int)
	for len(m) < 26 {
		c := rand.Int()%26 + 'a'
		if _, ok := m[c]; !ok {
			m[c] = len(m) + 'a'
		}
	}
	r := ""
	for _, c := range input {
		r = fmt.Sprintf("%s%c", r, m[int(c)])
	}
	return r
}
```

I'm a simple guy: I see rand.Seed(x), I immediately start getting suspicious. Turns out it's a simple scramble function and the scrambling is deterministic. The another_helper looks like that:

```
func another_helper(input string) (r bool) {
	r = true
	for i, v := range input { //i is positiion, v is ord(c)
		for j, w := range input {
			r = r && (i > j || v <= w)
			fmt.Print(r)
			fmt.Print("\n")
		}
	}
	return
}
```
basically it checks for each c in a string if it's ord is higher than the previous one, i.e. the string has to be in ascending ordinal order.

## Solving

I took the easy way out. All I needed was and ```input``` where ```compute4(input)```returns a series of ascending ord, 26 chars long. I simply reversed the map function in the golang, gave 'ab..z' as input, feeded the output to the program as input and voila, flag received.
