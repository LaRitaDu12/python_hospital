# python_hospital

## Django

### SetUp


1. The first thing to do is to clone the repository

```sh
$ git clone https://github.com/LaRitaDu12/python_hospital.git
$ cd python_hospital
```

2. Create a virtual environment to install dependencies
 
```sh
$ pyenv install 3.10
$ pyenv virtualenv 3.10 .env
$ source .env/bin/activate
```

3. Then install the dependencies

```sh
(.env)$ pip install -r requirements.txt
```

4. Once 'pip' has finished downloading the dependencies

```sh
(.env)$ cd python_hospital
(.env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


### Walkthrough

#### Welcome page, Who are we, What we do

Ces pages permettent de recontextualiser notre travail afin d'avoir une meilleure compréhension de notre travail. 
Elle permet à n'importe quelle personne de comprendre ce que l'on a fait, comment et pourquoi.

#### Dataviz

On peut trouver sur cette page la liste des différentes visualisations. Les visualistations ont été séparé en 3 categories :
	- Quelques informations
	- Comprendre le dataset
	- L'impact de l'HbA1c
	
En cliquant sur une visualisation, vous pourrez accéder à toutes les informations la concernant.

#### Models

On peut y trouver l'historique des prédictions effectuées. Pour des soucis de simplicité, le formulaire se trouve dans la page admin du projet
(car le nombre de features était trop grand)

#### Page admin

L'utilisateur peut accéder à la page admin par le bouton `Login` en haut à droite.
Pour des soucis de sécurité, nous ne donnerons pas accès à cette page. Sachez que c'est à travers cette page que l'on a pu créer
des visualisations et des prédictions.

