<!DOCTYPE html>
<html lang = "fi">
<meta charset="UTF-8">
<body>

<?php 

?> 

<form method="get" action="input_testing.php">

<!-- Kohdemaa valinta -->
<p>Mihin</p>
<select name="mihin" id="mihin" multiple>
	 <option id="Suomi" name="Suomi">Suomi</option>
     <option id="Norja" name="Norja">Norja</option>
     <option id="Tanska" name="Tanska">Tanska</option>
	 <option id="Ruotsi" name="Ruotsi">Ruotsi</option>
	 <option id="Islanti" name="Islanti">Islanti</option>
</select>

</br></br>

<!-- Lähöajan valinta -->
<p>Lähtöaika</p>
<select name="aika" id="aika" multiple>
	 <option id="Päivä" name="Päivä">Päivä</option>
     <option id="Ilta" name="Ilta">Ilta</option>
     <option id="Aamu" name="Aamu">Aamu</option>
</select>
</br>

<!-- Matustajamäärän syöttö -->

<p>Matkustajamäärä</p>
<input type="number" id="passengers" name="passengers">
</br>

<!-- Lähdön haluttu päivämäärä -->

<p>Valitse lähtöpäivä</p>
<input type="date" name="pvm" id="pvm">
</br>
</br>

<input type="submit" name="submit" value="Lähetä">

</form>


</body>
</html>