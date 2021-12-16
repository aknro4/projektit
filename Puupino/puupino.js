var alue = [];
var circleTotal = [];
var circleTotalSum = [];
var cubeTotal = [];
var cubeTotalSum = [];
var cubeCircleArea = [];

//alueen Pituus ja Korkeus arvojen syöttö ja lasku
function laheta() {
	var lenght = document.getElementById("pituus").value;
	var height = document.getElementById("korkeus").value;
	
//Tarkistaa onko arvot enemmän kuin 0
	if (height <= 0 || lenght <= 0) {
		document.getElementById("results").innerHTML = "Vaara arvo"; 
	} else {
		var pintaala = lenght * height;
		rounded = pintaala.toFixed(3);
		roundedA = parseFloat(rounded);
		alue.push(roundedA);
// Laittaa laskun/loopin käyntiin jos arvot ovat "oikeat"
		looping();
	}
}

//Kiertää koodia niin kauan kunnes alue on täytetty puilla.
function looping () {

	for (i = 0; i < alue; count++) {
		
	var count =0;
	
//Arvotaan puun halkaisijan arvo. (CM)
	var puuA = Math.floor(Math.random()*41)+10;
	
//Lasketaan puun pinta-ala (CM)
	d = puuA / 100;
	a = d / 2;
	b = 2 * a * Math.PI;
	c = b * (d/4);
	
//Ympyran pinta-ala	pyöristettynä
	round = c.toFixed(3);
	roundN = parseFloat(round);
	circleTotal.push(roundN);

//Laskee ympyrän pinta-ala arvot yhteen 
	circleTotalSum.push(circleTotal.reduce((a, b) => a + b ,0));
	circlePop = circleTotalSum.pop();
	
//Neljon pinta-ala lasku
	var cubeA = d * d;
	cubeR = cubeA.toFixed(3);
	cubeRF = parseFloat(cubeR);
	cubeTotal.push(cubeRF);
	
//Laskee Neljon pinta-ala arvot yhteen
	cubeTotalSum.push(cubeTotal.reduce((a, b) => a + b ,0));
	cubePop = cubeTotalSum.pop();
	
//Pyöristää arvon tarkempaa vertailua varten.
	cubePopR = cubePop.toFixed(0);
	cubePopRF = parseFloat(cubePopR);

//Asettaa i arvoksi yhteen lasketun neljön pinta-alan summan
	i = cubePopRF;

	for (var j = 0; j < alue; j++) {
		count++;
		}	
	}
	
// Laskee puuaineksen laskennallinen prosenttiosuus
	var total = circlePop / cubePop;
	var prosentti = total * 100;
	totalR = prosentti.toFixed(0);
	totalRF = parseFloat(totalR);
	cubeCircleArea.push(totalRF);
	
//Laskee kuutio metrit
	var lenght1 = document.getElementById("pituus").value;
	
	var total1 = cubePop - circlePop;
	totalR1 = total1.toFixed(1);
	totalRF1 = parseFloat(totalR1);
	
	//Kuinka monta puuta aluella on
	puita = circleTotal.length;
	
	document.getElementById("results").innerHTML = cubeCircleArea + " % " + "<br/>" + totalRF1;
}