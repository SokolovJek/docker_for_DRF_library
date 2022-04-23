#!/bin/sh
# wait-for-postgres.sh
# Скрипт в цикле будет пробовать подключаться к базе данных и, когда произойдёт удачное
# подключение, совершит выход из бесконечного цикла

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="dante123456" psql -h "$host" -d "library" -U "dante" -c '\q';>
>&2 echo "Postgres is unavailable - sleeping"
sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd