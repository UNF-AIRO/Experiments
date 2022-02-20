##########################################################
#       install-packages.sh
#       
#       This script is designed to be use as a testing 
#       tool for experimenting such as installing 
#       dependencies, 
#       
#       NOTE: Please note, that this script always changes. 
#
#
##########################################################


function initialize-packages {
        pacman -Sy
}

function update-packages {
        pacman -Syyu
}

function install-packages {
        pacman -S git                   ## Install git
        pacman -S php                   ## Install php
        pacman -S python                ## Install python
        pacman -S npm                   ## Install npm
}

function install-dependencies {
        ## Later 
}


function install-repositories {
        git clone https://github.com/UNF-AIRO/Experiments
}


initialize-packages
update-packages