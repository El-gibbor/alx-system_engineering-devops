# a script that adds, commit, and push my work to github

#!/bin/bash

echo "input your commit message"

read commitMessage

git add .

git commit -m "commitMessage"

git push

