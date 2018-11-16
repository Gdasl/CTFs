package main

import (
	"encoding/hex"
	"fmt"
	"math/rand"
	"regexp"
	"strings"
	"time"
)

/**
 * important computation, part 1 of 2
 */
func compute1(done chan bool) {
	fmt.Print("starting animation")
	//fmt.Printf("\n\n\n\n\n\n")
	frames := []string{
		"\033[6A\r               X \n                  \n               O  \n             Y/|\\Z\n               |\n              / \\\n",
		"\033[6A\r                 \n             X    \n             Y_O  \n               |\\Z\n               |\n              / \\\n",
		"\033[6A\r                 \n             XY   \n              (O  \n               |\\Z\n               |\n              / \\\n",
		"\033[6A\r              Y  \n                  \n             X_O  \n               |\\Z\n               |\n              / \\\n",
		"\033[6A\r               Y \n                  \n               O  \n             X/|\\Z\n               |\n              / \\\n",
		"\033[6A\r                 \n                 Y\n               O_Z\n             X/|  \n               |\n              / \\\n",
		"\033[6A\r                 \n                ZY\n               O) \n             X/|  \n               |\n              / \\\n",
		"\033[6A\r                Z\n                  \n               O_Y\n             X/|  \n               |\n              / \\\n",
	}
	ctr := 0
	for {
		select {
		case <-done:
			return
		case <-time.Tick(time.Duration(250) * time.Millisecond):
			ctr++
			s := frames[ctr%len(frames)]
			x := []byte("\033[32mo\033[39m")
			y := []byte("\033[34mo\033[39m")
			z := []byte("\033[35mo\033[39m")
			for t := 0; t < ctr/len(frames)%3; t++ {
				x = xor_slice(xor_slice(x, y), z)
				y = xor_slice(xor_slice(x, y), z)
				z = xor_slice(xor_slice(x, y), z)
				x = xor_slice(xor_slice(x, y), z)
			}
			s = strings.Replace(s, "X", string(x), 1)
			s = strings.Replace(s, "Y", string(y), 1)
			s = strings.Replace(s, "Z", string(z), 1)
			//fmt.Print(s)
			//fmt.Print("some new crap 2")
		}
	}
}

const Output = 16
const Space = 100000
const Rounds = 100000

/**
 * important computation, part 2 of 2
 *
 * pro-tip: you should always roll your own crypto. This prevents the NSA or other attackers from using
 * off-the-shelf tools to defeat your system.
 */
func compute2(data []byte, done chan bool) chan string {
	r := make(chan string)

	go func() {
		state := make([]int, Space)
		j := 0
		i := 0
		for i = range state {
			state[i] = i
		}

		for t := 0; t < Space*Rounds; t++ {
			i = (i + 1) % Space
			j = (j + state[i] + int(data[i%len(data)])) % Space
			state[i], state[j] = state[j], state[i]
		}

		o := make([]byte, Output)
		for t := 0; t < Output; t++ {
			i = (i + 1) % Space
			j = state[(state[i]+state[j])%Space]
			o[t] = byte(j & 0xff)
		}

		done <- true
		r <- hex.EncodeToString(o)
	}()

	return r
}

/**
 * Some other computation.
 */
func compute3(r chan byte) chan byte {
	s := make(chan byte)
	go func() {
		var prev byte = 0
		for v := range r {
			if v != prev {
				s <- v
				prev = v
			}
		}
		close(s)
	}()
	return s
}

/**
 * These aren't helpful, right?
 */
func compute4(input string) string {
	rand.Seed(42)
	m := make(map[int]int)
	for len(m) < 26 {
		c := rand.Int()%26 + 'a'
		//fmt.Print(c)
		//fmt.Print("\n")
		if _, ok := m[c]; !ok {
			m[c] = len(m) + 'a'
		}
	}
	//map function is always the same
	fmt.Print("\n")
	fmt.Print(m)
	fmt.Print("\n")
	r := ""
	for _, c := range input {
		r = fmt.Sprintf("%s%c", r, m[int(c)])
		fmt.Print(r)
		fmt.Print("\n")
	}
	return r
}

func reverseMap(m map[int]int) map[int]int {
	n := make(map[int]int)
	for k, v := range m {
		n[v] = k
	}
	return n
}

func compute4inverse(input string) string {
	rand.Seed(42)
	m := make(map[int]int)
	for len(m) < 26 {
		c := rand.Int()%26 + 'a'
		//fmt.Print(c)
		//fmt.Print("\n")
		if _, ok := m[c]; !ok {
			m[c] = len(m) + 'a'
		}
	}

	//map function is always the same
	fmt.Print("\n")
	fmt.Print(m)
	m = reverseMap(m)

	fmt.Print("\n")
	fmt.Print(m)
	r := ""
	for _, c := range input {
		r = fmt.Sprintf("%s%c", r, m[int(c)])
		fmt.Print(r)
		fmt.Print("\n")
	}
	return r
}


/**
 * A boring helper function
 */
func xor_slice(a []byte, b []byte) []byte {
	r := make([]byte, len(a))
	for i, v := range a {
		r[i] = v ^ b[i]
	}
	return r
}

/**
 * Another boring function
 */
func panicIfInvalid(s string) {
	if !regexp.MustCompile("^[a-zA-Z0-9]{26}$").MatchString(s) {
		panic("invalid input!")
	}
}

/**
 * Last one
 */
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

/**
 * Pro-tip: start here.
 */
func main() {
	input := "nxelvzqaifsyhojudrbcwgptmk"
	panicIfInvalid(input)



	done := make(chan bool)
	go compute1(done)
	fmt.Print("starting compute2")
	h := compute2([]byte(input), done)
	fmt.Print("\nfinished compute2")
	s := make(chan byte, len(input))
	r := compute3(s)
	for _, c := range input {
		s <- byte(c)
	}
	close(s)
	fmt.Print("\nfinished close s")
	input = ""
	for c := range r {
		input = fmt.Sprintf("%s%c", input, c)
	}

	fmt.Printf("input before compute4: %s",input)
	lolzer := compute4inverse("abcdefghijklmnopqrstuvwxyz")
	fmt.Printf("actualer: %s",lolzer)
	fmt.Print("\n")
	panicIfInvalid(input)

	fmt.Print("\nstarting compiute 4")
	input = compute4(input)
	fmt.Printf("\ninput after compute4 (shuffling): %s",input)
	fmt.Print("\nfinished compiute 4")
	input2 := compute4inverse(input)
	fmt.Printf("\ninverse compute: %s",input2)
	fmt.Print("\n")
	if !another_helper(input) {
		panic("invalid input!")
	}
	panicIfInvalid(input)

	flag := <-h
	fmt.Print("\nwhat the fuck is going on here 2\n")
	fmt.Printf("fAILED! 🚩  = flag-%s\n", flag)



	fmt.Printf("Congrats! 🚩  = flag-%s\n", flag)
}

//80f816ac68b72430ca5f78327d630ec7
// author: Alok
