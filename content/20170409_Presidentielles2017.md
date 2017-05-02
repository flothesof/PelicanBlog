Title: Une application Android pour s'informer sur les programmes électoraux 2017
date: 2017-04-09 15:12
comments: true
slug: presidentielles-2017
Tags: Politique
Category: Python
Summary: Les programmes des candidats pour la présidentielle 2017 sont complexes. Pour les explorer, je propose une application Android sous forme de quizz.

# Contexte

L'[élection présidentielle 2017](https://fr.wikipedia.org/wiki/%C3%89lection_pr%C3%A9sidentielle_fran%C3%A7aise_de_2017) voit s'affronter 11 candidats. Leurs programmes sont, de manière générale, complexes. Afin d'explorer ces programmes, je propose une démarche ludique sous forme de quizz. Ceci s'appuie sur le fait que la plupart des candidats structurent leurs propositions sous la forme d'une liste d'actions. 

# Exploration interactive avec Jupyter et mybinder.org

Dans un premier temps, j'ai *parsé* le contenu HTML des sites de campagne de six candidats. Ceci m'a permis d'en extraire une liste de propositions pour chacun d'entre eux. 
Ces listes de propositions sont hébergées de manière ouverte sur le repo github suivant : <https://github.com/flothesof/presidentielles2017>.
A l'aide des outils interactifs Jupyter/Python j'ai ensuite mis en ligne une interface graphique accessible à travers de la plateforme mybinder.org. Pour l'utiliser, il suffit de cliquer sur le lien suivant : <http://mybinder.org/repo/flothesof/presidentielles2017>. 

Un aperçu de l'interface graphique est disponible ci-dessous : 
![Alt Text]({filename}/images/presidentielles2017_mybinder.png)

# Une application Android

Avec l'encouragement de mon entourage, je me suis également lancé dans l'écriture d'une application Android autour des mêmes données. Celle-ci est également open-source sur github : <https://github.com/flothesof/presidentielles2017-android>.

Elle propose le même principe avec quelques améliorations (un tirage au sort des questions un peu plus équilibré notamment). Vous pouvez la télécharger gratuitement (et sans publicité) sur le play store : <https://play.google.com/store/apps/details?id=com.frolianlb.presidentielles2017&hl=en>.

![Alt Text]({filename}/images/presidentielles2017_play_store.png)

# Et maintenant ?

A quelques jours de la présidentielle, vous pouvez donc utiliser les deux outils décrits ci-dessous pour prendre connaissance de manière ludique (et assez aléatoire) des propositions des candidats. 

Tous les candidats ? Malheureusement, non. Etant donné que je fais ceci sur mon temps libre, je n'ai pu intégrer que les programmes de six candidats à l'application (JLM, BH, EM, FF, NDA, MLP). Les outils ci-dessus sont en open-source, et permettraient donc à une personne intéressée de rajouter les contenus des cinq autres candidats. 