# (c)Sound rendering

[Csound](http://www.csounds.com/) is extremely interesting. It is from 1984, where the constraints of computing power required a paradigm less demanding than real-time audio processing. Instead, a csound file has to be rendered before hearing the final result. (Though, modern computers can do it real-time just fine.) But this brings some clear advantages. You can build a composition with thousands of oscillators and instruments without a massive impact on your machine. And with today's technology, a 10 minute file could render in just seconds! At the same time, a score file doesn't have to be written in chronological order; csound organizes it automatically when rendering.

All these files can be found on [my GitHub repository](https://github.com/nicolaspe/itp_algorithmiccomp/tree/master/creations/csound).


<br>

## First c-steps
Each csound file is composed by an orchestra file (.orc), which defines the instruments, and a score file (.sco), which defines the notes each instrument plays.

For these experiments, I used rather simple instruments.
- a drum samples sound file with
- an oscillator
- a `pluck` instrument

I only used one "more complicated" feature, a *line envelope* (`linen`) for the amplitude, to introduce attack and decay.
```csound
k1 linen max_amp, attack_time, total_duration, decay_time
```

Each instrument is defined differently, but they always take the same three parameters, specified on the score file. After that, the meaning of each parameter depends on how each instrument is coded. For mine, I use the following structure:
- `p1` = instrument #
- `p2` = starting point
- `p3` = duration
- `p4` = frequency (offset when the instrument is a  sound file)
- `p5` = amplitude (max)
- `p6` = panning (for multi-channel output)

The Mac IDE for Csound is not very good (well, I didn't like it and crashed on me several times... the only useful thing is the information bar on the side), so I created the orc files + some javascript and python files to generate the score. Then, in order to render the audio file, enter the following on the terminal:

```bash
csound foo.orc bar.sco -o output.wav
```


<br>

## Non-linear layers
For the first week playing with csound, I experimented with this new tool (for me), by taking advantage of the non-linear approach to writing the score file: each layer can be written and appended to the document separately.

First, I created a percussion layer with the sound file provided, consisting of a random hi-hat rotation and an occasional snare. Then, I added 500 oscillator notes distributed normally on the 15 second track. The oscillator has a random base frequency and a "scale" of randomized multipliers, which were written at the beginning of the file.

[audio wav="http://itp.nicolaspe.com/wp-content/uploads/2018/02/alg_02_layers.wav"][/audio]


<br>

## MIDI experiments
After the second week of csound, I went into using MIDI to create more harmonic melodies. I am much more interested on creating *nice-sounding noise*, but in order to introduce complexity in rhythm and melody, harmony has to be kept simple. At the same time, it is easier to create something more coherent by messing up an ordered system, rather than trying to make chaos more organized.

I began by using the `pluck` instrument, which simulates the plucking of a string. This instrument plays random notes from a minor random scale.

[audio wav="http://itp.nicolaspe.com/wp-content/uploads/2018/02/alg_03_midi1.wav"][/audio]


Then, I added a drum base line. I lowered the speed from the layered experiment, added the kick drum and tried to add some syncopation to make the rhythm more interesting. The results were not very satisfactory, but not completely discardable.

[audio wav="http://itp.nicolaspe.com/wp-content/uploads/2018/02/alg_03_midi2.wav"][/audio]


For this last one, I decided against using the snare for the drum line and changed its speed. Also, I replaced the plucked instrument for an oscillator to have the contrast between the two of them. The difference between randomizing the timing of both instruments is clear, as the plucked instrument cannot be held for a long time.

[audio wav="http://itp.nicolaspe.com/wp-content/uploads/2018/02/alg_03_midi3.wav"][/audio]


<br>

## Sequencing
Now, I needed to start experimenting with sequences. I created randomly a 8 long sequence for the notes and a 5 long sequence for the durations. For the instruments, I kept the same last drum line and started with the oscillator to create a harmonic layer. The oscillator goes over the notes sequence making three note chords, while following the duration sequence.

[audio wav="http://itp.nicolaspe.com/wp-content/uploads/2018/02/alg_03_seq1.wav"][/audio]


Finally, the plucked instrument was added again, going over the same sequence of notes of the chords, but one at the time. Also, the duration or interval of each note is 1/4th of the oscillator, but follows the exact same sequence of speeds.

[audio wav="http://itp.nicolaspe.com/wp-content/uploads/2018/02/alg_seq2.wav"][/audio]
