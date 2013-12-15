#Kaboom - Command line key value store

Inspired by [Boom](http://zachholman.com/boom/)

Kaboom is a command line python application which can be used to store text snippets.

###Prerequisite

1. Python
2. Running instance of rethinkdb     (`brew install rethinkdb`)
3. MacOSX (should work on linux but not tested)

###installation

`pip install kaboom`

###Usage

* `kaboom show all` - shows all available scripts
* `kaboom show <key>` - shows script for <script-name>
* `kaboom add <key> <value>` - add scriptname to database
* `kaboom delete <key>` - delete key from database
* `kaboom delete all` - empty up the database
* `kaboom` - show help message
* `kaboom help` - show help message






