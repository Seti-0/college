<?php

require "components/my_connect.php";
require "components/my_table.php";

$paymentsQuery = "SELECT * FROM classicmodels.payments
                  ORDER BY paymentDate DESC
                  LIMIT 20;";
$paymentsResult = $connection->query($paymentsQuery);

if (isset($_GET["target"])) {

    $customerQuery = $connection->prepare("SELECT customerName, phone, salesRepEmployeeNumber, creditLimit 
                  FROM classicmodels.customers
                  WHERE customers.customerNumber = ?;");
    $customerQuery->bind_param("s", $_GET["target"]);
    $customerQuery->execute();

    $customerResult = $customerQuery->get_result();

}
else {

    $customerResult = null;

}

if ($customerResult !== null && $customerResult->num_rows > 0) {

    $customerResult = $customerResult->fetch_assoc();

    $historyQuery = $connection->prepare(
            "SELECT checkNumber, paymentDate, amount 
                 FROM classicmodels.payments
                 WHERE payments.customerNumber = ?
                 ORDER BY payments.paymentDate DESC;");
    $historyQuery->bind_param("s", $_GET["target"]);
    $historyQuery->execute();

    $historyResult = $historyQuery->get_result();

    $totalQuery = $connection->prepare("SELECT sum(amount) FROM classicmodels.payments
               WHERE customerNumber = ?");
    $totalQuery->bind_param("s", $_GET["target"]);
    $totalQuery->execute();

    $totalResult = $totalQuery->get_result();

    if ($totalResult->num_rows > 0) {

        $totalResult = $totalResult->fetch_assoc()["sum(amount)"];

        if ($totalResult == null) {
            $totalResult = "Unknown";
        }

    }
    else {
        $totalResult = "Error";
    }

    $displayCustomerInfo = true;
    $container = "two-part-container";
    require "components/my_separator.php";

}
else {

    $displayCustomerInfo = false;
    $historyResult = null;
    $totalResult = null;
    $container = "one-part-container";

}



$connection->close();

?>
<html lang="en">
<?php require 'components/my_head.php'; ?>
<body class=<?=$container?>>
<?php require 'components/my_nav.php' ?>
<div class=part-A>
    <?php tabulateQuery($paymentsResult, TableType::Clickable, "payments.php"); ?>
</div>
<?php if($displayCustomerInfo) { ?>
<?php separator("Customer Info: " . $customerResult["customerName"]); ?>
<div class=part-B>
    <div class=customer-info>
        <p class=customer-details>
            Phone Number: <em><?=$customerResult["phone"]?></em>
            Sales Rep #: <em><?=$customerResult["salesRepEmployeeNumber"]?></em>
            Credit Limit: <em><?=$customerResult["creditLimit"]?></em>
            Total Paid: <em><?=$totalResult?></em>
        </p>
    </div>
    <?php tabulateQuery($historyResult); ?>
</div>
<?php } ?>
<?php require "components/my_footer.php"; ?>
</body>
</html>