#!/bin/bash

apt update
apt install nginx -y

mkdir -p /var/www/TF01
cp -r ./website/* /var/www/TF01/

chown -R www-data:www-data /var/www/TF01
chmod -R 755 /var/www/TF01
cp ./nginx/site.conf /etc/nginx/sites-available/site.conf
ln -sf /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/

systemctl enable nginx
systemctl restart nginx