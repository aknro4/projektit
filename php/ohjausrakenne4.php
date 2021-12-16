<!DOCTYPE html>
<html>
<body>

<?php 
function nNumber($n){  
    $num = 0; 
  
    for ($i = 0; $i < $n; $i++) 
    { 
        for ($j = 0; $j <= $i; $j++ ) 
        { 
            echo $num." "; 
        } 
            $num = $num + 1;  
        echo "</br>"; 
    } 
} 
    $n = 10; 
    nNumber($n); 
?> 

</body>
</html>