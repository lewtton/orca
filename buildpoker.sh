#!/bin/bash
echo "开始执行编译"
pkill -9 uwsgi
npm run build
rm -R /home/david/Documents/orca/templates/poker
rm -R /home/david/Documents/orca/static/js
rm -R /home/david/Documents/orca/static/css
mv /home/david/Documents/orca/poker/build /home/david/Documents/orca/templates/poker
mv /home/david/Documents/orca/templates/poker/static/* /home/david/Documents/orca/static/
uwsgi -i /home/david/Documents/orca/uwsgi.ini