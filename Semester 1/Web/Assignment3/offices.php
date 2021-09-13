<?php

require "components/my_connect.php";
require "components/my_table.php";

$officesQuery = "SELECT * FROM classicmodels.offices;";
$officesResult = $connection->query($officesQuery);

if (isset($_GET["target"])) {

    $employeeQuery = $connection->prepare("
        SELECT employeeNumber, firstName, lastName, jobTitle, email 
        FROM classicmodels.employees
        JOIN classicmodels.offices 
        ON employees.officeCode = offices.officeCode
        WHERE employees.officeCode = ?;");

    $employeeQuery->bind_param("s", $_GET["target"]);
    $employeeQuery->execute();
    $employeeResult = $employeeQuery->get_result();

    $displayDetails = true;
    $container = "two-part-container";

    require "components/my_separator.php";

} else {

    $employeeResult = null;
    $displayDetails = false;
    $container = "one-part-container";

}

$connection->close();

?>
<html lang="en">
<?php require 'components/my_head.php'; ?>
<body class=<?=$container?>>
<?php require 'components/my_nav.php' ?>
<div class=part-A>
    <?php tabulateQuery($officesResult, TableType::Button, "offices.php", "Show Employees"); ?>
</div>
<?php if ($displayDetails) { ?>
    <?php separator("Employees"); ?>
    <div class=part-B>
        <?php tabulateQuery($employeeResult); ?>
    </div>
<?php } ?>
<?php require "components/my_footer.php"; ?>
</body>
</html>