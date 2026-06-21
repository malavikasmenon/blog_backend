# server_start.sh
#!/bin/bash

source blog/bin/activate

pip install -r requirements.txt

nohup gunicorn blog_backend.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 2 \
  > gunicorn.log 2>&1 &