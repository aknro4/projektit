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
	<input type="number" name="firstN"> First number <br>
	<input type="number" name="secondN"> Second number <br>
	<br><br>
	<input type="submit" name="submit" value="Lähetä">
</form>	


<?php 
	

	
	if(isset($_POST["submit"])) {
		function math() {
			$value1 = $_POST["firstN"];
			$value2 = $_POST["secondN"];
			
			$total = $value1 + $value2;
			
			echo $value1;
			echo " + ";
			echo $value2;
			echo " = ";
			echo $total;
		}
	}
	
	math();
	
?>

</body>
</html>