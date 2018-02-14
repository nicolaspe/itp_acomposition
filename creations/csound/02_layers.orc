sr = 44100 ;  audio sampling rate
kr = 4410 ;   refresh rate of 'scheduler'
ksmps = 10 ;  # samples in a control period

nchnls = 2 ;  # of channels

instr 1   ; instrument #1 - oscillator
  ifn = 1 ; waveform

  /* amplitude modifier: input amplitude, attack, duration, decay */
  kmaxamp = 0.6
  aline linen kmaxamp, 0.3, p3, 0.7
  a1 oscil p5*aline, p4, ifn
  a2 oscil p5*aline, p4, ifn

  out a1*(1.0 -p6), a2*p6
endin

instr 2   ; instrument #2 - base
  a3 soundin "drums.aiff", p4
  out a3*0.2, a3*0.2
endin
