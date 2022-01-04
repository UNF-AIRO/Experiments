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

echo """
#######################################################################
#	In this next step, please enter your sudo (superuser) 
#       password to create file permission privileges for 
#       installing firn. 
#
#
#
######################################################################


"""

sleep 6

## Create file permission privileges for installing firn

sudo chmod 777 install-firn




## Get special permission from /usr/local/bin/
sudo chmod 777 /usr/local/bin/firn

## Run the file
./install-firn
