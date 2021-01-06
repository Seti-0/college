<?php

function splitCamel(string $input) : string {

    $pattern = "/(?<=[a-z])(?=[A-Z])/";
    $separator = " ";

    $input = preg_replace($pattern, $separator, $input);
    $input = ucfirst($input);

    return $input;
}

abstract class TableType {
    const Normal = 1;
    const Button = 2;
    const Clickable = 3;
}

function tabulateQuery(?mysqli_result $result,
                       int $tableType = TableType::Normal,
                       string $baseTarget = "",
                       string $buttonText = "More Info")
{

    if ($result === null) {
        echo "<p class='empty'>An error occurred while retrieving data</p>";
        return;
    }

    if ($result->num_rows === 0) {
        echo "<p class='empty'>No records to display</p>";
        return;
    }

    echo "<table>";

    // Header row

    echo "<tr>";
    if ($tableType === TableType::Button) {
        // An extra empty cell for the button column, if there is one
        echo "<th></th>";
    }
    foreach ($result->fetch_fields() as $field) {
        $name = splitCamel($field->name);
        echo "<th>$name</th>";
    }
    echo "</tr>";

    // Data rows

    while ($currentRow = $result->fetch_row()) {

        $firstValue = $currentRow[0];

        // This will be the GET request if there is a user interaction.
        $target = "$baseTarget?target=$firstValue";

        echo "<tr>";

        // Depending on the type of user interaction requested (if any),
        // the first column(s) of the table will be different
        switch ($tableType) {

            case TableType::Normal:
                // default: no interaction
                echo "<td>$firstValue</td>";
                break;

            case TableType::Clickable:
                // Make the first cell send a GET request
                echo "<td class='clickable' ><a href='$target'>$firstValue</a></td>";
                break;

            case TableType::Button:
                // Add a button cell and make it send a GET request.
                // The first data cell is unchanged.
                echo "<td><a href='$target'><button>$buttonText</button></a></td>";
                echo "<td>$firstValue</td>";
                break;
        }

        foreach (array_slice($currentRow, 1) as $cell) {
            echo "<td>$cell</td>";
        }

        echo "</tr>";
    }

    echo "</table>";

}
