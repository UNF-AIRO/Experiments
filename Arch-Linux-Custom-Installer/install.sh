##########################################################
#       AIRO-Arch-Linux Installation Script
#       
#       This script allows the automatic installation of
#       Arch Linux customized to be deployed on a server
#       that is used with the projects maintained by UNF-AIRO
#
#
##########################################################


clear

echo """
___________________________________________________________________________


        U      N        F            -          A        I       R       O

___________________________________________________________________________


"""
sleep 5


clear


echo """
____________________________________


Welcome to the Installer 

____________________________________


____________________________________________________

Choose 1 to Continue. Pressing (1) will wipe your storage device data.

Choose 2 to exit the Program

____________________________________________________

        ______________________________________
	* Yes, Install 		        (1)
	
	* No, Exit the Program		(2)
        ______________________________________
	
"""
while :
	do 
	read CHOICE

	case $CHOICE in 

		## After the user chooses yes, then it will install 
		
		1)      
			ip link					## Get the network to work 

			timedatectl set-ntp true		## Get the system clock to be updated

fdisk /dev/sda <<EOF			
n
p
w
EOF
			
			
			mkfs.ext4 /dev/sda1			## Create the file system 

			mkswap /dev/sda1			## Swap the file system 

			mkfs.fat -F 32 /dev/sda1		## Create an EFI File system 

			mount /dev/sda1	/mnt/boot		## Mount the drive

			swapon /dev/sda1			## enable the volume using swapon


			## Install packages such as the kernel, firmware
			pacstrap /mnt base linux linux-firmware 

			## Configure the system with fstab
			genfstab -U /mnt >> /mnt/etc/fstab


			## Chroot into the installed system
			arch-chroot /mnt
			



                        ;;

		## After the user chooses no, it will exit the program

		
		2)
			exit
                        ;;

		## If the user presses a unknown character, it will inform
		## the user to choose the correct commands. 
		*)
			echo """
			*****************************************************
			*	Unknown! Please Try Again!
			*
			*****************************************************
			"""
esac
done
