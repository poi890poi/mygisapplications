<?php

//echo "readbin.php";
$name = 'sample.bin';
$headersize = 18;
$rowsize = 18;
$x = 4;
$y = 2;
$width = 8;
$height = 4;

try {
    $fp = fopen($name, 'rb');
    $offset = $headersize + $rowsize * $y + $x;
    echo nl2br("reading at ".$x.", ".$y." (offset: ".$offset.")\n\n");
    for ($l = 0; $l < $height; $l++) {
        fseek($fp, $offset);
        $buffer = fgets($fp, $width+1);
        for ($i = 0; $i < strlen($buffer); $i++) {
            echo strtoupper(str_pad(dechex(ord($buffer[$i])), 2, '0', STR_PAD_LEFT));
            echo " ";
        }
        echo nl2br("\n");
        $offset += $rowsize;
    }
} catch (Exception $e) {
    echo 'Caught exception: ', $e->getMessage(), "\n";
}
    
exit;

?>
