sr = 44100 ;  audio sampling rate
kr = 4410  ;  refresh rate of 'scheduler'
ksmps = 10 ;  # samples in a control period

nchnls = 2 ;  # of channels

instr 1    ; instrument #1 - base
    ; p4 = offset
    a1 soundin "drums.aiff", p4
    out a1*0.15, a1*0.15
endin

instr 2   ; instrument #2 - oscillator
    ; p3 = duration
    ; p4 = frequency
    ; p5 = amplitude (max)
    ; p6 = pan

    ifn = 1 ; waveform
    ; amplitude envelope: amplitude, attack, duration, decay
    k2 linen 0.9, 0.05, p3, 0.65
    a2 oscil p5*k2, p4, ifn
    out a2*(1.0 -p6), a2*p6
    ; out a2, a2

endin

instr 3   ; instrument #3 - plucking
    ; p3 = duration
    ; p4 = frequency
    ; p5 = amplitude (max)
    ; p6 = pan
    ifn = 1 ; waveform
    kmaxamp = 0.6
    a3 pluck p5*kmaxamp, p4, p4, ifn, 1

    out a3*(1.0 -p6), a3*p6
endin
