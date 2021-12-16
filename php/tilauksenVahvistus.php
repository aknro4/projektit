<!DOCTYPE html>
<html lang = "fi">
<meta charset="UTF-8">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script type="text/javascript">
//Paluu "etusivulle"
function myF () {
	location.replace("connection_test.php")
}
</script> 
</head>
<body>
<?php 

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

	//Siiretään kun vahvistetaan tilausta.
	//Ostajan tiedot
	$firsNameG = $_GET['firstName'];
	$surNameG = $_GET['surName'];
	$puhNG = $_GET['puhN'];
	$addressG = $_GET['address'];
	$emailG = $_GET['email'];
	
	//Päivämäärä
	$date = $_GET["pvm"];
	
	//Näytetään tilauksen tiedot
	$idL = $_GET["town"];
	
	//Matukstaja määrä
	$amount =$_GET['passengers'];
	
	$sql3 = "SELECT Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE LentoID = '$idL'";
	$result2 = $conn->query($sql3);
	
	//Viellä kertaalleen näytetään varauksen tiedot.
	echo "Varauksen tiedot" . "</br>" . "Etunimi: " . $firsNameG . "</br>" . "Sukunimi: " . $surNameG . "</br>" . "Matukstajat: " . $amount . "</br>" . "</br>" . "Puh numero: " . $puhNG . "</br>" . "Osoite: " .
	$addressG . "</br>" . "Email " . $emailG . "</br>" . "</br>" . "Lennon tiedot ". "</br>";

	//Kaikki lennon tiedot
	$sql3 = "SELECT Aika, Kohdemaa, Kaupunki, LipunHinta, VapaatPaikat FROM lennot WHERE LentoID = '$idL'";
	$result3 = $conn->query($sql3);
	
	//tallennetaan arvot tietokantaan
	$conn->query ("INSERT INTO tilausTiedot (PVM, Email) VALUES ('$date', '$emailG')");
	
	//Haetaan ajankohta
	// $sql4 = "SELECT Aika From lennot WHERE LentoID = '$idL'";
	// $result4 = $conn->query($sql4);
	
	//Haetaan kaupunki
	// $sql5 = "SELECT Kaupunki From lennot WHERE LentoID = '$idL'";
	// $result5 = $conn->query($sql5);
	
	if ($result3->num_rows > 0) {
		while ($row2 = $result3->fetch_assoc()){
			echo "Kohdemaa: " . $row2['Kohdemaa'] . "</br>" . " Kaupunki " . $row2['Kaupunki'] . "</br>" . " Aikataulu " . $row2['Aika'] . "</br>" . " Lipun hinta KPL " . $row2['LipunHinta'] . "€";
		
			$conn->query ("INSERT INTO tilausTiedot (Aika,Kaupunki) VALUES (".$row2['Aika'] .",". $row2['Kaupunki'] . ").");
		}
	}

	
	if (isset($_GET['submit'])) {
	
		$sql = "SELECT VapaatPaikat FROM lennot WHERE LentoID = '$idL'";
		$result = $conn->query($sql);

		if ($result3->num_rows > 0) {
		while ($row2 = $result3->fetch_assoc()){		
			$conn->query ("INSERT INTO tilausTiedot (Aika,Kaupunki) VALUES (".$row2['Aika'] .",". $row2['Kaupunki'] . ").");
		}
	}

		if ($result->num_rows > 0) {
			while ($row = $result->fetch_assoc()) {
				$implod = implode($row);
				
				//yllättäen ei toimi gööögle time
				$math = $implod - $amount;
				
				$sql2 = "UPDATE lennot SET VapaatPaikat = $math WHERE LentoID = '$idL'";
				
				if ($conn->query($sql2) === TRUE) {
					echo $amount;
				} else {
					echo "Error updating record: " . $conn->error;
				}

$conn->close();
			}
		}
	}
	
?>

<form method="get" action="tilausN.php">

<p>Vahvistetaanko tilaus</p>
<!-- Siirtyy "Tilaus vahvistettu" sivulle -->
<input type="submit" name="submit" id="submit" value="Vahvista">

<!-- Palaa "etusivulle" -->
<input type="button" name="decline" id="decline" value="Peruuta" onClick="myF();">

</form>

</body>
</html>