##############################################################################
#	install.sh 
#	This automated script which automates the installation 
# 	of firn to make it easier
#
##############################################################################






## Source: [https://github.com/theiceshelf/firn/blob/master/README.org] 


## Goes to the home directory
cd 




## Downloads firn

curl -s https://raw.githubusercontent.com/theiceshelf/firn/master/install -o install-firn



## Tell the user to put their superuser password to create 
## special file permissions for installing firn

#echo """
#######################################################################
#	In this next step, please enter your sudo (superuser) 
#       password to create file permission privileges for 
#       installing firn. 
#
#
#
######################################################################


#"""

#sleep 6

## Create file permission privileges for installing firn


## Goes to superuser mode 

#sudo su


## Make it runnable
#chmod -x install-firn && ./install-firn



