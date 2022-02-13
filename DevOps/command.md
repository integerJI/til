# Aws ec2 ubuntu 접속

key.pem은 꼭 권한 바꿔주기
```
chmod 400
```

ssh 접속
```
ssh -i *.pem ubuntu계정@public dns
```

# Django 실행

Port 지정 후 서버 실행
```
python manage.py runserver 0:8000
```

# gunicorn 관련
gunicorn 실행
```
gunicorn "projectName".wsgi --bind 0:8000
```

gunicorn service 생성
```
sudo vim /etc/systemd/system/gunicorn.service
```

gunicorn.service
```
[Unit]
Description=Gunicorn Daemon

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/env/"githubName"
ExecStart=/home/ubuntu/env/bin/gunicorn "projectName".wsgi --bind 0:8000

[Install]
WantedBy=multi-user.target
```

gunicorn enable
```
sudo systemctl enable gunicorn.service
```

gunicorn start
```
sudo systemctl start gunicorn.service
```

gunicorn status
```
sudo service gunicorn status
```

gunicorn restart
```
sudo service gunicorn restart
```

gunicorn 프로세스 확인
```
ps aux | grep gunicorn
```