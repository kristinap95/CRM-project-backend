# CRM-project-backend

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

cd crm_system

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

Email: (Your email here)

Name: (for example, admin)

is_superuser: True

password:

password:

python manage.py runserver
