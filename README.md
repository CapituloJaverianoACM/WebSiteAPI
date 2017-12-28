# ACMWebSite
WebSite 2.0 for ACM

## Creating the environment and setup the project

### How to create your virtual environment (This step is optional, only if you dont want to install the project requirements diretly into your own computer)
```shell
$path-of-project> python3 -m venv <virtual-environment-name>
```

### How to activate your virtual environment (This step is only if you create previously your virtual environment)

> On windows
```shell
$path-of-project> "./<vitual-environment-name>/Scripts/activate"
```

> On Linux or Mac
```shell
$path-of-project> source ./<vitual-environment-name>/bin/activate
```

After activate your virtual environment your command line prompt should look like this
```shell
(<vitual-environment-name>) $path-of-project>
```

### Intalling the requirements
```shell
pip install -U -r .\requirements.txt
```
