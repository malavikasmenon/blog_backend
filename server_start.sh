# server_start.sh
#!/bin/bash

cd ~/blog_backend
source blog/bin/activate
git pull origin main

pip install -r requirements.txt

pkill gunicorn
nohup gunicorn blog_backend.wsgi:application \
  --bind 127.0.0.1:8000 \
  --workers 2 \
  > gunicorn.log 2>&1 &