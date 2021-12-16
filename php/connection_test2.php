<?php  

$palvelin= "localhost";  
$kayttajanimi= "root";  
$salasana= "";  
$tietokanta= "lennot"; 
$portti="3306"; 

//Luodaan yhteys tietokantaan  

$conn = mysqli_connect($palvelin, $kayttajanimi, $salasana, $tietokanta, $portti);  

//Tsekataan onnistuuko yhteys 

if (!$conn) 
{  
    die("Yhteys ei onnistunut " . mysqli_connect_error());  
}  

$sql = "SELECT LentoID, Kohdemaa,Aika, Kaupunki FROM lennot WHERE Kohdemaa = 'Ruotsi' AND Aika = 'Aamu'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {

  while($row = $result->fetch_assoc()) {
    echo "Lento ID: " . $row["LentoID"] . " Aikataulu: ". $row["Aika"] . ". Kohdemaa: "  . $row["Kohdemaa"]. ". Kaupunki: " . $row["Kaupunki"]. "<br>";
  }
} else {
  echo "Ei tuoloksia";
}


?>