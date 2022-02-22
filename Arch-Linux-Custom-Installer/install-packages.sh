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


initializePackages() {
        pacman -Sy
}

updatePackages() {
        pacman -Syyu
}

installPackages() {
        pacman -S git                   ## Install git
        pacman -S php                   ## Install php
        pacman -S python                ## Install python
        pacman -S npm                   ## Install npm
}

installDependencies() {
        echo "lateron"
}


installRepositories() {
        git clone https://github.com/UNF-AIRO/Experiments
}


initializePackages
updatePackages
installPackages
installRepositories
