<!DOCTYPE html>
<html lang="fi">
<head>
<title>JC Airlines</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="jc_airlines.css">
<style>

.imgWhitT {
	height:auto; 
	background-position:50% 50%; 
	background-image: url('view.jpeg'); 
	color:white; 
	text-align:left;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	position: relative;
	padding-top:15px;
	padding-bottom:15px;
	padding-left:15px;
	padding-right:15px;
}

h2 {
	text-align:center;
	font-family: "Monaco", monospace;
	font-weight:bold;
	font-size:25px;
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
  <a href="tietoaMeista.php">Tietoa meistä</a>
  <a href ="varaaLento.php">Varaa lento</a>
</div>

<div class="row">
  <div class="main">
    <h2 style="color:white;">VARAA LENTO</h2>
    <h3>Kaikki lennot lähtevät meidän kotikentältä Tikkakoskelta.</h3>
    <div class="imgWhitT"><?php include 'valitseKaupunki.php' ?></div>
    <br>
		<div style="height:400px;"></div>
  </div>
</div>

<div class="footer">
  <p style="font-size:10px;">Copyright © 2020 My Company. All rights reserved.</p>
</div>

</body>
</html>