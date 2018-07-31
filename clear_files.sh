find -name "*~" | xargs -r rm
find -name "*.staging" | xargs -r rm
find -name "*#" | xargs -r rm
find ./nodejs_codegen -name "*.pyc" | xargs -r rm
