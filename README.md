# Универсальный шаблон для быстрого запуска разработки на Django + React

Перед запуском необходимо создать файл .env в корневой директории проекта и в директориях /back и /front, заполнив их данными из .env_example.

## Запуск через docker compose
```shell
docker compose up --build -d
```
или
```shell
docker compose up --build
```
если хотите видеть логи во время разработки. В то же время для дебага удобнее запускать отдельно фронт и бэк.
Вот как это сделать:
## Запуск "вручную"
### frontend
```shell
cd front
npm i
npm run dev
```
### backend
```shell
cd back
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## Запуск в проде
Для запуска в проде используйте инструкцию "Запуск через docker compose" предварительно скопировав файл nginx/nginx.conf в папку /etc/nginx/sites-available и отредактировав его под свои нужны в местах, помеченных комменатриями. Также создайте symlink между файлом nginx.conf и директорией /etc/nginx/sites-enabled/
```shell
sudo ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/
```

Запуск LDAP сервера
```
docker run --detach --rm --name openldap \
  --network my-network \
  --env LDAP_ADMIN_USERNAME=admin \
  --env LDAP_ADMIN_PASSWORD=adminpassword \
  --env LDAP_USERS=customuser \
  --env LDAP_PASSWORDS=custompassword \
  --env LDAP_ROOT=dc=example,dc=org \
  --env LDAP_ADMIN_DN=cn=admin,dc=example,dc=org \
  bitnami/openldap:latest
```
