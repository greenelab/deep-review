# Automatically rebuild manuscript when content changes
# Depends on watchdog https://github.com/gorakhargosh/watchdog
watchmedo shell-command \
  --wait \
  --command='sh build/build.sh' \
  content
