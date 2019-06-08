# CTF Tools
I am a foregtful person. Oftentime, I will use a tool for some task and then forget about it whne I solve a similar task 3 months later. I recently played a CTF where 4 of the challenges could have been solved by simply using the easiest tools available but somehow I didn't think of any. This mainly focuses on forensics & stego.

## Forensics
### Memory dump analysis

- Volatility

### File extraction

- binwalk

- foremost

---

## Steganography

### Basic tools

- exiftool

- TweakPNG

- Stegsolve

- zsteg (to extract LSB)

### Image encryption

- steghide

- https://futureboy.us/stegano/decinput.html


---

## Attack-automation

One idea would be to create an automatic common-exploit bruteforcer of sorts that would for instance parse an image and execute all sorts of analysis and return potential juicy bits. For instance extract all rgb layers (24 total) and check if any of those is a hidden QR code (common practice), check if the LSB contain anythin in flag format or plain text etc.
