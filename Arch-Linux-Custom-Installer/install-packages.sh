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
        sudo pacman -Sy
}

updatePackages() {
       sudo pacman -Syyu
}

installPackages() {
        sudo pacman -S git                   ## Install git
        sudo pacman -S php                   ## Install php
        sudo pacman -S python                ## Install python
        sudo pacman -S npm                   ## Install npm
}

installDependencies() {
        echo "lateron"
}


installRepositories() {
        git clone https://github.com/UNF-AIRO/Experiments
}


initializePackages
updatePackages
installDependencies
installPackages
installRepositories
