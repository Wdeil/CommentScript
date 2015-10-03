/*
Submit by Dreamacro
Using for displacement
You should repalce the text value by your own text. 
*/
var text = 'text';

var A = 'A'.charCodeAt();

for(var k = 1; k < 26; k++) {
	var re = text.split('').map(function(item) {
		if(item == ' ') return item;
		var code = item.charCodeAt();
		return String.fromCharCode(A + (code - A + k) % 26);
	}).join('');
	
	console.log(re);
}
