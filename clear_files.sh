find -name "*~" | xargs -r rm
find -name "*.staging" | xargs -r rm
find -name "*#" | xargs -r rm
find ./mapper_on_files -name "*.pyc" | xargs -r rm
