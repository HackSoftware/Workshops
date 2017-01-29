## Pre install some dependencies:
```
sudo apt-get install python-virtualenv
```

## nginx:

Install nginx:

```
sudo apt-get install nginx
sudo service nginx start
```

## Install postgresql

```
sudo apt-get install postgresql postgresql-server-dev-9.3
sudo pg_createcluster 9.3 main
sudo service postgresql start
```
If `pg_createcluster` fails do the following:

```
export LC_ALL="en_US.UTF-8"
```

## Create `user` that will execute the python code

```
adduser hack
```

### Add your keys to the hack usre
```
su hack
cd /home/hack
mkdir .shh
chmod 700 ~/.ssh # Only hack can write and read there
cd .ssh
vi authorized_keys # Paste public key in here
chmod 600 authorized_keys
```
More information about the permissions in linux https://wiki.archlinux.org/index.php/File_permissions_and_attributes

## Create folder for the project & virtual environment

```
mkdir hack
chown hack:hack -R hack/ # Give ownership to the hack user
```

**Important** Do everything esle as the hack user

```
./install_os_dependencies.sh install # **Important note** Install os requirements as `root this will install all the required os dependences
su hack
cd /hack
mkdir hack33
cd hack33
virtualenv -p /usr/bin/python3 env
source env/bin/activate
mkdir current # Create project's folder
cd current
git clone https://github.com/pgergov/hack33.git .
pip install -r requirements/production.txt
```

## Set env variables

```
vi /etc/environment  # Paste your environments here
```

## Create postgres user & db

**Important note** Run the next commands as root

```
sudo -u postgres createuser hack
sudo -u postgres createdb -O hack hack33
```

**Important note** ssh again as hack so that env variables are recongnized!

## Run migrations

```
python manage.py migrate
```

### check your work

```
python manage.py runserver 0.0.0.0:8000
```

## Setup gunicorn

**Important note** You won't be able to access it from outside

```
gunicorn config.wsgi:application
```

## Setup upstart job that's gona keep the gunicorn up

**Important note** Execute the next commands as `root`

```
cd /etc/init/
vi hack33.conf # paste the upstart config from the repo  
start hack33
```

## Setup nginx

**Important note** Run the following commands as `root`
```
cd /etc/nginx/sites-enabled
rm default
vi hack33 # paste the nginx config from this repo
sudo service nginx restart
```
