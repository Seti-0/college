<?php

require "components/my_connect.php";

if ($connection) {

    $linesQuery = "SELECT * FROM classicmodels.productlines;";
    $linesResult = $connection->query($linesQuery);

}

if (isset($_GET["target"])) {

    $productQuery = $connection->prepare("
            SELECT products.* FROM classicmodels.products
            JOIN classicmodels.productlines 
            ON productlines.productLine = products.productLine
            WHERE products.productLine = ?;");

    $productQuery->bind_param("s", $_GET["target"]);
    $productQuery->execute();
    $productResult = $productQuery->get_result();

    $displayProducts = true;
    $container = "two-part-container";

    require "components/my_table.php";
    require "components/my_separator.php";

}
else {

    $productResult = null;

    $displayProducts = false;
    $container = "one-part-container";

}

$connection->close();

?>
<html lang="en">
<?php require 'components/my_head.php'; ?>
<body class=<?=$container?>>
    <?php require 'components/my_nav.php' ?>
    <ul class="part-A product-lines">
        <?php while ($current = $linesResult->fetch_assoc()) { ?>
        <?php $line=$current["productLine"] ?>
        <li id="<?=$line?>" class=product-line>
            <a href="index.php?target=<?=$line?>#<?=$line?>">
                <div class=product-line-title-bar>
                    <h2 class=product-line-title><?=$line?></h2>
                </div>
                <p class=product-line-description><?=$current["textDescription"]?></p>
            </a>
        </li>
        <?php } ?>
    </ul>
    <?php if ($displayProducts) { ?>
    <?php separator("Products"); ?>
    <div class=part-B>
        <?php tabulateQuery($productResult); ?>
    </div>
    <?php } ?>
    <?php require "components/my_footer.php"; ?>
</body>
</html>