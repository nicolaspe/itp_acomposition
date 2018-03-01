# Algorithmic Composition - Feb 28


## Filter theory
How to smooth stuff? Like, any shit, signals, inputs or whatsoever?


### Smoothing by averaging (first order non-recursive low pass filter - FIR)
Just take the previous input level and average it with the last one.

y_n = (x_n + x_[n+1]) /2

You can also take the XX first values and average them all (XX order).


### First order recursive low-pass filter - IIR

```
smoothlevel = a1*smoothlevel + a2*miclevel

// where a1 = old, a2 = new, a1 + a2 = 1
```

The problem is that this is *infinite*. You will *never* get to the limit value.


### Biquadratic filter theorem ("biquad") ("2p2z")
So, the basic filters are
- lowpass
- hipass
- bandpass
- bandreject (notch)
- allpass

All these filters can be described with:
y_n = a*x_n + b*x_{n-1} + c*x_{n-2} - d*y_{n-1} - e*y_{n-2}

**[George Lewis'](https://en.wikipedia.org/wiki/George_Lewis_(trombonist)) [Voyager](https://www.youtube.com/watch?v=hO47LiHsFtc)** an interactive play between the artist and his computer. He uses this equation to *decide* what to do: it only knows about the last two things each has done and the thing the player is doing now.



## Logistic population

X_{n+1} = R * X_n * (1-X_n)



## Strange Attractors!
From Julien C. Sprott's book!

x =     sin(A*y) - z * cos(B*x)
y = z * sin(C*x) -     cos(D*y)
z = E * sin(x)

A, B, C, D, E = range of area


## [L-systems](https://en.wikipedia.org/wiki/L-system)
Designed by [Aristid Lindenmayer](https://en.wikipedia.org/wiki/Aristid_Lindenmayer), a hungarian botanist. There was a very interesting synergy in the 60's and 70's research field, that he wrapped up and used for his own studies:
- [Watson and Crick](http://www.history.com/this-day-in-history/watson-and-crick-discover-chemical-structure-of-dna) discover the double-helix structure of DNA
- [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert), teach kids how to code by drawing : [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). This programing language had a ["turtle"](https://en.wikipedia.org/wiki/Turtle_(robot))
  - He had a student called [John Maeda], who created [Design by Numbers].
	- His students were [Casey Reas] and [Ben Fry], who created [Processing].
	- And [Lauren McCarthy] studied under Reas and created [p5.js]
- [Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky) father of modern linguistics > [Generative Grammars]




`poly~ synthstrings~ `
