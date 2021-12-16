<!DOCTYPE html>
<html lang = "fi">
<meta charset="UTF-8">
<head>
<!-- jquery -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<!-- JavaScript -->
<script type="text/javascript">
//Paluu "etusivulle"
function myF () {
	location.replace("verkkosivu.php")
	
}
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

<!-- Responsive -->
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
//Tietokanta

	$palvelin= "localhost";  
	$kayttajanimi= "root";  
	$salasana= "";  
	$tietokanta= "lennot"; 
	$portti="3306"; 

//Luodaan yhteys tietokantaan  

	$conn = mysqli_connect($palvelin, $kayttajanimi, $salasana, $tietokanta, $portti);  

//Tsekataan onnistuuko yhteys 

	if (!$conn) {  
		die("Yhteys ei onnistunut " . mysqli_connect_error());  
	}  

	//Ostajan tiedot
	$firsNameG = $_GET['firstName'];
	$surNameG = $_GET['surName'];
	$puhNG = $_GET['puhN'];
	$addressG = $_GET['address'];
	
	//Sähköposti
	//Annetaan tiedot kaikille tiedostoille käytettäväksi
	$emailG = $_GET['email'];
	setcookie("emailG",$emailG, time() + (1000), "/");
	
	//Näytetään tilauksen tiedot. Lennon ID.
	$idL = $_GET["town"];
	//Annetaan tiedot kaikille tiedostoille käytettäväksi
	setcookie("LentoID",$idL, time() + (1000), "/");

	//Lisätään lennon ID matkustajat taulukkoon jolla voidaan vähentää lippujen määrää.
	$conn->query("UPDATE matkustajat SET LentoID = $idL");

	//Haetaan lennon tiedot ID avulla. Ja tulostetaan ruudulle.
	$sql3 = "SELECT LentoID ,Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE LentoID = '$idL'";
	$result3 = $conn->query($sql3);
	
	
	//Viellä kertaalleen näytetään varauksen tiedot.
	echo " <p>Varauksen tiedot</p>" . "Etunimi " . $firsNameG  . "</br>" . "Sukunimi: " . $surNameG . "</br>" . "Matukstajat: " . $_COOKIE['passengers'] . "</br>" . "</br>" . "Puh numero: " . $puhNG . "</br>" . "Osoite: " .
	$addressG . "</br>" . "Email: " . $emailG . "</br>" . "</br>" . "Lennon tiedot ". "</br>";

	//Tulostetaan tietokannasta tilauksen tiedot ruudulle.
		if ($result3->num_rows > 0) {
		while ($row2 = $result3->fetch_assoc()){
			echo "Kohdemaa: " . $row2['Kohdemaa'] . "</br>" . " Kaupunki: " . $row2['Kaupunki'] . "</br>" . " Aikataulu: " . $row2['Aika'] . "</br>" . " Lipun hinta KPL: " . $row2['LipunHinta'] . "€";		
		}
	}
	
	

	//Jos hyväksyy tilauksen lisätään tiedot tilaustiedot tietokantaan
if (isset($_GET['submit'])) {
	$conn -> close();
}
	

	if(isset($_GET['decline'])) {
		$conn -> close();
	}
	
?>
<!-- Käyttäjä input -->
<form method="get" action="tilausN2.php">

<p>Vahvistetaanko tilaus</p>
<!-- Siirtyy "Tilaus vahvistettu" sivulle -->
<input type="submit" name="submit" id="submit" class="button"  value="Vahvista">

<!-- Palaa "etusivulle" -->
<input type="button" name="decline" id="decline" class="button"  value="Peruuta" onClick="myF();">

</form>
</div>
</body>
</html>