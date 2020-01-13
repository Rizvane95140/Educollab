# Educollab

Ce projet est réalisé dans le cadre d'un projet scolaire. Il est codé avec le langage python et le framework Django. 

Le but est de mettre en relation les élèves entre eux afin de se corriger, et d'offrir une plateforme de gestion pour les utilisateurs de l'application en temps que professeurs.

### Installation de l'application 

###### INSTALLATION DE L'ENVIRONNEMENT VIRUTEL (OTIONNEL)
Vous pouvez commencer à installer un environnement virtuel, ou l'utiliser dans votre propre environnement. 

Un de ces deux liens vous guideront dans cet installation : 
(https://virtualenv.pypa.io/en/latest/installation/)
(https://tutorial.djangogirls.org/fr/django_installation/)

###### INSTALLATION DES DÉPANDANCES 

La première étape, après avoir cloné le projet, est d'installer les dépendances du projet via la commande suivante : 

```
pip install -r requirements.txt
```

###### INSTALLATION DE LA BASE DE DONNÉES 

Les dépandances étant installés, il faut ensuite s'occuper de la base de données, en SQL Lite par défaut. Une erreur peut survenir sous MySQL à cause d'un problème de version. Une solution à ce problème sera fourni bientôt. 

Pour installer la base de données, il faut se baser sur les fichiers de migrations. La commande a lancer afin de lancer la migration est donc : 

```
python manage.py migrate
```

ou 

```
./manage.py migrate
```

Après ces installations, le projet devrait se lancer en local via la commande suivante : 

```
./manage.py runserver
```

Il ne faut pas oublier de configurer le fichier ```settings.py``` dans le dossier ```mysite``` avec les informations de la base de données que vous allez utiliser. 

Il est également possible de créer un admin, et accéder à l'administration du site et de créer ensuite ses comptes soit-même. Pour ce faire, vous entrez la commande suivante  : 

```
./manage.py createsuperuser
```

Vous entrez vos données, et votre compte admin est crée.

L'URL vers l'admin :  ```/admin``` qui va vous permettre de créer les comptes étudiants et professeurs. 

La prochaine étape est de créer la base de données.

MCD de l'application (qui changera très certainement, car il manque certaines choses):

![Image de la base de données modélisé](https://i.ibb.co/ZKN2x61/Capture-d-e-cran-2019-10-27-a-16-41-14.png)
