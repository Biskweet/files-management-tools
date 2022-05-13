# Files management tools

Handy and compact (because it's more fun) functions made for simple operations on all files and folders of a directory. Made for terminal interpreter use.

### Requirements
* `humanize` package

### How-to
* Run the selected function with the path you want (examples: `get_all_extensions(".")`, `renamer("/home/user", " ", "_")`, ...)
* DON'T ADD `/` AT THE END OF YOUR PATH (✅`dir_size("/home")`✅, ❌`dir_size("/home/")`❌). That problem could be easily avoidable but I am too lazy to handle it. This repo is more for my personal use than someone else's anyway.
