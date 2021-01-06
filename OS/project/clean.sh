#! /bin/bash

echo "================"
echo "Starting Cleanup"
echo "================"

# Kill stray processes
killall ./*.sh

# Remove pipes and lock files left by prematurely
# terminated processes
rm ./*.pipe ./*.lock

# Reset the application - delete all user folders
rm -r ./*/

echo "================"
echo "Cleanup Complete"
echo "================"