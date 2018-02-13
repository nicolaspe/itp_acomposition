sr = 44100 ;  audio sampling rate
kr = 4410  ;  refresh rate of 'scheduler'
ksmps = 10 ;  # samples in a control period

nchnls = 2 ;  # of channels

instr 1   ; instrument #1 - base
  a1 soundin "drums.aiff", p4
  out a1*0.2, a1*0.2
endin

instr 2   ; instrument #2 - oscillator
  ifn = 1 ; waveform

  /* amplitude modifier: input amplitude, attack, duration, decay */
  kmaxamp = 0.6
  aline linen kmaxamp, 0.3, p3, 0.7
  a2 oscil p5*aline, p4, ifn

  out a2*(1.0 -p6), a2*p6
endin

instr 3   ; instrument #3 - plucking
  ifn = 1 ; waveform
  kmaxamp = 0.6
  a3 pluck p5, p4, p4, ifn, 1

  out a3*(1.0 -p6), a3*p6
endin
