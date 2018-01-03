# ACMWebSite
WebSite 2.0 for ACM develop by the Javerian Chapter

## Developers
- Backend - [Johan Sebastian Murillo Castillo](https://github.com/johan-smc)
- Backend - [Juan Pablo Rodriguez Navarro](https://github.com/JuanPabloRN30)
- Frontend - [Juan Manuel Sánchez Lozano](https://github.com/juanmsl)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Python
You must have installed python3 on your pc, to install it on Windows you can download python from their [webpage](https://www.python.org/downloads/), or, if you are in Linux, probably you have it already.

```shell
$ python3 --version
Python 3.6.4
```

If you haven't python installed you can install it

```shell
$ sudo apt install python3.6
```

#### Node (npm)

Furthermore you must have node.js on your computer, you can download it from their [webpage](https://nodejs.org/en/download/), and you can install it in [different architectures](https://nodejs.org/es/download/package-manager/).

When you have installed node you can check your version
```shell
$ npm --version
3.10.10
```

When you have installed `npm`, install `gulp` and `yarn`
```shell
$ npm install -g gulp yarn
```

After install the packagues, check it in your system
```shell
$ gulp -version
CLI version 3.9.1

$ yarn -version
1.3.2
```

### Installing
1. Clone this repository, or download the zip project to your pc

	```shell
	$ git clone https://github.com/CapituloJaverianoACM/ACMWebSite.git
	```
1. Create a virtual environment if you want

	#### Creating the virtual environment
	We gonna use `myvenv` as the name of the virtual environment, but you can use the name that you prefer.
	
	```shell
	$ python3 -m venv myvenv
	```
	
	#### Activating the virtual environment
	
	On windows
	
	```shell
	$ .\myvenv\Scripts\activate
	```

	On Linux or Mac
	
	```shell
	$ source ./myvenv/bin/activate
	```

	After activate your virtual environment your command line prompt should look like this
	
	```shell
	(myvenv) $
	```

1. Install the requirements

	Install the python packages described in the `requirements.txt`, and node packages described in the `package.json`
	
	```shell
	$ npm run requirements
	```

1. Migrate the database

	```shell
	$ npm run migrate
	```

1. Running the server
	
	```shell
	$ npm start
	```
	
	After starting your local server you can test the webpage on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Licence
This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/CapituloJaverianoACM/ACMWebSite/blob/master/LICENSE) file for details
