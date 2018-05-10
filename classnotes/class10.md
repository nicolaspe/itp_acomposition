# Algorithmic Composition - Apr 06

## soundfonts

General MIDI : how to standarize sounds
a general midi synth hsould be able to do:
128 sounds spread across 16 channels with 32-note polyphony


Yamaha DX7: most popular digital synth
First fully functional MIDI keyboard


classic synth
- additive synthesis: you add a ton of sine waves
ex: [Xenakis](https://www.youtube.com/watch?v=Q8suVSzQmwA)
- subtractive synthesis: you have a very rich base sound and you filter it to create a rich tone
ex: [Van Halen Jump synth](https://www.youtube.com/watch?v=SwYN7mTi6HM)
- frequency modulation synthesis:!
ex: [Depeche Mode Everything Counts](https://www.youtube.com/watch?v=1t-gK-9EIq4) all DX7!

What do you hear in FM?
if
    f_c = frequency of the carrier
    f_m = frequency of the modulator

you hear:
    f_c + f_m
    f_c - f_m
    f_c + 2*f_m
    f_c - 2*f_m
    ...
    f_c + n*f_m
    f_c - n*f_m

index of modulation: the modifier f the amplitude of the modulator is a function of the base frequency. On an FM Synth you typically vary this number!

Bessel functions: cancellation of sine waves when you increment the index of modulation. It is what happens in brass instruments!

Four stage volume control for instruments:
- A: attack
- D: decay
- S: sustain
- R: release


Fairlight CMI: let you record your voice for later playback
ex: [Kate Bush, Running Up That Hill](https://www.youtube.com/watch?v=wp43OdtAAkM) all her backing vocals was her pre recorded. Same for some played back guitars
