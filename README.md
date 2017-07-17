# wordnet
Some issues to work with the ontology


    wget http://www-eu.apache.org/dist/jena/binaries/apache-jena-3.3.0.tar.gz
    wget http://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-2.6.0.tar.gz
    tar xzvf apache-jena-fuseki-*.tar.gz
    tar xzvf apache-jena-3*.tar.gz

tdbloader2 to load the WordNet 3.1 data

    cd apache-jena-3.3.0    
    ./apache-jena-3.3.0/bin/tdbloader2 --loc apache-jena-fuseki-2.6.0/db/wn31 wn31.nt

to test: use elephant query
- curl -O https://raw.githubusercontent.com/lumenrobot/relex-id/master/core/elephant.sparql
- cd jena
- ./bin/tdbquery --loc=../fuseki/wn31 --file ../elephant.sparql º


# Reference
https://github.com/lumenrobot/relex-id
https://github.com/limves/wordnet
