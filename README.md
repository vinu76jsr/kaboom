#Kaboom - Command line key value store

Inspired by [Boom](http://zachholman.com/boom/)

Kaboom is a command line python application which can be used to store text snippets.

###Prerequisite

1. Python
2. Running instance of rethinkdb (`brew install rethinkdb`)
3. MacOSX (should work on linux but not tested)

###installation

1. clone this repo
2. put it in your path

###Usage

`./kaboom.py show all` - shows all available scripts
`./kaboom.py show <key>` - shows script for <script-name>
`./kaboom.py add <key> <value> - add scriptname to database
`./kaboom.py delete <key> - delete key from database
`./kaboom.py delete all` - empty up the database





