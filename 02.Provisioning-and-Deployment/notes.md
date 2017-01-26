#### Start nginx:

```
sudo start nginx start
```

#### Restart nginx:

```
sudo start nginx restart
```

### Install postgresql

#### Create cluster before starting postgres:

```
sudo pg_createcluster 9.3 main
```

#### If `pg_createcluster` fails do the following:

```
export LC_ALL="en_US.UTF-8"
```

#### Actually instal postgresql:

```
sudo apt-get install postgresql
```

#### Start postgres

```
sudo service postgresql start
```

## Create `user` that will execute the python code

```
adduser hack
```

#### Switch from root to hack:

```
su hack
```

#### Go to `/home/hack`

```
mkdir .shh
```

#### Only hack can write and read there

```
chmod 700 ~/.ssh
```

#### Paste your `id_rsa.pub` in `authorized_keys`:

```
vi authorized_keys -> <paste public key in here>
```

```
chmod 600 authorized_keys
```

#### What rights mean:
-------------------------
user | group | all
 100 |  010  | 001

4 - r
2 - w
1 - e
-------------------------

## Create folder for the project & virtual environment

#### ssh as root & create the main folder:

```
mkdir hack
```

#### Give ownership to the hack user:

```
chown hack:hack -R hack/
```

**Important** Do everything esle as the hack user

```
su hack
```

#### Go to the hack directory

```
cd /hack
```

#### Create project folder

```
mkdir hack33
```

#### create virtualenv

**Important none** Do this as root!

```
sudo apt-get install python-virtualenv
```

### Switch to hack & create `env` folder inside `hack33` folder:

#### Create `env` folder:

```
virtualenv -p /usr/bin/python3 env
```

#### Source in the virtual environment:

```
source env/bin/activate
```
#### Create project's folder:

```
mkdir current  
```

```
cd current
```

#### Clone your project:

```
git clone https://github.com/pgergov/hack33.git .  
```

## Install requirements

```
sudo apt-get install postgresql-server-dev-9.3
```

**Important note** Install os requirements as `root`:

```
./install_os_dependencies.sh install
```

#### Be sure to be sourced in the environment before installing python requirements:

```
pip install -r requirements/production.txt
```

## Set env variables

#### Paste your environments here:

```
vi /etc/environment  
```

## Create postgres user & db

**Important note** Run the next commands as root

```
sudo -u postgres createuser hack
```

```
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
```

#### Define your gunicorn upstart job there

```
vi hack33.conf  
```

#### Start the upstart job

```
start hack33
```

## Setup nginx

**Important note** Run the following commands as `root`
```
cd /etc/nginx/sites-enabled
```

#### Delete the default nginx file:

```
rm default  
```

#### Define your nginx configuration here:

```
vi hack33
```

#### Restart nginx

```
sudo service nginx restart
```