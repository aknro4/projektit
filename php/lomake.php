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


<form action="lomake2.php" method="get">

	<h1> LOMAKE </h1>
	
	<p> Etunimi</p>
	<input type="text" name="firstName">
	<br>
	
	<p> Sukunimi</p>
	<input type="text" name="secondName"></input>
	<br>
	
	<p> Opiskelijanumero</p>
	<input type="number" name="number"></input>
	<br>
	
	<p> Ryhmätunnus</p>
	<input type="text" name="classID"></input>
	<br>
	
	<p> Kurssi tarjotin</p> 
<select name="courses" id="courses" multiple>
    <option name="course1">Kurssi 1</option>
    <option name="course2">Kurssi 2</option>
    <option name="course3">Kurssi 3</option>
</select>
	
	<p> Opettajat</p> 
<select name="teachers" id="teachers" multiple>
    <option name="teacher1">Opettaja 1</option>
    <option name="teacher2">Opettaja 2</option>
    <option name="teacher3">Opettaja 3</option>
</select>
	
	<p> Kurssin ajankohta</p>
	<input type="date" name="myDate">
	<br><br>
	
	<input type="submit" name="button1" value="Lähetä">
	
</form>


<?php
	
?>

</body>
</html>