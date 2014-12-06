#!/bin/bash

shopt -s globstar

if ! command -V ack &> /dev/null; then
    echo "You need ack"
    exit 1
fi

for schema in **/*schema.xml; do
     schemaname=$(ack --output="\$1" 'schema\s*name="([\w\-]*)"' $schema)
     fields=$(ack --output="\$1" 'field\s*name="(\w*)"' $schema)
     printf "# Available search fields for %s\n\n" "$schemaname"
     for field in $fields; do
         printf "* %s\n" $(sed -e 's|_|\\_|g' <<<$field )
     done
     printf "\n"
done
