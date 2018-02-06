sr = 44100 ;  audio sampling rate
kr = 4410 ;   refresh rate of 'scheduler'
ksmps = 10 ;  # samples in a control period

nchnls = 2 ;  # of channels

instr 1
  ifn = 1 ; waveform

  /* amplitude modifier: attack,  */
  aline linen 0.7, 0.2, p3, 0.4
  a1 oscil p5*aline, p4, ifn
  a2 oscil p5*aline, p4, ifn

  out a1*(1.0 -p6), a2*p6
endin
