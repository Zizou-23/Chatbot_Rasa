README.md — Structure recommandée
1. COMCEPTION d'un ChatBot Simple
Notre projet se nomme "ChatBot_Rasa"
	Description expliquant l’objectif du projet
Ce projet consiste en la création d'un chatbot intelligent capable d'interagir avec les utilisateurs en langage naturel. 
Il est développé avec Rasa et permet d'effectuer diverses actions telles que :

Répondre aux questions courantes 
Effectuer des calculs mathématiques 
Fournir des informations sur divers sujets 
Gérer des scénarios de conversation interactifs 
L'objectif principal est de créer un assistant capable de comprendre et de répondre 
aux utilisateurs avec précision et pertinence tout en offrant une expérience fluide et intuitive. 



2. Liste des membres du groupe

Equipe1:Gestion du traitement du langage naturel (NLP) et de l'entraînement du chatbot
KPAKATIA Abdoul Aziz
HOUSSOU Ryann

Equipe2:Développement de l'interface Tkinter, intégration de ChatGPT via l’API OpenAI  
TIANDO Sottima Herman
AGO Immaculée

Gestion des erreurs techniques: Travail commun des deux équipes


3. Introduction

Aujourd’hui, l’intelligence artificielle joue un rôle de plus en plus important dans l’interaction homme-machine. Ce projet vise à développer un chatbot intelligent capable de répondre aux questions des utilisateurs et d’exécuter des tâches spécifiques, comme effectuer des calculs mathématiques ou fournir des informations générales.

L’objectif est d’améliorer l’expérience utilisateur en proposant un assistant conversationnel fluide, intuitif et capable de gérer différentes requêtes de manière autonome. Ce chatbot repose sur Rasa, une plateforme avancée de traitement du langage naturel (NLP), et intègre plusieurs fonctionnalités pour rendre l’échange plus naturel et efficace.

4. Technologies utilisées

Langage de programmation: Python3.10,
Bibliothèque: Rasa version==3.5


5. Installation et Configuration
 Clonage du Projet depuis GitHub
 Prérequis
Avant de cloner le projet, assure-toi d'avoir :

Git installé sur ton ordinateur. 
Un accès à GitHub et aux permissions nécessaires pour cloner le projet.
Python 3.10 et pip installés. 
 Clonage du dépôt
Ouvre un terminal (cmd, PowerShell ou Terminal sur Mac/Linux) et exécute la commande suivante :

# Cloner le projet depuis GitHub
git clone https://github.com/nom-utilisateur/nom-du-projet.git

# Se déplacer dans le dossier du projet
cd nom-du-projet

Configuration des variables d’environnement si nécessaire

6. Guide d’utilisation

 Installation des dépendances
Avant de lancer le projet, installe les bibliothèques nécessaires avec la commande :

pip install -r requirements
 Lancer le chatbot
Démarrer le serveur Rasa
rasa run


démarrer le serveur d'action
rasa run actions

 Tester le chatbot
Exécuter l’interface de discussion
Une fois que le chatbot est en cours d’exécution, tu peux lui poser des questions comme :

"Bonjour"
"Qui es-tu ?"
"Fais-moi un calcul : 25 + 30"


7. Rapport détaillé 
	Semaine 1 : Recherche et Documentation
Nous avons consacré la première semaine à **nous renseigner sur le NLP** et à explorer les bibliothèques disponibles, notamment ChatterBot et Rasa. Nous avons analysé leur documentation et testé quelques exemples pour mieux comprendre leur fonctionnement.

	Semaine 2 : Tentative avec ChatterBot et passage à Rasa**
Nous avons commencé notre projet avec **ChatterBot**, mais nous avons rencontré de nombreux **problèmes de compatibilité de version**. Malgré plusieurs tentatives d'installation sur différentes machines des membres du groupe, nous n'avons pas pu le faire fonctionner correctement. 

Face à ces difficultés, nous avons décidé de **nous concentrer sur Rasa**, dont l'installation était plus simple et mieux documentée. Nous avons donc passé le **troisième tiers de la deuxième semaine** et **deux jours de la troisième semaine** à comprendre la structure du projet Rasa, en nous familiarisant avec les fichiers **NLU, rules, stories, domain**, et d'autres éléments essentiels pour permettre un dialogue fluide.

 	Semaine 3 : Entraînement initial et tentative d'intégration de ChatGPT**
Après avoir assimilé les bases de Rasa, nous avons commencé les **premiers entraînements du modèle**. Pour rendre notre chatbot plus puissant, nous avons tenté d'intégrer **l’API OpenAI de ChatGPT** afin de renforcer la qualité des réponses.

Cependant, nous avons rencontré des **problèmes de compatibilité liés à l’API**. Après plusieurs jours à corriger les erreurs et à tester différentes approches, nous n’avons pas réussi à stabiliser cette fonctionnalité. Nous avons donc décidé de **mettre cette option de côté** et de nous concentrer sur l'entraînement du **noyau Rasa (Rasa Core)**.

 	Semaine 4 : Entraînement final et gestion des conflits Git**
L'entraînement du modèle Rasa a occupé la fin de la troisième semaine et le début de la quatrième semaine. Parallèlement, nous avons essayé de **mettre le projet sur GitHub** pour permettre à chaque membre du groupe de travailler sur différentes branches.

Cependant, nous avons rencontré des **erreurs de compatibilité entre les fichiers stories, rules, NLU et domain** lors de la fusion des branches. Ces conflits empêchaient l’entraînement du chatbot, car la commande de validation des données retournait des erreurs.

Face à ces difficultés, nous avons décidé de **terminer complètement le projet avant de le déposer sur un autre dépôt Git**, afin d’éviter ces problèmes de fusion et de validation des fichiers.

---

  Résultats et Enseignements

 Compréhension approfondie de Rasa et de ses composants (NLU, Rules, Stories, Domain).  
 Expérience sur la gestion des conflits Git et l'organisation du travail en équipe.  
 Problèmes de compatibilité avec OpenAI n'ayant pas pu être résolus.  
 Difficultés à synchroniser les fichiers sur GitHub sans affecter l'entraînement du modèle.

Malgré ces défis, nous avons pu **finaliser un chatbot fonctionnel avec Rasa** et acquérir une expérience précieuse en gestion de projet et en développement IA.

---8. Documentation complémentaire
La documentation sur rasa : https://rasa.com/docs/rasa/
Pour la correction et l'explication de certaines erreur dans le code et l'explication de certaines notions: Chatgpt.com

9. Problèmes rencontrés 
Problèmes de compatibilité avec OpenAI n'ayant pas pu être résolus.  
 Difficultés à synchroniser les fichiers sur GitHub sans affecter l'entraînement du modèle.

les captures d'écran des interfaces du projet se trouvent dans le dossier "images"

10.Compétence du chatbot

Voici la liste des questions simple auxquels notre chatbot est en mesure de répondre et la liste des intentions que nous lui avont enseigné:

Questions de base :
Greet (salutations) :

Bonjour !
Salut, comment ça va ?
Coucou !
Goodbye (au revoir) :

Au revoir !
À bientôt !
Passe une bonne journée !
Bot Challenge (question sur le bot) :

Es-tu un humain ?
Qui t'a créé ?
Que peux-tu faire ?
Questions spécifiques :
Ask Weather (météo) :

Quel temps fait-il ?
Peux-tu me donner la météo ?
Quel temps fera-t-il à [location] ?
Ask Time (heure) :

Quelle heure est-il ?
Peux-tu me donner l'heure ?
Est-ce que le bus arrive bientôt ?
Ask Joke (blague) :

Raconte-moi une blague.
Peux-tu me faire rire ?
Dis quelque chose de drôle !
Ask About Bot (sur le bot) :

Qui es-tu ?
Que sais-tu faire ?
Quelle est ta mission ?
Ask Help (aide) :

Que peux-tu faire ?
Comment tu fonctionnes ?
J’ai besoin d’aide.
Questions liées à la commande de nourriture :
Order Pizza (commande de pizza) :

Je veux une pizza.
Peux-tu m'aider à commander une pizza ?
Je voudrais une pizza grande.
Add Drink (boisson) :

Ajoute une boisson à ma commande.
Je voudrais un coca avec ma pizza.
Je n’ai pas besoin de boisson.
Questions liées au transport :
Bus Schedule (horaires de bus) :
À quelle heure passe le bus ?
Quel est le prochain horaire de la ligne [bus_line] ?
Les bus passent à quelle heure ici ?



Interaction utilisateur (formulaires) :

Provide Name (donner son nom) :

Je m'appelle [nom].
Mon nom est [nom].

Provide Info (informations générales) :

J'ai 25 ans.
Je viens de [location].


Calculs mathématiques :

Perform Calculation (calculs) :
Peux-tu faire un calcul pour moi ?
Combien font 15 + 20 ?
Calcule 50 divisé par 5.


Liste complète des intents disponibles :

greet : Saluer le bot.
goodbye : Dire au revoir.
affirm : Répondre par l'affirmative.
deny : Répondre par la négative.
bot_challenge : Poser une question au sujet du bot.
ask_weather : Poser une question sur la météo.
ask_time : Demander l'heure ou un horaire.
ask_joke : Demander une blague.
ask_about_bot : Demander des informations sur le bot.
ask_help : Demander de l'aide.
provide_name : Donner un nom.
provide_info : Donner des informations personnelles.
ask_pizza : Commander une pizza.
ask_drink : Ajouter une boisson à une commande.
provide_location : Donner une localisation.
provide_pizza_size : Spécifier une taille de pizza.
ask_bus_schedule : Poser des questions sur les horaires de bus.
perform_calculation : Demander au bot de faire un calcul.
