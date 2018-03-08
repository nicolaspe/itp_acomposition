// analog bubbles
(
{
	var s = LFSaw.kr([8, 7.23], 0, 3, 80);
	// sawtooth of midi values
	var f = LFSaw.kr(0.4, 0, 24, s).midicps;
	var o = SinOsc.ar(f, 0, 0.04);
	// Comb filter: (cheap) echo with high feedback
	CombN.ar(o, 0.2, 0.2, 4);
}.play; )