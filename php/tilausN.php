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
	width: 30%;
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
	//Tyhjentää matkustajat taulukon
	
	$conn->query ("UPDATE lennot  SET VapaatPaikat = VapaatPaikat - (SELECT (maara) FROM matkustajat WHERE LentoID = '".$_COOKIE['LentoID'] ."') WHERE LentoID = '".$_COOKIE['LentoID'] ."'");
	
	$sql3 = "SELECT LentoID ,Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE LentoID = '".$_COOKIE['LentoID'] ."'";
	$result3 = $conn->query($sql3);	
	
	//Lisää tiedot tilaustiedot tietokantaan
	if ($result3->num_rows > 0) {
		while($row3 = $result3->fetch_assoc()) {
		//tallennetaan arvot tietokantaan
		$inserting = "INSERT INTO tilaustiedot (Aika,PVM,Kaupunki,Email, LennonID) VALUES ('". $row3['Aika'] . "' ,'" . $_COOKIE['date'] . "' ,'" . $row3['Kaupunki'] . "','".$_COOKIE['emailG']. "', '". $row3['LentoID'] ."')";
			//Tarkistaa onnistuiko lisäys
			if ($conn->query($inserting)=== TRUE) {
				echo "";
			} else {
				echo "error" . $conn->error;
			}
		}
	}

	//Lähetetään sähköposti tilauksen tiedoista.
	
	$to = "aarokolu.ak@gmail.com"; //Lähettäjän SP
	$from = $_COOKIE['emailG']; //Kenelle lähetetään
	$subject = "Lomake"; //SP title.
	$headers = "From:" . $from;
		
	//Viesti
		
	// $message =  "Lomakkeen tiedot" . "\n" . "\n" . $firstNameG . " " . $surNameG . "\n" . "\n" . "Puh numero " . $puhNG . " " . "\n" . "Osoite " . $addressG . "\n" . "Matkustaja määrä " . $amount .
				// "Lennon tiedot " . $result2; 
	// mail($from,$subject,$message,$headers);
	
	//Poistaa alussa annetun matkustaja määrän taulukosta.
	$deleteM = "DELETE FROM matkustajat";
		
		if ($conn->query($deleteM) === TRUE) {
			echo "";
		} else {
			echo "Error" . $conn->error;
		}
		
		if(isset($_GET['back'])) {
		$conn->close();
	}
	
	//Poistetaan cookiet
	setcookie("date", "", time() - 1000);
	setcookie("LentoID", "", time() - 1000);
	setcookie("emailG", "", time() - 1000);
	setcookie("passengers", "", time() - 1000);
$conn->close();
?>
<!-- Kiitos sivu -->
<div class="row">
  <div class="main">
    <h2> </h2>
	<div class="center">Kiitos tilauksesta <br><br>
	<input type="button" name="back" id="back" class="button" onclick = "myF();" value="Palaa etusivulle"></div>
	</div>
	
  </div>
</div>
</body>
</html>