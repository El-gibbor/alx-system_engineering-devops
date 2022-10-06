#!/bin/bash

# a scripts that add, commit and push my stuffs to github

echo "what is your commit message?"
# prompt user to input commit message

read commitMessage
# accepts commit message from user, then add, commit and push

git add .

git commit -m "commitMessage"

git push
