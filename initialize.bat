@echo off
echo Initializing db
python manage.py makemigrations
python manage.py makemigrations evolution
python manage.py migrate
echo done!
pause
