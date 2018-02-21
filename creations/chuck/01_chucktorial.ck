// this is a comment
/* this ALSO is a comment */

<<< "print like it's C++!" >>>;

// timing with the `dur` datatype
120::ms => dur beat;
4::beat => dur measure;


SinOsc thesine => dac; // "chuck" thesine to the speaker
thesine.gain(0.2);     // set the amplitude
thesine.freq(220);     // set the frequency

1::measure => now;


thesine.gain(0.3);     // set the amplitude
thesine.freq(432);     // set the frequency

1::measure => now;

// add "packages" called Std, yeah, seriously 
Std.rand2f(100, 500) => thesine.freq;

1::measure => now;


// loop as you always have
while(true){
  Std.rand2f(100, 600) => thesine.freq;
  1::beat => now;
}
