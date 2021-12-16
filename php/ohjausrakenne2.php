<!DOCTYPE html>
<html>
<body>

<form method="post">
	Numero <input type="number" name="nValue">
	<br><br>
	<input type="submit" name="button1" value="Laheta">
</form>

<?php 
if (isset($_POST["button1"])){
	
		$n = $_POST["nValue"];
		
		$nV = $n + 9;

	for ($x = $n; $x <= $nV; $x++) {
		echo "$x <br>";
	}
}	
?>  

</body>
</html>