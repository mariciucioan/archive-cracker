
  
    
# archive-cracker      
## EN 
#### Introduction      
 This repository contains my Python3 class project.      
      
| Name | Zipspy |      
|--|--|      
| Author | [Mariciuc Ioan (@mariciucioan)](https://github.com/mariciucioan/)      
| Python Version | [Python 3.9](https://docs.python.org/3.9/) |      
| Supports | **.ZIP** files |    
  
#### Frameworks  
  
| Framework | Used for |  
|--|--|  
| [Kivy](https://kivy.org/#home) | Graphical User Interface |   
| [plyer](https://pypi.org/project/plyer/) | File chooser for GUI app |  
| [termcolor](https://pypi.org/project/termcolor/) | Terminal colors |  
| [pyzipper](https://pypi.org/project/pyzipper/) | Working with zip files |  
| [tqdm](https://tqdm.github.io/) | Progress bar |  
      
#### Requirements 
> Write a tool that receives as parameters a ZIP archive and searches for its password. The password must be alphanumeric and must have a maximum length of 10 characters. **It must not use extern tools**.   
#### Approach   
 | Goal | Technologies/Details |      
| -- | -- |      
|☑ Create a graphic user interface (GUI)| [Kivy](https://kivy.org/#home) |      
|☑ Implement the cracking algorithm | [Dictionary](https://www.tech-faq.com/dictionary-attack.html) & [Brute Force](https://www.tech-faq.com/brute-force-attack.html) Attacks |      
|☑ Implement testing| [unittest](https://docs.python.org/3/library/unittest.html) |  
  
#### Accuracy and performance  
  
 - Dictionary attacks are faster and can break common passwords and do not grant finding the password;  
 - Brute attacks are slower but grant 100% accuracy for alphanumerical passwords with length <= 10. For a better performance we can make use of multi-threading.  
  
#### To do  
  
 - [x] Connect the GUI app to the scripts and make it functional.  
 - [ ] ~~Make a portable version of the GUI app.~~ <- built application is too big to even care about that.  
 - [ ] For the GUI app make the password cracking run in different thread so the GUI app won't get 'not responding'.  
 - [x] Check if the archive has a password.  
  
      
## RO 
#### Introducere      
 Acest repository contine proiectul pentru laboratorul de Python3.      
      
| Nume | Zipspy |      
|--|--|      
| Autor | [Mariciuc Ioan (@mariciucioan)](https://github.com/mariciucioan/)      
| Versiune Python | [Python 3.9](https://docs.python.org/3.9/) |      
| Extensii suportate| **.ZIP** files      
  
#### Frameworks  
  
| Framework | Folosit pentru|  
|--|--|  
| [Kivy](https://kivy.org/#home) | Interfata grafica |   
| [plyer](https://pypi.org/project/plyer/) | File chooser pentru aplicatia grafica |  
| [termcolor](https://pypi.org/project/termcolor/) | Culori in terminal |  
| [pyzipper](https://pypi.org/project/pyzipper/) | Lucru cu fisierele .zip |  
| [tqdm](https://tqdm.github.io/) | Bara de progres |  
      
#### Cerinta 
> Scrieti un tool care primeste ca paramtru o arhiva parolata ZIP si care ghiceste parola arhivei. Parola va fi alfanumerica si va avea maxim 10 caractere. **Nu se pot folosi tool-uri externe**. 

 #### Mod de abordare   
 | Scop | Tehnologii/Detalii |      
|--|--|      
|☑ Crearea unei interfete grafice pentru utilizator| [Kivy](https://kivy.org/#home) |      
|☑ Implementarea algoritmului pentru spargerea parolei| [Dictionary](https://www.tech-faq.com/dictionary-attack.html) & [Brute Force](https://www.tech-faq.com/brute-force-attack.html) Attacks |      
|☑ Implementarea testelor| [unittest](https://docs.python.org/3/library/unittest.html) |  
  
#### Acuratete si performanta  
  
 - Atacurile de tip "Dictionary Attacks" sunt mai rapide, insa nu garanteaza 100% gasirea parolei. Acest tip de atac verifica parolele intalnite in mod comun.  
 - Atacurile de tip "Brute Force Attack" sunt mai incete, insa garanteaza 100% acuratete in gasirea parolelor alfanumerice mai scurte sau egale cu 10 caractere. Pentru o performanta mai buna cautarea parole s-a facut ajutandu-ma de multi-threading.  
  
#### To do  
  
 - [x] Comunicare intre GUI app si scripturi.  
 - [ ] ~~Construirea unui executabil portabil pentru aplicatia grafica.~~ <- aplicatia e prea mare si nu merita.  
 - [ ] Pentru aplicatia grafica algoritmul pentru gasirea parolei trebuie sa fie facut sa ruleze pe alt thread pentru a nu primit 'not responding'.  
 - [x] Verifica daca fisierul are parola sau nu.  
  
  
## IMAGES  
  
### Terminal side  
![Terminal-1](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-1.PNG?raw=true)  
![Terminal-2](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-2.PNG?raw=true)  
  
##  
  
### GUI side  
![GUI-1](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-gui-1.PNG?raw=true)  
![GUI-2](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-gui-2-1.PNG?raw=true)  
![GUI-3](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-2-2.PNG?raw=true)  
![GUI-4](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-3.PNG?raw=true)  
![GUI-5](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-4.PNG?raw=true)  
![GUI-6](https://github.com/mariciucioan/archive-cracker/blob/main/resources/images/zipspy-pics/zipspy-5.PNG?raw=true)
