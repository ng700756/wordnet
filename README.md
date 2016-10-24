# wordnet
Some issues to work with the ontology


- wget http://www-us.apache.org/dist/jena/binaries/apache-jena-3.1.0.tar.gz
- wget http://www-us.apache.org/dist/jena/binaries/apache-jena-fuseki-2.4.0.tar.gz
- tar xzvf apache-jena-fuseki-2.4.0.tar.gz

tdbloader2 to load the WordNet 3.1 data
- bin/bin/tdbloader2 --loc fuseki/db/wn31 wn31.nt

to test: use elephant query
- curl -O https://raw.githubusercontent.com/lumenrobot/relex-id/master/core/elephant.sparql
- jena/bin/tdbquery --loc=fuseki/wn31 --file elephant.sparql


# Reference
https://github.com/lumenrobot/relex-id
