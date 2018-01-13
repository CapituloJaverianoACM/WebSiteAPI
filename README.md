# ACMWebSite
WebSite 2.0 for ACM develop by the Javerian Chapter

- [Contributors](#contributors)
- [Prerequisites](#prerequisites)
	- [Python](#python)
	- [Node (npm)](#node-npm)
- [Installing](#installing)
	- [Clone the repository](#clone-the-repository)
	- [Create a virtual environment (This step is optional)](#create-a-virtual-environment-this-step-is-optional)
	- [Install the requirements](#install-the-requirements)
	- [Migrate the database](#migrate-the-database)
- [Running the project](#running-the-project)
	- [1. Running django server](#1-running-django-server)
	- [2. Compile frontend frameworks to generate the static content](#2-compile-frontend-frameworks-to-generate-the-static-content)
- [Licence](#licence)

## Contributors
| Name                             | GitHub                                            | Rol                |
| -------------------------------- | ------------------------------------------------- | ------------------ |
| Johan Sebastian Murillo Castillo | [johan-smc](https://github.com/johan-smc)         | Backend developer  |
| Juan Pablo Rodriguez Navarro     | [JuanPabloRN30](https://github.com/JuanPabloRN30) | Backend developer  |
| Juan Manuel Sánchez Lozano       | [juanmsl](https://github.com/juanmsl)             | Frontend developer |


## Prerequisites

### Python
You must have installed python3 on your pc, to install it on Windows you can download python from their [webpage](https://www.python.org/downloads/), or, if you are in Linux, probably you have it already.


```shell
$ python3 --version
Python 3.6.4
```

If you haven't python installed you can install it

```shell
$ sudo apt install python3.6
```

### Node (npm)

Furthermore you must have node.js on your computer, you can download it from their [webpage](https://nodejs.org/en/download/), or just run the following command

```shell
$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

> When you have installed node you can check your version
```shell
$ npm --version
3.10.10
```

When you have installed `npm`, install `gulp` and `yarn`
```shell
$ npm install -g gulp yarn
```

> After install the packages, check it in your system
```shell
$ gulp -version
CLI version 3.9.1
$ yarn -version
1.3.2
```

## Installing
### Clone the repository

```shell
$ git clone https://github.com/CapituloJaverianoACM/ACMWebSite.git
```

### Create a virtual environment (This step is optional)

#### Creating the virtual environment

We gonna use `myvenv` as the name of the virtual environment, but you can use the name that you prefer.

```shell
$ python3 -m venv myvenv
```

#### Activating the virtual environment

```shell
# On windows
$ .\myvenv\Scripts\activate

# On Linux or Mac
$ source ./myvenv/bin/activate
```

> After activate your virtual environment your command line prompt should look like this

```shell
(myvenv) $
```

### Install the requirements

Install the python packages described in the `requirements.txt`, and node packages described in the `package.json`

```shell
$ npm run requirements
```

### Migrate the database

```shell
$ python3 manage.py migrate
```

## Running the project
### 1. Running django server

```shell
$ npm start
```

> After starting your local server you can test the webpage on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 2. Compile frontend frameworks to generate the static content
	
To generate the `static`, and `templates` folders you only need to start the development mode of project, it render the pages and open the page in a browser

```shell
$ npm run dev
```

> It generate a proxy to django server, to enable the live reload, and open the project on [http://127.0.0.1:3000/](http://127.0.0.1:3000/)

## Licence
This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/CapituloJaverianoACM/ACMWebSite/blob/master/LICENSE) file for details
