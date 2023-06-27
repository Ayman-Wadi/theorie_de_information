
<h1 align="center">
  <br>
<img src="https://cdn.discordapp.com/attachments/1122367085260062880/1123021349691068666/ensa_logo.png" alt="ENSA TANGER" width="200"></a>
  <br>
  <br>
 Travaux pratiques de la théorie de l'information
</h1>
<h3 align="center">	
Un travail de : Ayman Wadi 
<br>Encadré par : Mme Siham Massou.
</h3>

<p align="center"> <br>
	Ce répertoire contient mes codes Python pour l'apprentissage de la programmation avec Mme Massou. Vous y trouverez différents fichiers, tels que des scripts, des données, et des notes de cours. J'ai créé ce répertoire sur GitHub pour sauvegarder mes codes en toute sécurité et pour les partager avec d'autres développeurs. N'hésitez pas à me contacter pour toute question ou suggestion d'amélioration.
<br>
Merci de visiter mon répertoire GitHub !
<br>
Ceci est mon <a href="https://www.linkedin.com/in/ayman-wadi/" target="_blank">LinkedIn</a>.
</p>


<p align="center">
  <a>
	<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  </a>
  <a>
	<img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=green&labelColor=green">
  </a>
  <a>
	<img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)">
  </a>
  <a>
	<img src="https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white">
  </a>
</p>

<p align="center">
  <a href="#Introduction">Introduction</a>
	<br>
  <a href="#Arithmétique flottante">Arithmetique flottante</a> •
  <a href="#Hamming">Codage Hamming</a> •
  <a href="#Huffman">Codage Huffman</a> •
  <a href="#LZ78">Codage LZ78</a> •
  <a href="#Shannon Fano">Cadage Shannon Fano</a>
</p>

<p align="center">
<img  src="https://media.tenor.com/GfSX-u7VGM4AAAAC/coding.gif" alt="Coding">
</p>

## Introduction

<p>La théorie de l'information est une branche des mathématiques appliquées qui étudie la quantité d'information contenue dans des données et les méthodes de traitement, de transmission et de stockage de l'information. Elle a été développée par Claude Shannon en 1948, mais a des racines plus anciennes dans la théorie de la communication et la statistique.</p>
<p>La théorie de l'information traite de plusieurs concepts fondamentaux, notamment :
	
 - L'entropie : mesure de la quantité de désordre dans un système d'informations.
 - Le canal de communication : le moyen par lequel l'information est transmise d'un point à un autre, souvent soumis à des perturbations et des bruits.
 - Le codage de l'information : la représentation de l'information sous une forme qui peut être stockée, transmise et traitée efficacement.
</p>
<p>La théorie de l'information est utilisée dans de nombreux domaines, notamment la communication, la cryptographie, la compression de données, la reconnaissance de formes et l'apprentissage automatique. Elle est également utilisée dans des applications pratiques telles que la transmission de signaux sans fil, la compression de fichiers multimédias, la correction d'erreurs dans les transmissions numériques, etc.</p>
<p>En résumé, la théorie de l'information fournit un cadre mathématique pour comprendre et quantifier l'information, ce qui est essentiel pour la conception et l'optimisation de systèmes d'informations efficaces et fiables.</p>
<p align="center">
<img  src="https://cdn.discordapp.com/attachments/1122367085260062880/1123234277933465611/rsz_shannon-1200x630-1.jpg" alt="Coding"> <br>
<em> Claude Shannon avec une machine de codage trés développée en 1950 </em>
</p>
<br>
<br>


## Arithmétique flottante

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
Soit bornelnf ← 0.0
Soit borneSup ←	1.0
Tant que il y a des symboles à coder Faire
  C ← symbole à coder
  Soient x, y les bornes de l'intervalle correspondant à C dans la table
  taille ← borneSup — bornelnf;
  borneSup ← bornelnf + taille * y
  bornelnf ← bornelnf + taille * x
Fin Tant que
Retourner borneSup
```

> **Note**
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.


## Download

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## Emailware

Markdownify is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <bullredeyes@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [Electron](http://electron.atom.io/)
- [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)
- [showdown](http://showdownjs.github.io/showdown/)
- [CodeMirror](http://codemirror.net/)
- Emojis are taken from [here](https://github.com/arvida/emoji-cheat-sheet.com)
- [highlight.js](https://highlightjs.org/)

## Related

[markdownify-web](https://github.com/amitmerchant1990/markdownify-web) - Web version of Markdownify

## Support

<a href="https://www.buymeacoffee.com/5Zn8Xh3l9" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)

