<!DOCTYPE html>
<html lang = "fi">
<head>
<meta charset="UTF-8">

<style>

body {
	background-color:gray;
}

</style> 

<body>

<?php

	$firstName = $_GET["firstName"];
	$secondName = $_GET["secondName"];
	
	// Opiskelijanumero
	$number = $_GET["number"];
	
	// Ryhmätunnus
	$classID = $_GET["classID"];
	
	// Kurssit 
	$course = $_GET["courses"];	
		
	// Opettajat
	$teacher = $_GET["teachers"];
	
	// PVM
	$myDate = $_GET["myDate"];
	
	//Näyttää sivulla tiedot.
	
	echo "Etunimi";
	echo "</br>";
	echo $firstName;
	echo "</br>";
	echo "Sukunimi";
	echo "</br>";
	echo $secondName;
	echo "</br>";
	echo "</br>";
	
	echo "Opiskelijanumero:";
	echo " ";
	echo $number;
	echo "</br>";
	echo "Ryhmätunnus:";
	echo " ";
	echo $classID;
	echo "</br>";
	echo "</br>";

	echo "Kurssi:";
	echo " ";
	echo $course;
	echo "</br>";
	
	echo "Opettaja:";
	echo " ";
	echo $teacher;
	echo "</br>";
	echo "</br>";

	echo "Päivämäärä";
	echo "</br>";
	echo $myDate;
	echo "</br>";
	echo "</br>";
	
	
	
//Lähettää sähköpostin.
	
	if(isset($_POST["button1"])) {
		
		//------------//
		
		//Ei myöskään lähetä vaikka arvot ovat if statementin sisällä
		
		// $firstName = $_POST["firstName"];
		// $secondName = $_POST["secondName"];
		
		//Opiskelijanumero
		// $number = $_POST["number"];
		
		//Ryhmätunnus
		// $classID = $_POST["classID"];
		
		//Kurssit 
		// $course = $_POST["courses"];	
			
		//Opettajat
		// $teacher = $_POST["teachers"];
		
		//PVM
		// $myDate = $_POST["myDate"];
		
		//------------//
		
		//Sp tiedot
		
		$to = "aarokolu.ak@gmail.com"; //Lähettäjän SP
		$from = $_POST["myEmail"]; //Kenelle lähetetään --> Tämän arvon saa lähetettyä spseen. 
		$subject = "Lomake"; //SP title.
		$headers = "From:" . $from;
		
		//Ei lähetä tietoja sp. 
		//"echo $firstName;" ei toimi. Tai "$firstName" / $firstName.
		
		$message =  "Lomakkeen tiedot" . "\n" . "\n" . $firstName . " " . $secondName . "\n" . "\n" . "Opiskelijanumero " . $number . " " . "\n" . "Ryhmätunnus " . $classID . "\n" .
					"Kurssi " . $course . " " . "\n" .  "Opettaja " . $teacher . "\n" . "\n" . "Päivämäärä " . $myDate; 

		mail($from,$subject,$message,$headers);
	}
?>

<form method="post">
	
	Sahköposti <br>
	<input type="text" name="myEmail"> 
	<br><br> 
	<input type="submit" name="button1" value="Lähetä">
	
</form>

</body>
</html>