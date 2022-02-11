# 빠른 Project 생성 명령어 (for windows)

가상환경 생성
```
python -m venv myvenv
```

가상환경 실행
```
source myvenv/Scripts/activate
```

Django 설치
```
pip install django
```

pip 업그레이드
```
python -m pip install --upgrade pip
```

Django 프로젝트 생성
```
django-admin startproject project
```

Django 앱 생성
```
cd project

python manage.py startapp app
```

DB 마이그
```
python manage.py migrate
```

Super User 생성
```
python manage.py createsuperuser
```

서버 실행
```
python manage.py runserver
```

패키지 목록 파일화
```
pip freeze > requirements.txt
```

패키지 일괄 다운
```
pip install -r requirements.txt
```