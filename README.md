# Calendrier de l'Avent musical :

Ce calendrier de l'Avent utlise un ESp32-TTGO-T-Display permettant d'alimenter un circuit sur lequel 2 circuits intégrés CD4511 sont couplés à un circuit intégré CD40106 pour allumé aléatoirement 24 leds et jouer des musiques de Noël.
Les leds sont placé sur un plateau en bois décoré de 23 maisonnettes et une église simulants les 24 jours avant le jour de Noël).
Le déclenchement des musiques et de l'éclairage par clignottement aléatoire est défini selon la date et l'heure, tous les jours à 18h30 l'éclairage s'allume et il s'éteind automatiquement à 22h, il est toutefois possible d'allumer ou d'éteindre manuellement ces fonctions à l'aide de bouton sensitif.
Lors de l'appui sur un jour souhaité sur la partie NOEL de la décoration, la led relié s'illumine avec plus d'intensité pour repérer facilement la maisonnette correspondante.

# Firmware Micropython :
Le firmware utilisé est Micropython, disponible dans le répertoire [Firmware](https://github.com/Francois25/Calendrier_avent_musical/tree/main/firmware)

# Fonctionnement :
L'ESP32 est alimenté via une batterie 5V. Les pin 2 et 15 de l'ESP sont utilisés en tant que touch-pin, lorsque la pin 2 est touchée par l'utilisateur le circuit intégré CD4511 est alors alimenté et gènère un alumage aléatoire des 24 leds des maisonnettes via les circuits intégrés CD40106 (12 led par circuit). Lorsque la pin 15 est touchée l'ESP choisi au hasard une musique de la bibliothère des musiques de Noël et la diffuse sur le buzzer. Pendant ce temps, il n'est pas possible d'éteindre les lumières qui clignottent aléatoirement.
Lors de l'appui sur un bouton date, celui-ci étant relié à la borne 5V de l'ESP32 la led 12V associée s'illumine avec une intensité plus importante, ce qui permet de repèrer facilement la maisonnette associée.
Le module datetime permet d'utiliser la date et l'heure souhaitée pour alumer ou éteindre les lumières ainsi que jouer des musique via le buzzer.
Aucune librairies supplémentaire n'est nécessaire au bon fontionnement.

# Suppléments :
Tous les fichiers destinés à la fabrication des maisonnettes et de l'églises sont disponibles dans le répertoire [CNC_program](https://github.com/Francois25/Calendrier_avent_musical/tree/main/Doc/CNC_program)
Les fichiers destinés à la réalisation du PCB, les composants utilisé ainsi que le cablage sont disponibles dans le répertoire [Electronic](https://github.com/Francois25/Calendrier_avent_musical/tree/main/Doc/Electronic)
Les fichiers destinés à la réalisation du boitier recevant l'électronique et du cloché de l'église sont disponibles dans le répertoire [3D_stl](https://github.com/Francois25/Calendrier_avent_musical/tree/main/Doc/3D_stl)

# Remerciement :
Un merci tout particulier à Monsieur Jacky BEURET. J'ai utilisé et étoffé son circuit de base trouvé par hasard sur internet. [Jeu de lumière aléatoire](http://www.electronique-3d.fr/Jeu_de_lumiere_aleatoire.html). N'hésitez pas à jetter un oeil à son site il y a plein de chose à se bricoler.
Adresse du site de M. BEURET : [CLIC](http://www.electronique-3d.fr/index.html) , [Facebook](https://www.facebook.com/profile.php?id=100054204263511)
