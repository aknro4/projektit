<!DOCTYPE html>
<html lang="fi">
<head>
<title>JC Airlines</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="jc_airlines.css">
<style>

.imgWhitT {
	height:50%; 
	background-position:50% 50%; 
	background-image: url('view.jpeg'); 
	color:white; 
	text-align:left;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	position: relative;
	
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


<div class="row">
  <div class="main">
    <div class="imgWhitT"><?php include 'tilausN.php' ?></div>
	<div style="height:550px;"></div>
    <br>
  </div>
</div>

<div class="footer">
  <p style="font-size:10px;">Copyright © 2020 My Company. All rights reserved.</p>
</div>

</body>
</html>