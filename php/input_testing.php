<!DOCTYPE html>
<html lang = "fi">
<meta charset="UTF-8">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script type="text/javascript">

//Jos haluaa peruttaa tilauksen.
function myF () {
	location.replace("connection_test.php")
}

//disables submit button jos arvo on tyhjä..  toimii vain kerran
$(document).ready(function() {
     $(':input[type="submit"]').prop('disabled', true);
     $('#email').keyup(function() {
        if($(this).val() != '') {
           $(':input[type="submit"]').prop('disabled', false);
        }
     });
 });
</script>
</head>
<body>
<?php

if (isset($_GET['submit'])) {
	
	
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
	//Siiretään kun vahvistetaan tilausta.
	//Ostajan tiedot
	$firsNameG = $_GET['firstName'];
	$surNameG = $_GET['surName'];
	$puhNG = $_GET['puhN'];
	$addressG = $_GET['address'];
	$emailG = $_GET['email'];
	
	//Siirto tapahtuu... Tee koodi missä tarkistaa onko input arvot tyhjiä.
	//$conn->query("INSERT INTO userinfo (Etunimi, Sukunimi, PuhNumero, Osoite, Email) VALUES ('$firsNameG', '$surNameG', '$puhNG', '$addressG', '$emailG')");
	

	//Käyttäjän valitsema kohdemaa ja lähtöaika
	$where = $_GET["mihin"];
	$time = $_GET["aika"];
	
	//Päivämäärä
	$date = $_GET["pvm"];
	
	//Matkustaja määrä
	$amount = $_GET["passengers"];
	
	//Haetaan valitun maan ja ajan perusteella
	$sql = "SELECT LentoID, Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE Kohdemaa = '$where' AND Aika = '$time' AND VapaatPaikat >= '$amount'";
	$result = $conn->query($sql); 

	//Haetaan Lennon ID arvo jota voidaan käyttää tarkempaa hakua varten. 
	//Tavoitteena suorittaa lippujen vähennys ID perusteella. 
	//Ja mahdollisesti lisätä uuteen sql taulukkoon missä näkyy kaikki tilaukset.

	//LentoID 
	$idV = "SELECT LentoID FROM lennot WHERE Kohdemaa = '$where' AND Aika = '$time' AND VapaatPaikat >= '$amount'";
	$result2 = $conn->query($idV);
	
	//Aika
	$aika = "SELECT Aika FROM lennot WHERE Kohdemaa = '$where' AND Aika = '$time' AND VapaatPaikat >= '$amount'";
	$result3 = $conn->query($aika);
	
	
	//Tulostetaan
if ($result2->num_rows > 0) {
		echo "Mihin kaupunkiin ";
		echo "</br>";
		
		//Tehdään form taulukko
		echo "<form method='get' action='tilauksenVahvistus.php'> <select name='town' id='town' multiple>";
		
		//Ongelma. Joko saan itselleni ID arvon tarkempaa hakua varten ja käyttäjä ei näe lennon tietoja. 
		//Tai aisakas näkee lennon tiedot mutta en saa tarkempaa hakua tehtyä.
		while($row2 = $result2->fetch_assoc() && $row3 = $result3->fetch_assoc()) {
			echo "<option name='' id='' value=". $row2['LentoID']. ">" . "Lähtöaika: " . $row3['Aika'] . " " 
			 . " - PVM " . $date . " Lipun hinta/KPL "  . "€" . "</option>";
		}
			echo  "</select>";
	} else {
			//Erorreita varten -> tee järkevämpi
			echo "Ei tuloksia, Input: ";
			echo $where;
			echo " ";
			echo $time;
	}
}

// if (isset($_GET['submit'])) {
	
	// $id = $_GET['town'];
	
	// $sql2 = "SELECT LentoID, Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE LentoID ='$id'";
	// $result3 = $conn->query($sql2);
	
		// if(result3->num_rows > 0) {
			// while($row3 = $result3->fetch_assoc()) {
				// $conn->query ("INSERT INTO valihaku(ajanKohta, KohdeKaupunki,PVM,LennoID) VALUES(".$row3['Aika'] .",". $row3['Kaupunki'] .",$date". $row3['LentoID'] .").");
			// }
			
		// }
// }

?>

<!-- Käyttäjän input -->
<form method="get" action="tilauksenVahvistus.php">
<p>Anna sinun yhteystiedot</p>
	<input type="text" name="firstName" id="firstName" required> Etunimi</br>
	<input type="text" name="surName" id="surName" required> Sukunimi</br>
	<input type="number" name="puhN" id="puhN" required> Puh numero</br> 
	<input type="text" name="address" id="address" required> Osoite</br> 
	<input type="email" name="email" id="email" required> Email</br>
	</br>
		
	<input type="submit" name="submit" id="submit" value="Varaa" disabled="disabled">
<!-- Jos käyttäjä haluaa peruttaa tilauksen. Palaa "etusivulle" -->
	<input type="button" name="cancel" id="cancel" value="Peruuta" onClick="myF();">

</form>
</body>
</html>