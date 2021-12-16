<!DOCTYPE html>
<html lang="fi">
<meta charset="UTF-8">
<body>
<!-- HTML -->

<form method="post">
	Ikä: <input type="number" name="age">
<br>
	Sukupuoli 
<br>
<input type="radio" name="male" value="male">Mies 
<input type="radio" name="female" value="female"> Nainen
	<br><br>
	<input type="submit" name="button1" value="Laheta">
</form>

<?php

if (isset($_POST["button1"])){
	
	$age1 = $_POST["age"];
	$genderM = $_POST["male"];
	$genderF = $_POST["female"];
		
		//Jos alle 0 tai yli 110
		
		if ($age1 <= 0 || $age1 > 110) {
			echo "Kuinka vanha luulet olevasi";
		}
		
		//Jos on mies
		
		elseif ($genderM &&  $age1 <= 13 ) {
			echo "Mitä poitsu";
		} 
		elseif ($genderM && $age1 >= 14 && $age1 <= 25) {
			echo "Mitä nuori mies";
		} 
		elseif ($genderM && $age1 >= 26 && $age1 <= 56) {
			echo "Olet mies parhaassa iässä";	
		} 
		elseif ($genderM && $age1 > 57 ) {
			echo "Olet jo eläke iässä";
		} 
		
		//Jos on nainen
		
		elseif ($genderF && $age1 <= 13) {
			echo "saisinko";
		} 
		elseif ($genderF && $age1 >= 14 && $age1 <= 25) {
			echo "tarjoilija";
		} 
		elseif ($genderF && $age1 >= 26 && $age1 <= 56) {
			echo "kahvia";
		} 
		elseif ($genderF && $age1 > 57) {
			echo "Kiitos";
		} 
		
		//Error
		
		else {
			echo "what im doing";	
		}
}
?>

</body>
</html>