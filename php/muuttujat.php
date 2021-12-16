<!DOCTYPE html>
<html>
<body>
<!-- HTML -->

<form method="post">
	Etunimi: <input type="text" name="firstName">
	<br>
	Sukunimi: <input type="text"  name="secondName">
	<br>
	Kuukausipalkka: <input type="number" name="income">
	<br>
	Veroprosentti: <input type="number" name="taxes">
	<br><br>
	<input type="submit" name="button1" value="Laheta">
</form>

<?php
	if (isset($_POST["button1"])){
	//Nettopalkka
	
	$income1 = $_POST["income"];
	$taxes1 = $_POST["taxes"];
	
	$toDecimal = $taxes1 / 100;
	$secondTotal = $income1 * $toDecimal;
	$newTotal = $income1 - $secondTotal;
	
	//Bruttopalkka
	
	$brutto = 1 - $toDecimal;
	$totalBrutto = $newTotal / $brutto;
	
	}

	$firstName = $_POST["firstName"];
	$secondName = $_POST["secondName"];
	
	echo $firstName;
	echo "<br>";
	echo $secondName;
	echo "<br>";
	echo "Nettopalkka";
	echo "<br>";
	echo $newTotal;
	echo "<br>";
	echo "Bruttopalkka";
	echo "<br>";
	echo $totalBrutto;
?>

</body>
</html>