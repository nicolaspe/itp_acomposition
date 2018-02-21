// this is a comment
/* this ALSO is a comment */

<<< "print like it's C++!" >>>;

// timing with the `dur` datatype
60::ms => dur beat;
4::beat => dur measure;


SawOsc thesaw => LPF thefilter => dac;
thesaw.gain(0.5);
thesaw.freq(220);
thefilter.freq(800); // cutoff freq
thefilter.Q(745.7);    // cutoff freq skew 

1::measure => now;


// loop and condition as you always have
0 => int currentBeat;

while(true){
    if(currentBeat==0){
        Std.rand2f(100, 600) => thesaw.freq;
    }
    
    Std.rand2f(200, 800) => thefilter.freq;
    1::beat => now;
    
    (currentBeat+1)%4 => currentBeat;
}
