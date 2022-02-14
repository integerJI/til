# ngnix 설정

ngnix 파일 생성
```
cd /etc/nginx/sites-available/
sudo vi "projectName".com
```

"projectName".com
```
server {
    listen 80;
    server_name "ec2PublicIp";

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static {
        alias /home/ubuntu/env/"githubName"/"staticDir";
    }

    location /media {
        alias /home/ubuntu/env/"githubName"/"mediaDir";
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }

}
```

enabled 폴더 이동
```
cd ..
cd sites-enabled
```

symbolic link 제거 및 재설정
```
sudo rm -rf default
sudo ln -s etc/nginx/sites-available/"projectName".com default
```

ngnix 시작
```
sudo service nginx start
```
ngnix 재시작
```
sudo service nginx restart
```
ngnix 정지
```
sudo service nginx stop
```
ngnix 상태 확인
```
sudo service nginx status
```