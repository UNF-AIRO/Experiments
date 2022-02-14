# Arch-Linux-Custom-Installer

#### Introduction

This folder contains shell scripts that will be used as the automatic installation of Arch Linux as a backend that will be deployed on the server. The customized setup of Arch Linux will contain the projects that is made by UNF-AIRO. 

This folder is an experiment that will be used for developing and testing the scripts, before it is deployed to the AIRO-Arch-Linux-Installer Repository. 

#### Running the script

Once you have downloaded the latest version of Arch Linux, then put this command: 



Obtain the  packages on the live environment

```shell
pacman -Sy
```



Install git

```shell
pacman -S git
```



Clone the repository into the live environment

```shell
git clone https://github.com/UNF-AIRO/Experiments/
```



Change directory to Experiments

```shell
cd Experiments
```



Go to Arch-Linux-Custom-Installer folder 

```shell
cd Arch-Linux-Custom-Installer
```





Run the script

```shell
sh install.sh
```
