# Algorithmic Composition - Jan 31

## csound

`$csound blah.orc blah.sco -o foo.wav`

where:
- `blah.orc` is the orchestra file (how they sound)
- `blah.sco` is what they play (score)
- `-o foo.wav` outputs the render to a wav file

comments with `/* */` or `;`!!!! (yeah, seriously)


**[Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon)**

#### Variables
- `sr` sample rate
	- CD quality is 44.1kHz (double the Nyquist -Harry Nyquist- freq)
- `kr` says every how many samples csound checks for an event
	- `ksmps` could be used instead, but determining the ms
- `nchnls` number of channels
- `oscil` creates an oscillator, which can output to...
	- audio, if the variable name starts with `a`
	- frequency, if the variable name starts with `k`
- `kamp` sets the volume. The oscilator goes from -1 to 1, but the volume can go as high as 32767!
- `out` says where it goes

#### CsScore
- `f <table #> <start> <size> <genvalue> <harmonics!>`
	- `genvalue = 10`
- `i <instrument #> <start> <duration>`

**[Tom Dimuzio](http://www.thomasdimuzio.com/)** *Heaven to Stairway*

**[John Oswald]** *Plexure* > Plunderphonics
