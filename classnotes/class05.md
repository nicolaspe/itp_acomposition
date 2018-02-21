# Algorithmic Composition - Feb

## [chucK](http://chuck.cs.princeton.edu/)
Is a music programming language created by Ge Wang, Rebecca Fiebrink and Spencer Salazar. It is **strongly timed**, meaning its elemental component is time! It is written in C++, from the [Synthesis Toolkit] (https://ccrma.stanford.edu/software/stk/)

csound | chucK
-------|-------
orc + sco | code in chuck language
orig.render | realtime
strong dichotomy | none
mostly static | interactive

- Csound interfaces two files, Max has audio rate vs control rate, Chuck controls everything according to the time.
- runs with a Virtual Machine which keeps track of the shreds
- It can be used on the terminal with the `chuck` command
- *miniAudicle* is the GUI for chucK
- has a lot of puns (every *thread* is called a *shred*, so we have the *shreduler*, etc etc)
- Is more interactive (like super collider), hence **good for live coding!**

The main thing you do in Chuck is advance the clock. If you don't advance the clock, you don't have anything, you don't hear anything


### let's code/shred!

- `=>` chuck command! how you assign or connect all the stuff
- `@=>` a **reference pointer**! you use this to assign (chuck) arrays
- `.cap()` length of an array
- `Std.` is the


### Going multi
[RTSKED](https://en.wikipedia.org/wiki/RTSKED) = Real Time Scheduler, created by Max Mathews on '82. It creates a clock and has a timed scheduler array of commands.

To do a multithread program, you need to fork a thread... In chuck you *"spork"* a *"shred"* (*sigh*). So, after you create a `fun`ction you do
```chucK
spork ~ function1();
```

There's more computational load in passing samples between threads, than having threads repeat processes

- `~` SPORK operator
- `fun` is a function


### Record 😃
Basically, you take the `dac` (it's global!), you give it volume, take the wave out and plug it into a `blackhole()`!!
```
fun void recordIt(){
	"foo.wav" => string filename;
	dac => Gain g => WvOut w => blackhole();
	filename => w.wav.Filename;
	0.5 => g,gain;
	1 => w.record;

	// for how long do we want to record?
	10::second => now;

}
```


### How to be on synch???
We need to create a synch offset

```
100::ms*16 => dur synch;
synch - (now%synch) => now;
```


### STK instrument unit generators
... are based on physics models that describe the particular instruments. As they are modeled almost perfectly, they sound perfectly accurate. As they were done for the STK, they work for chuck! (as... STD's 🙄 *sigh*)




## References
- [John Chowning](https://en.wikipedia.org/wiki/John_Chowning), made the FM synthesis (and a very good reverb algorithm!)
- [David Tudor](https://en.wikipedia.org/wiki/David_Tudor), pianist on 4:33, made a lot of weird instruments. He made a piece called [Rainforest](https://davidtudor.org/Works/rainforest.html), where anything would be turned (with trnasducers) into speakers. Collab with Raushenberg and friends with John Cage.
- [GameTrak](https://en.wikipedia.org/wiki/Gametrak) failed game interface
