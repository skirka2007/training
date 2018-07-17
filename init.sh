sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
#sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
#sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('pass111')"
mysql -uroot -e "CREATE DATABASE mybase"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'@'localhost'"

python manage.py makemigrations
python manage.py migrate

cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application


