# Asteroid sonification
Sonification of a data set of discovered asteroids and comets that transit near Earth. Project done in collaboration with [Camilla Padgitt-Coles](http://www.ivymeadows.net/) and [Katya Rozanova](http://www.katyarozanova.com/).


## Failed experiments (for now)
Our first attempt was to use The Beatle's song Norwegian Wood to make a sentiment analysis of the comments on one of ots [YouTube videos](https://www.youtube.com/watch?v=SiJiuhnDfck). We extracted the MIDI data with the help of the [Tone.js MidiConvert library](https://github.com/Tonejs/MidiConvert), created a Markov chain to alter the lead flute sound while playing the original rhythmic guitar with instruments created in Csound. For the sentiment analysis we were going to use [NLTK (Natural Language ToolKit)](http://www.nltk.org/), a Python library that returns the level of positive or negative sentiment. This data would've been mapped to create different chords to play on top of the song, but this ultimately proved kind of difficult to learn as fast as we needed.

Bellow is the result of the markovian Norwegian Wood



## Earth's near deaths
*by Camilla*

We took a new approach. While we may tackle sentiment analysis later on either together or in our own projects, we decided to use another data set and start from scratch for the second part of our project together. We searched for free data sets and came across a list of asteroids and comets that flew close to earth [here](https://data.nasa.gov/resource/2vr3-k9wn.json) ([source of dataset repository](https://github.com/jdorfman/awesome-json-datasets#github-api)).

We also experimented with layering the result over NASA's "Earth Song" as a way to sonify both the comets and asteroids (algorithmically, through Csound) and Earth (which they were flying over).  The result was cosmic to say the least (pun intended!)

Here are the two versions below.



## Python script
For each asteroid or comet on the file, we extracted some common characteristics to set the sound parameters. The most important aspect is to portray how often they pass near the Earth, so the representation of the time has to be accurate. We set an equivalence of one month = 5 seconds and a year multiplier of 12 months, in case we wanted to make a longer year to introduce longer periods of silence on the score. The audio file starts on Jan 1, 2010 - the earliest year from the acquired data set. Each rock's discovery date sets its first occurrence on the score, and each occurrence repeats itself according to its `period_yr` (except for the 'Parabolic Comet', which doesn't have a return period).

```python
month_interval = 5. # in sec
year_mult = 12 # multiplier (how many months in a year)

for a in aster_data:
    # get raw data
		datetime = dateparser.parse(a['discovery_date'])
		yea = datetime.year       # starting time
		mon = datetime.month      # starting time
		day = datetime.day        # starting time

		# first occurrence (starting in 2010)
		start = ((yea-2010)*year_mult + mon + day/30.) * month_interval

		# recursion
		start += recur *year_mult
```

For the other parameters, we selected characteristics that gave us some expressive possibilities. The pitch of each rock is based on the orbit's angle (`i_deg`), the instruments are based on the `orbit_class`, the duration on the `q_au_1` (which we have no idea what it actually represents). For the scale of this score, we chose a minor B flat, in reference to [the sound of a black hole and the "lowest note in the universe"](http://www.nytimes.com/2003/09/16/science/music-of-the-heavens-turns-out-to-sound-a-lot-like-a-b-flat.html).


## Instruments in csound
*by Katya*

The first three corresponded to the three most common occurring meteors and asteroids. These are subtle `pluck` sounds. A pluck in CSound produces naturally decaying plucked string sounds.

The last six instruments consisted of louder, higher frequency styles.
- Instrument four is a simple oscillator.
- Instrument five, six, and eight are VCO, analog modeled oscillators, with a sawtooth frequency waveform.
- Instrument seven is a VCO with a square frequency waveform.
- Instrument nine is a VCO with a triangle frequency waveform.

`linseg` is an attribute we used to add some vibrato to instruments 6 - 9. It traces a series of line segments between specified points. These units generate control or audio signals whose values can pass through 2 or more specified points.
