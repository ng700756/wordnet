# wordnet
Some issues to work with the ontology


    wget http://www-eu.apache.org/dist/jena/binaries/apache-jena-3.3.0.tar.gz
    wget http://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-2.6.0.tar.gz
    tar xzvf apache-jena-fuseki-*.tar.gz
    tar xzvf apache-jena-3*.tar.gz

tdbloader2 to load the WordNet 3.1 data

    mkdir apache-jena-fuseki-2.6.0/db
    mkdir apache-jena-fuseki-2.6.0/db/win31
    ./apache-jena-3.3.0/bin/tdbloader2 --loc apache-jena-fuseki-2.6.0/db/wn31 wn31.nt

to test: use elephant query

    curl -O https://raw.githubusercontent.com/lumenrobot/relex-id/master/core/elephant.sparql
    ./apache-jena-3.3.0/bin/tdbquery --loc=apache-jena-fuseki-2.6.0/db/wn31 --file elephant.sparql 
    
As server

     java -Xmx2048m -Xms2048m  -jar fuseki-server.jar --loc db /db/wn31
     http://localhost:3030/

# Reference
https://github.com/lumenrobot/relex-id
https://github.com/limves/wordnet
