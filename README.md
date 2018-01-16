# ACMWebSite
WebSite 2.0 for ACM develop by the Javerian Chapter

- [Contributors](#contributors)
- [Prerequisites](#prerequisites)
	- [Python](#python)
	- [Node (npm)](#node-npm)
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

### Python
You must have installed python3 on your pc, so check it.

```shell
$ python3 --version
Python 3.5.2
```

If you haven't python installed you can install it with the command below

```shell
$ sudo apt install python3
```

### Node (npm)

Furthermore you must have `node.js` on your computer, you can download it from their [Webpage](https://nodejs.org/en/download/package-manager/), or just run the following command if you are in a Debian and Ubuntu based Linux distribution

```shell
$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

When you have installed `node.js` you can check your version

```shell
$ node --version
v8.9.4

$ npm --version
5.6.0
```

When you have installed `node.js` with `npm`, install `gulp` and `yarn`

```shell
$ sudo npm install -g gulp
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
$ sudo apt-get update && sudo apt-get install yarn
```

After install the packages, check it in your system
```shell
$ gulp --version
CLI version 3.9.1

$ yarn --version
1.3.2
```

> If you have any problem installing the packages, visit the [Node webpage](https://nodejs.org/en/download/package-manager/), or [Yarn webpage](https://yarnpkg.com/en/docs/install).

## Installation
### Clone the repository

```shell
$ git clone https://github.com/CapituloJaverianoACM/ACMWebSite.git
$ cd ACMWebSite
```

### Create a virtual environment (This step is optional)

If you don't want to install the project's requirements on your computer, we are going to create a virtual environment to install them there.

#### Creating the virtual environment

We gonna use `myvenv` as the name of the virtual environment, but you can use the name that you prefer.

```shell
$ python3 -m venv myvenv
```

#### Activating the virtual environment

```shell
$ source myvenv/bin/activate
```

> After activate your virtual environment your command line prompt should look like this

```shell
(myvenv) $
```

> If you want to exit from your virtual environment just run the command `deactivate` on the console

### Install the requirements

Install the python packages described in the `requirements.txt`, and node packages described in the `package.json`

```shell
$ npm run requirements
$ yarn --prod=false
```

### Migrate the database

```shell
$ python manage.py migrate
```

## Deployment

### 1. Build the project

```shell
$ npm run build
```

### 2. Running django server

```shell
$ npm start
```

> After starting your local server you can test the webpage on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Gulp tasks

This tasks are described in the `gulpfile.babel.js` file, and can help you to work with the project

To run the development mode just run the following command, it start the `default` gulp task.

```shell
$ npm run dev
```

Furthermore there are another task that you can execute them with the command below

```shell
$ gulp <taskname>
```

| Taskname          | Description                                            |
| ----------------- | ------------------------------------------------------ |
| build:styles      | Build `styles.css` file from the `.scss` files         |
| build:html        | Build `html` file pages from the `.pug` files          |
| build:scripts     | Build `bundle.js` file from the `.js` files            |
| build:fonts       | Copy all fonts in `dev` folder to the `static` folder  |
| build:images      | Copy all images in `dev` folder to the `static` folder |
| generate:todolist | Generate the todolist and the fixmelist of the project |
| clean             | Clean the project of all the generated files           |
| build             | Execute all `build:` tasks                             |
| clean:build       | Clean the project and after that build it              |

## Licence
This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/CapituloJaverianoACM/ACMWebSite/blob/master/LICENSE) file for details
