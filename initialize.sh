# Create remote gh-pages branch
git checkout --orphan gh-pages
git rm -r --cached .
git commit --allow-empty \
  --message "Blank branch instantiation commit" \
  --message "[ci skip]"
git push --set-upstream origin gh-pages

# Create remote references branch
git branch references
git checkout references
git push --set-upstream origin references

# Return oneself to thy master
git checkout --force master
