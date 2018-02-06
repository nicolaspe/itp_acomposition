# Algorithmic Composition - Jan 31

## csound

`$: csound blah.orc blah.sco -o foo.wav`

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



## Examples

#### Oscillator
The different parameters are:
- `ifn`: instrument function
- `linen`: line envelope - (input amplitude, attack, duration, decay)
- `oscil`: oscillator - (amplitude, frequency, function)
- `out`: what goes out and to which channel

A score line looks like:
```
	i <#> <start> <duration> <frequency> <amplitude> <pan>
```

```
instr 1   ; instrument #1 - oscillator
  ifn = 1 ; waveform

  kmaxamp = 0.6
  aline linen kmaxamp, 0.3, p3, 0.7
  a1 oscil p5*aline, p4, ifn
  a2 oscil p5*aline, p4, ifn

  out a1*(1.0 -p6), a2*p6
endin
```

#### Sound file
The different parameters are:
- `soundin`: specifies source file - (filename, offset)
- `out`: what goes out and to which channel

```
instr 1
	a1 soundin "drums.aiff", p4
	out a1*0.2
endin
```

A score line looks like:
```
	i <#> <start> <duration> <offset>
```
