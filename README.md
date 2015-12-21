# MusicBrainz Simple Solr Search Server Schema #

This repository includes schema definitions for several Solr cores - 1 for each
entity type in MusicBrainz.
[The Solr Reference Guide](https://cwiki.apache.org/confluence/display/solr/Documents%2C+Fields%2C+and+Schema+Design)
contains more information about how these work.

Note that this repository uses the
[core discovery](https://cwiki.apache.org/confluence/display/solr/Solr+Cores+and+solr.xml)
mechanism of Solr 5. It will not work with all versions of Solr 4.

## Adding the MusicBrainz Query Response Writer 

To run a Solr server with the cores definied in this repository, you first need
to install
[the MusicBrainz QueryResponseWriter](https://github.com/jeffweeksio/mb-solrquerywriter)
and place the resulting file called solrwriter-0.0.1-SNAPSHOT-jar-with-dependencies.jar into the `mbsssss/lib` folder, which is configured as the Solr server's **sharedLib**
folder.

## Running a Solr server with these cores

If you haven't already, download Solr from its
[website](https://lucene.apache.org/solr/mirrors-solr-latest-redir.html) and
extract the archive.

You will now have a solr-x.x.x folder (where x.x.x is Solrs version
number). Inside this folder, there's a `bin` folder containing scripts to start
a Solr server. You can use those to start a Solr server which knows the cores in
this repository with the following command:

> /path/to/solr-x.x.x/bin/solr -f -s /path/to/this/repository

## Defining a new core

Defining a new core requires following these steps:

1. Create a config directory for it, based on the template directory
   (`cp -r _template $corename`)
2. Create an empty `core.properties` file in the cores directory
   (`touch $corename/core.properties`).
3. Symlink the `fieldtypes.xml` file from the `common` folder into the new
   configuration folder (`pushd $corename/conf && ln -s ../../common/fieldtypes.xml
   . && popd`). This file includes the fieldtype definitions that all cores have
   in common.
4. Edit the `solrconfig.xml` and `schema.xml` file in the configuration folder
   according to your needs.

## Generating mediawiki tables for the documentation

The file `searchfields.py` is a script that generates Mediawiki tables to
document the cores and all their search fields. Simply running it like

> python searchfields.py

prints that markup to standard output. You can either redirect it to a file:

> python searchfields.py > searchfields.txt

or copy it directly to the clipboard:

> python searchfields.py | xclip
