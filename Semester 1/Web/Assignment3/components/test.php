

<?php

$q=array(
    array('productLine' => 'A', 'textDescription' => 'B'),
    array('productLine' => 'A2', 'textDescription' => 'B2'),
    array('productLine' => 'A3', 'textDescription' => 'B3'),
    array('productLine' => 'A4', 'textDescription' => 'B4'),
    array('productLine' => 'A5', 'textDescription' => 'B5'),
);

$s=array(
    array('productCode' => "a", 'productName' => "b", 'productLine' => "c"),
    array('productCode' => "a2", 'productName' => "b2", 'productLine' => "c2"),
    array('productCode' => "a3", 'productName' => "b3", 'productLine' => "c3"),
    array('productCode' => "a4", 'productName' => "b4", 'productLine' => "c4"),
    array('productCode' => "a5", 'productName' => "b5", 'productLine' => "c5"),
);

foreach ($q as $r) {

    $current_product = $r['productLine'];
    echo "<h2>".$current_product."</h2>";
    echo "<p>". $r['textDescription']. "</p>";

    echo "<table>";

    foreach($s as $row) {
        echo "<tr><td>".$row['productCode']."</td><td>".$row['productName']."</td><td>".$row['productLine']."</td></tr>";
    }

    echo "</table>";
}
