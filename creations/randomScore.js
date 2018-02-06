let freq, amp;
let dur, pan;

console.log("f 1 0 16384 10 1 0.8 0.7 0.5 0.3");

for(var i=0; i<1000; i++){
	dur = 1 + Math.random()*0.5;
	pan = Math.random();
	freq= Math.random()*1000 + 100;
	amp = Math.random()*500 + 500;

	console.log("i 1 "+ i*0.1+" "+ dur+" "+ freq+" "+ amp+" "+ pan);
}

console.log("e");
