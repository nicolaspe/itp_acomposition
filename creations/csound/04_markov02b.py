# Markov Chain COMPOSITION
# Algorithmic Composition - ITP - Spring 2018
# by nicolás escarpentier

import numpy as np
import random as rng

# MIDI to frequency function
def mtof(m):
	f = 440. * np.exp(.057762265 * (m - 69.))
	return f

# MARKOV CHAIN function
def markov(arr):
	thechain = {}
	for ind in range(len(arr)):
		n = arr[ind]
		if n not in list(thechain.keys()):
			thechain[n] = []
		thechain[n].append(arr[ (ind+1)%len(arr) ])
	return thechain



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
orig_notes = [76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71, 71, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71]
orig_speed = [0.5, 0.5, 0.5, 0.5, 0.5, 1., 1., 1., 0.5, 1., 0.5, 0.5, 0.5, 1., 1., 1., 1., 1., 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

n_chain = markov(orig_notes)
s_chain = markov(orig_speed)

# starting point of the chain
note = rng.choice(orig_notes)
sped = rng.choice(orig_speed)

# == CREATE SCORE
# select instrument: pluck
instr = 3
# time loop
i = 0.0
while i < total_dur:
    # parameters of time
	start= i
	dur  = sped *interval
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
	note = rng.choice( n_chain[note] )
	sped = rng.choice( s_chain[sped] )



# == END ==
score_file.append("e")



# == WRITE FILE ==
filename = "04_markov02b.sco"
# clear the file
open(filename,"w").close()
# write the lines
sco = open(filename,"w")
sco.writelines(score_file)
sco.close()
