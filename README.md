To add new files and directories to git:
1) git add (name of directories)

To update current files:
1) git commit -a -m "Update 1.0"
2) git push

To update repo:
1) git pull

To clone repo:
1) git clone https://github.com/skirka2007/training.git /home/box/web

To start init.sh:
1) bash /home/box/web/init.sh

To maintain server on local pc:
1) sudo ln -sf /home/inesterova/training/etc/nginx.conf /etc/nginx/sites-enabled/default
2) sudo /etc/init.d/nginx restart

3) gunicorn -b 0.0.0.0:8080 hello

To test locally:
﻿1) curl -vv 'http://127.0.0.1/hello/?a=1&a=2&b=3'


