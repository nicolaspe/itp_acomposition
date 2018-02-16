# Markov Chain COMPOSITION
# Algorithmic Composition - ITP - Spring 2018
# by nicolás escarpentier

import numpy as np
import random as rng

# MIDI to frequency function
def mtof(m):
	f = 440. * np.exp(.057762265 * (m - 69.))
	return f



#	SCORE FILE BREAKDOWN !!!
# 	-- first 3 parameters are ALWAYS the same! --
#	p1 = # instrument
#	p2 = start point
#	p3 = duration

total_dur = 15.0
interval  = 0.20	# 300 bpm sampling

score_file = []
score_file.append("; MARKOVIAN COMPOSITION by nicolas escarpentier")
score_file.append("\n")
score_file.append("\n")



# == F TABLE & HARMONICS ==
# create 1 - 6 harmonics
h = []						# harmonics list
h.append(rng.random()*0.2 + 0.9)	# range: 0.8 - 1.0
h_count = rng.randrange(1, 8)
for i in range(h_count):
	h.append(rng.random())	# range: 0.0 - 1.0

# create string for score file
harmonic_log = "f 1 0 16384 10"
for h_val in h:
	harmonic_log += " " + str(h_val)
score_file.append(harmonic_log + "\n")



# == MARKOV CHAIN - hard coded
chain = {}
chain[72] = []
chain[72].append(60)
chain[72].append(64)
# it's the same as: chain[72] = [60, 64]
chain[60] = []
chain[60].append(72)
chain[64] = []
chain[64].append(60)
chain[64].append(67)
chain[67] = []
chain[67].append(67)
chain[67].append(72)

# starting point of the chain
note = rng.choice([60, 64, 67, 72])

# speeds for randomizing durations
speeds = [0.5, 1.0, 1.5, 2.5, 1.0]



# == CREATE SCORE
# select instrument: oscillator
instr = 2
# time loop
i = 0.0
while i < total_dur:
    # parameters of time
	start= i
	dur  = rng.choice(speeds) *interval
	# parameters of sound
	freq = mtof( note )
	amp  = rng.random()*2000 + 4000
	pan  = 0.5
	# write line
	note_list = ["i", instr, start, dur*2, freq, amp, pan, "\n"]
	note_str = " ".join(str(item) for item in note_list)
	score_file.append(note_str)
	# skip ahead
	i += dur
	note = rng.choice( chain[note] )


# select instrument: pluck
instr = 3
# time loop
i = 0.0
while i < total_dur:
    # parameters of time
	start= i
	dur  = rng.choice(speeds) *interval
	# parameters of sound
	freq = mtof( note )
	amp  = rng.random()*2000 + 4000
	pan  = 0.5
	# write line
	note_list = ["i", instr, start, dur, freq, amp, pan, "\n"]
	note_str = " ".join(str(item) for item in note_list)
	score_file.append(note_str)
	# skip ahead
	i += dur
	note = rng.choice( chain[note] )


# == END ==
score_file.append("e")



# == WRITE FILE ==
filename = "04_markov02.sco"
# clear the file
open(filename,"w").close()
# write the lines
sco = open(filename,"w")
sco.writelines(score_file)
sco.close()
