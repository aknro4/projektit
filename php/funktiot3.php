<!DOCTYPE html>
<html lang = "fi">
<head>
<meta charset="UTF-8">
<style>

body {
	background-color: gray;
}

</style>

<body>

<form method="post" action= " ">

<p> Sauvojen käyttötarkoitus</p> 
<select name="options" id="options" multiple>
	<option name="option1">Perinteinen</option>
    <option name="option2">Luisteluhiihto</option>
    <option name="option3">Sauvakävely</option>
</select>

<p>Kuinka pitkä olet?</p>
<input type="number" name="myNumber"> 
	
<input type="submit" name="submit" value="Lähetä">
</form>	


<?php 

	
	if(isset($_POST["submit"])) {
		function math() {
			
			$options = $_POST["options"];
			
			$option1 = $_POST["option1"];
			$option2 = $_POST["option2"];
			$option3 = $_POST["option3"];
			
			$myNumber = $_POST["myNumber"];
			
				if($options == $option1){
					$total1 = $myNumber * 0.85;
					
					echo "Pituus";
					echo $total1;
					
				} elseif ($options == $option2) {
					$total2 = $myNumber * 0.9;
					
					echo "Pituus";
					echo $total2;
					
				} else {
					$total3 = $myNumber * 0.68;
					
					echo "Sauvan pituus";
					echo $total3;
				}
		}
	}
	
	math();
	
?> 