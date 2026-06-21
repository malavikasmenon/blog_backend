#!/bin/bash

sudo cp blog_api.conf /etc/nginx/sites-available/blog_api

sudo ln -sf \
  /etc/nginx/sites-available/blog_api \
  /etc/nginx/sites-enabled/blog_api

sudo nginx -t
sudo systemctl reload nginx