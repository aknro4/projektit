<!DOCTYPE html>
<html lang="fi">
<head>
<title>JC Airlines</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="jc_airlines.css">
<style>

.column {
	float: left;
	width: 33.33%;
	text-align:center;
	font-family: "Monaco", monospace;
	font-weight:;
	font-size:25px;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	position: relative;
	
	padding-top: 50px;
	padding-right: 30px;
	padding-bottom: 50px;
	padding-left: 30px;
}

@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}


h2 {
	color:skyblue;
}

</style>
</head>
<body>

<div class="header">
  <h1>JC Airlines</h1>
  <p>The <b>BEST</b> thing that happens in the air.</p>
</div>

<div class="navbar">
  <a href="verkkosivu.php">Koti</a>
  <a href = "tietoaMeista.php">Tietoa meistä</a>
  <a href ="varaaLento.php">Varaa lento</a>
</div>

<div class="row">
  <div class="main">
    <h2 style="text-align:center;">Lista JC Airlines lentokoneista</h2>
    <h5></h5>
    <div style="height:300px;"> 
		<div class="column" style=" background-image: url('q400.jpg');"> Bombardier Q400 <br><br> Koneeseen mahtuu 78 matkustajaa. <br> Koneita löytyy 12KPL <br></div>
		<div class="column" style=" background-image: url('AirBusA220-300.jpg');">AirBus A220-300<br><br> Koneeseen mahtuu 135 matjustajaa. <br> Koneita löytyy 20KPL <br></div>
		<div class="column" style=" background-image: url('AirBusA220-100.jpg');"> AirBusA220-100<br><br> Koneeseen mahtuu 110 matkustajaa. <br> Koneita löytyy 2KPL <br></div>
	</div>
	<br>
    <h2 style="text-align:center;">Hiukan tietoa meistä</h2>
    <div style="height:300px;">  
		<div class="column" style="color:white;"> <h2>JC-Airline </h2><br>JC-Airline lentoyhtiö on perustettu 2015 ja kuljetamme matkustajaliikkennettä Pohjoismaitten vilkkaimille kentille.<br><br>
		Meidän lennot lähteävät Tikkakosen lentokentältä ja tarjoamme lentoja: Suomeen, Ruotsiin, Norjaan, Tanksaan ja Islantiin. </div>
		<div class="column"style="color:white;"><h2>Historia</h2><br> Yhtiön ensimmäinen lento lennettiin Tikkakoskelta - Kööpenhaminaan 1.5.2015 vuokratulta ATR-72 Lentokoneella.<br><br>
		Tammikuussa 2016 yhtiö osti ensimmäisen omat ATR-72 lentokoneet. <br><br>
		Tämän jälkeen yhtio on hankkinut useita omia uudempia koneita vuosittain sitä mukaan kun asiakasmäärät ovat kasvaneet.‍<br><br>
		Yhtiön kannattava liiketoiminta on kasvanut nopeasti. Se on saavutettu maailman nuorimpien ja polttoainetehokkaimpien lentokoneiden asnioista.<br><br>
		Lisäksi korkean asiakastyytyväisyyden vuoksi meille "virtaa" uusia asiakkaita jatkuvasti. </div>
		<div class="column"style="color:white;"><h2> Palkinnot</h2><br>Olemme voittaneet seuraavat palkinnot:<br><br>Grand Travel Award: Euroopan paras lentoyhtiö 2019<br><br>ServiceScore: Korkeimman palvelun lentoythiö vuodet 2018,2019</div>
	</div>
  </div>
</div>

<div class="footer">
  <p style="font-size:10px;">Copyright © 2020 My Company. All rights reserved.</p>
</div>

</body>
</html>