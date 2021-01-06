pid=$(ps | tr -s " " | grep $1 | cut -d$' ' -f1)

echo $pid

echo $(ps)

