# MIDI COMPOSITION
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
score_file.append("; MIDI COMPOSITION by nicolas escarpentier")
score_file.append("\n")
score_file.append("\n")


# == F TABLE & HARMONICS ==
# create 1 - 6 harmonics
h = []						# harmonics list
h.append(rng.random()*0.2 + 0.8)	# range: 0.8 - 1.0
h_count = rng.randrange(1, 5)
for i in range(h_count):
	h.append(rng.random())	# range: 0.0 - 1.0

# create string for score file
harmonic_log = "f 1 0 16384 10"
for h_val in h:
	harmonic_log += " " + str(h_val)
score_file.append(harmonic_log + "\n")



# == NOTES and SCALE
base = rng.randrange(48, 60, 1)
scale = [0, 2, 3, 5, 7, 8, 10, 0, 0, 0, 0, 3, 3, 3, 7, 7, 7, 10, 10]



# == BASE (instrument 1: drum samples) ==
instr = 1
for i in np.arange(0.0, total_dur, interval):
	# kick drum @ 150 bpm
	# if i%0.2 == 0.0:
	# parameters of time
	start= i
	dur  = 0.9
	# kick drum
	offset = 0
	#	chance of syncopation : 10%
	if rng.random() < 0.1:
		start += interval
	# write line
	note_list = ["i", instr, start, dur, offset, "\n"]
	note = " ".join(str(item) for item in note_list)
	score_file.append(note)

	# hi-hat rotation
	aux = rng.randrange(5)
	if   (aux == 0) or (aux == 1):	# closed hi-hat
		offset = 2
		# write line
		note_list = ["i", instr, start, dur, offset, "\n"]
		note = " ".join(str(item) for item in note_list)
		score_file.append(note)
	elif (aux == 2) :	# open hi-hat
		offset = 3
		# write line
		note_list = ["i", instr, start, dur, offset, "\n"]
		note = " ".join(str(item) for item in note_list)
		score_file.append(note)
	else:
		pass



# == AMBIENT (instrument #2: oscillator) ==
instr = 2
i = 0
while i < total_dur:
	# parameters of time
	start= i
	dur  = (interval+0.5) *(rng.randrange(3)+1)
	# parameters of sound
	freq = mtof( base-12 + rng.choice(scale) )
	amp  = rng.random()*2000 + 8000
	pan  = 0.5
	# write line
	note_list = ["i", instr, start, dur, freq, amp, pan, "\n"]
	note = " ".join(str(item) for item in note_list)
	score_file.append(note)
	# skip ahead
	i += dur *rng.randrange(2) *0.5



# == LEAD (instrument #3: pluck) ==
instr = 3
for i in np.arange(0.0, total_dur, interval):
	# parameters of time
	start= i
	dur  = rng.random()*0.5 +0.5
	# parameters of sound
	freq = mtof( base + rng.choice(scale) )
	amp  = rng.random()*3000 + 2000
	pan  = 0.5
	# write line
	note_list = ["i", instr, start, dur, freq, amp, pan, "\n"]
	note = " ".join(str(item) for item in note_list)
	score_file.append(note)



# == END ==
score_file.append("e")


# == WRITE FILE ==
filename = "03_midi004.sco"
# clear the file
open(filename,"w").close()
# write the lines
sco = open(filename,"w")
sco.writelines(score_file)
sco.close()
