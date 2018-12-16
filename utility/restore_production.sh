USERNAME="radorado"
APP="hackconf-production-2019"

echo "Fetching latest dump ...\n"
curl -o db.dump `heroku pg:backups:public-url --app $APP`

echo "Recreating database ...\n"
dropdb --if-exists colab
sudo -u postgres createdb -O $USERNAME hackconf

echo "Starting pg_restore ...\n"
pg_restore -U $USERNAME -d hackconf -c -j 4 db.dump > dump_log 2>&1
rm db.dump

echo "Migrations and data ...\n"
python manage.py migrate
