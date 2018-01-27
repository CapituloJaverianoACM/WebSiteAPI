# ACMWebSite
WebSite 2.0 for ACM develop by the Javerian Chapter

- [Contributors](#contributors)
- [Prerequisites](#prerequisites)
	- [Python](#python)
- [Installation](#installation)
	- [Clone the repository](#clone-the-repository)
	- [Create a virtual environment (This step is optional)](#create-a-virtual-environment-this-step-is-optional)
		- [Creating the virtual environment](#creating-the-virtual-environment)
		- [Activating the virtual environment](#activating-the-virtual-environment)
	- [Install the requirements](#install-the-requirements)
	- [Migrate the database](#migrate-the-database)
- [Deployment](#deployment)
	- [1. Build the project](#1-build-the-project)
	- [2. Running django server](#2-running-django-server)
- [Gulp tasks](#gulp-tasks)
- [Licence](#licence)

## Contributors
| Name                             | GitHub                                            | Rol                |
| -------------------------------- | ------------------------------------------------- | ------------------ |
| Johan Sebastian Murillo Castillo | [johan-smc](https://github.com/johan-smc)         | Backend developer  |
| Juan Pablo Rodriguez Navarro     | [JuanPabloRN30](https://github.com/JuanPabloRN30) | Backend developer  |
| Juan Manuel Sánchez Lozano       | [juanmsl](https://github.com/juanmsl)             | Frontend developer |


## Prerequisites

We recommend work on Linux, because it is easier install packages and frameworks; but, if you want to work on Windows you can do it.

### PyEnv

Install:

```shell
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

Install dependencies:

```shell
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev git
```

add this lines in `.bashrc`:

```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

and then Update:

```
$ pyenv update
```

### Python

Install on pyenv

```shell
$ pyenv install 3.6.0
```

Set Python 3.6.0 as global env

```shell
$ pyenv global 3.6.0
```

### Direnv

For handle the environments variables

```shell
$ sudo apt install direnv
```

And add the following line to `.bashrc`

```
eval "$(direnv hook bash)"
```

## Installation
### Clone the repository

```shell
$ git clone https://github.com/CapituloJaverianoACM/WebSiteAPI.git
$ cd ACMWebSite
```

### Create a virtual environment

If you don't want to install the project's requirements on your computer, we are going to create a virtual environment to install them there.

#### Creating the virtual environment

We gonna use `myvenv` as the name of the virtual environment, but you can use the name that you prefer.

```shell
$ pyenv virtualenv <myvenv>
```

#### Activating the virtual environment

```shell
$ pyenv local <myvenv>
```

> After activate your virtual environment your command line prompt should look like this

```shell
(myvenv) $
```

> If you want to exit from your virtual environment just get out of the project folder

### Install the requirements

Install the python packages described in the `requirements.txt`

```shell
$ pip install -r requirements.txt
```

### Migrate the database

```shell
$ python manage.py migrate
```

## Deployment

### 1. Running django server

```shell
$ python manage.py runserver
```

> After starting your local server you can test the webpage on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Licence
This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/CapituloJaverianoACM/ACMWebSite/blob/master/LICENSE) file for details
