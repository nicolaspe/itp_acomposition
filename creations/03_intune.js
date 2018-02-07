// parameters
let start, dur;			// both
let freq, amp, pan;	// oscillator
let offset;					// base

let total_dur = 15.0;
let interval 	= 0.10;


// == F TABLE & HARMONICS ==
console.log("f 1 0 16384 10 1 0.8 0.7 0.5 0.3");


// == BASE (instrument #2) ==
dur = 0.9;
for(let i = 0; i < total_dur; i += interval){
	start = i;

	// Hi-hat rotation
	let aux = Math.floor(Math.random()*3);
	switch (aux) {
		case 0:		// do nothing
			break;
		case 1:		// closed hi-hat
			offset = 2;
			console.log("i 2 "+ start +" "+ dur +" "+ offset);
			break;
		case 2:		// open hi-hat
			offset = 3;
			console.log("i 2 "+ start +" "+ dur +" "+ offset);
			break;
	}

	// 10% snare chance
	if(Math.random()*100 < 10){
		offset = 1;
		console.log("i 2 "+ start +" "+ dur +" "+ offset);
	}
}


// == OSCILLATOR ==
let base = Math.random()*530 +120;	// base (120 , 650)

// "scale" creation
let scale = [];
scale[0] = 1;
scale[1] = scale[0] *(Math.random()*1.2 +1.2);
scale[2] = scale[1] *(Math.random()*1.2 +1.2);
scale[3] = scale[2] *(Math.random()*1.2 +1.2);
scale[4] = scale[3] *(Math.random()*1.2 +1.2);

// comments with data
console.log("; base: " +base);
console.log("; scale: " +scale[0] +", " +scale[1] +", " +scale[2] +", " +scale[3] +", " +scale[4]);

// sound loop
for(var i=0; i<500; i++){
	// oscillator parameters
	dur = 0.6 +Math.random()*0.6;		// dur = (0.6, 1.2)
	pan = 0.2 +Math.random()*0.4;		// pan = (0.2, 0.6)
	amp = 1000 +Math.random()*500;	// amp = (1000, 1500)
	freq= base *scale[ Math.floor(Math.random()*5) ];

	// normally distributed random > 5 dies
	start = 0.0;
	for (let j = 0; j < 5; j++) {
		start += Math.random() * total_dur;
	}
	start = start / 5.0;

	// print msg
	console.log("i 1 "+ start +" "+ dur +" "+ freq +" "+ amp +" "+ pan);
}


// END
console.log("e");
