#####################################################################
#	build.sh
#	This shell script automates generating a static site
#	using Org Mode with Firn
#
#
#####################################################################






## This will build the site. 
## After writing an article in org mode, this will detect the .org files, 
## for example, index.org, it will output the conversion to index.html.

## For more information about this, please read their documentation here

## https://firn.theiceshelf.com/getting-started 

firn build


ls -l _firn/_site


## Test the generated site in localhost. 
firn serve
