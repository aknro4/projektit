<!DOCTYPE html>
<html lang = "fi">
<meta charset="UTF-8">
<head>
<style>


<!-- Tausta tälle tiedostolle. -->
.center {
	margin: auto;
	width: 60%;
	border: 3px solid skyblue;
	padding: 5px;
	text-align:center;
	background-image: -webkit-gradient(linear, left top, left bottom from(#211a47), to(#ce2528));
	background-image: linear-gradient(180deg,#211a47,#ce2528);
		
}
<!-- responsive -->
@media screen and (max-width: 600px) {
  .center {
    width: 100%;
  }
}


<!-- Nappulan tyyli -->
.button {
	font-family: "Monaco", monospace;
	font-size:15px;
	padding: 10px 10px;
	color:white;
	background: skyblue;
}

</style>
</head>
<body>

<?php
	//Tietokanta

	$palvelin= "localhost";  
	$kayttajanimi= "root";  
	$salasana= "";  
	$tietokanta= "lennot"; 
	$portti="3306"; 

//Luodaan yhteys tietokantaan  

	$conn = mysqli_connect($palvelin, $kayttajanimi, $salasana, $tietokanta, $portti);   	

//Tarkistetaan onnistuuko yhteys 

	if (!$conn) {  
		die("Yhteys ei onnistunut " . mysqli_connect_error());  
	} 
	
	//Positaa matkustaja määrän jos niitä tietokannassa on
	$deleteM = "DELETE FROM matkustajat";
		
		if ($conn->query($deleteM) === TRUE) {
			echo "";
		} else {
			echo "Error" . $conn->error;
		}

?>

<div class="center">

<form method="get" action="tilauksenValinta2.php">

<!-- Kohdemaa valinta -->
<p>Valitse kohde</p>
<select name="mihin" id="mihin">
    <optgroup label="Suomi">
      <option value="Helsinki">Helsinki</option>
      <option value="Oulu">Oulu</option>
	  <option value="Rovaniemi">Rovaniemi</option>
    </optgroup>
    <optgroup label="Ruotsi">
      <option value="Göteborg">Göteborg</option>
      <option value="Malmö">Malmö</option>
	  <option value="Arland">Arland</option>
    </optgroup>
	<optgroup label="Tanska">
      <option value="Kööpenhamina">Kööpenhamina</option>
      <option value="Billund">Billund</option>
    </optgroup>
	<optgroup label="Norja">
      <option value="Bergen">Bergen</option>
      <option value="Trondheim">Trondheim</option>
	  <option value="Oslo">Oslo</option>
    </optgroup>
	<optgroup label="Islanti">
      <option value="Keflaki">Keflaki</option>
    </optgroup>
	
  </select>
</select>

</br>
<!-- Lähöajan valinta -->
<p>Lähtöaika</p>
<select name="aika" id="aika">
	 <option id="Päivä" name="Päivä">Päivä</option>
     <option id="Ilta" name="Ilta">Ilta</option>
     <option id="Aamu" name="Aamu">Aamu</option>
</select>
</br>

<!-- Matustajamäärän syöttö, syötetään jotta voitaisiin näyttää lennon mihin vielä mathuu. -->

<p>Matkustajamäärä</p>
<input type="number" id="passengers" name="passengers" >
</br>

<!-- Lähdön haluttu päivämäärä -->

<p>Valitse lähtöpäivä</p>
<input type="date" name="pvm" id="pvm" >
</br>
</br>

<input type="submit" name="submit" class="button" value="VARAA">

</form>

</div>

</body>
</html>