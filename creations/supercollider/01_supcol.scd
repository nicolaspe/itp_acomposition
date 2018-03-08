// this is a comment

// first sound!
(
var f = 432;
{
	// stuff in here is the audio chain
	SinOsc.ar(f, 0, 0.5);
}.play;
)


// play more than one thing!
(
var f1 = 1000;
var f2 = 1200;

{
	SinOsc.ar(f1, 0, 0.5);
}.play;
{
	SinOsc.ar(f2, 0, 0.5);
}.play;

)


// first-class functions!
(
{
	// SinOsc wants a freq, a phase, an amp, an offset
	// XLine wants a start, an end, a time
	// so we're embedding the XLine as the freq and amp
	var swoop = XLine.kr(4000, 100, 1.4);
	var fade = Line.kr(0.01, 0.8, 0.5);

	SinOsc.ar(swoop, 0, fade);
}.play;

{
	// another example
	var woah = SinOsc.kr(1, 0, 100, 200);
	SinOsc.ar(woah, 0, 0.8);
}
)


// FREQUENCY MODULATION!
(
{
	var slide = XLine.ar(1, 2000, 5);
	var woah = SinOsc.ar(slide, 0, 500, 500);
	SinOsc.ar(woah, 0, 0.8);
}.play;)
