sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
#sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
#sudo /etc/init.d/gunicorn restart

cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application

sudo /etc/init.d/mysql start
mysql -u root
CREATE DATABASE skirka CHARACTER SET utf8

python manage.py makemigrations
python manage.py migrate


