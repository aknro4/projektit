<!DOCTYPE html>
<html lang = "fi">
<meta charset="UTF-8">
<head>
<!-- jquery -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<!-- JavaScript -->
<script type="text/javascript">

//Jos haluaa peruttaa tilauksen.
function myF () {
	location.replace("verkkosivu.php")
}

//disables submit button jos email arvo on tyhjä..  toimii vain kerran
$(document).ready(function() {
     $(':input[type="submit"]').prop('disabled', true);
     $('#email').keyup(function() {
        if($(this).val() != '') {
           $(':input[type="submit"]').prop('disabled', false);
        }
     });
 });
</script>
<!-- css tyyli tiedosto -->
<link rel="stylesheet" href="jc_airlines.css">

<style>

<!-- Tausta tälle tiedostolle. -->
.center {
  margin: auto;
  width: 60%;
  border: 3px solid skyblue;
  padding: 10px;
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

</style>

</head>
<body>

<div class="center">
<?php

if (isset($_GET['submit'])) {
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

	//Käyttäjän valitsema kohdemaa ja lähtöaika
	$where = $_GET["mihin"];
	$time = $_GET["aika"];
	
	//Päivämäärä
	$date = $_GET["pvm"];
	setcookie("date",$date, time() + (1000), "/");
	
	//Matkustaja määrä ja syötetään tieto taulukkoon.
	$amount = $_GET["passengers"];
	setcookie("passengers",$amount, time()+ (1000),"/");
	$conn->query("INSERT INTO matkustajat(maara)VALUES ('$amount')");
	
	//Haetaan valitun maan ja ajan perusteella
	$sql = "SELECT LentoID, Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE Kaupunki = '$where' AND Aika = '$time' AND VapaatPaikat >= '$amount'";
	$result = $conn->query($sql); 

	
	//Tulostetaan
if ($result->num_rows > 0) {
		echo "</br>";
		
		//Tehdään form taulukko
		echo "<form method='get' action='tilauksenV2.php'> 
				<p style='color:white';>Valitse lippu</p> 
					<select name='town' id='town'>";
		
		//Tulostetaan saadut vaihtoehdot
		while($row = $result->fetch_assoc()) {
			echo "<option name='' id='' value=". $row['LentoID']. ">"  . " Lähtöpäivä " . $date . " Lipun hinta/KPL " . $row['LipunHinta'] . "€" .  "</option>";
		}
			echo  "</select>";
	} else {
			// Jos ei tuloksia löydy, tulostaa annetun maan ja ajan. Ja kertoo että tuloksia ei löytynyt -> tee järkevämpi
			echo "Ei tuloksia, Input: ";
			echo $where;
			echo " ";
			echo $time;
	}
	$conn -> close();
}

	//Jos haluaa perua tilauksen.
	if(isset($_GET['cancel'])) {
		$conn -> close();
	}


?>

<!-- Käyttäjän input -->
<form method="get" action="tilauksenV2.php">

<!-- Käyttäjä syöttää omat tiedot -->
<p style='color:white';>Anna sinun yhteystiedot</p>
	<input type="text" name="firstName" id="firstName" placeholder="Etunimi"  required> <br>
	<input type="text" name="surName" id="surName" placeholder="Sukunimi" required> <br>
	<input type="number" name="puhN" id="puhN"  placeholder="Puh numero"required> <br>
	<input type="text" name="address" id="address"  placeholder="Osoite"required> <br>
	<input type="email" name="email" id="email" placeholder="Email" required> 
	</br>
	<br>

	<input type="submit" name="submit" id="submit"  value="Varaa" disabled="disabled">
<!-- Jos käyttäjä haluaa peruttaa tilauksen. Palaa "etusivulle" -->
	<input type="button" name="cancel" id="cancel"  value="Peruuta" onClick="myF();">

</form>
</div>
</body>
</html>