<!DOCTYPE html>
<html lang="fi">
<head>
<title>JC Airlines</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="jc_airlines.css">
<style>

.imgWhitT {
	height:250px; 
	background-position:50% 50%; 
	background-image: url('view.jpeg'); 
	color:white; 
	text-align:center;
	font-size: 30px;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	position: relative;
	color: white;
}

.column {
	float: left;
	width: 33.33%;
	text-align:center;
	font-family: "Monaco", monospace;
	font-weight:bold;
	font-size:25px;
}

@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}

h2 {
	text-align:center;
	font-family: "Monaco", monospace;
	font-weight:bold;
	font-size:25px;
}

p {
	text-align:center;
	font-family: "Monaco", monospace;
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
    <h2> </h2>
    <div class="imgWhitT">
	<div class="column"> <br>Palvelu </div>
	<div class="column"> <br>Rohkeus </div>
	<div class="column"> <br>Välittäminen </div>
	</div>
    <br>
	<h2> Tarjoamme</h2>
	<p> Turvallisen matkan ja ystävällisen palvelun järkevään hintaan</p>
	<p> Lentojen varaus 24/7 verkosta.</p>
	<div style="height:450px;"></div>
  </div>
</div>

<div class="footer">
  <p style="font-size:10px;">Copyright © 2020 My Company. All rights reserved.</p>
</div>

</body>
</html>