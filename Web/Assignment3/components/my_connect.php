<?php
/**
 * @var ?mysqli::__construct $connection
 */

require "config.php";
$connection = new mysqli(servername, username, password);

if ($connection->connect_error) {
?>
<div class=connection-error>
    <h2>An error occurred while trying to connect to the database</h2>
    <ul>
        <li>Host name: <?=servername?></li>
        <li>User name: <?=username?></li>
        <li>Password: <?=password?></li>
    </ul>
    <p>Connection Failed: <?=$connection->connect_error?></p>
</div>
<?php
    $connection = null;
}

?>