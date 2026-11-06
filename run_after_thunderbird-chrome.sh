#!/bin/bash
# Copy Thunderbird userChrome.css + user.js into every profile found
set -euo pipefail
src="$HOME/.config/thunderbird"

for base in \
  "$HOME/.var/app/org.mozilla.thunderbird_esr/.thunderbird" \
  "$HOME/.var/app/org.mozilla.Thunderbird/.thunderbird" \
  "$HOME/.thunderbird"; do
  [ -d "$base" ] || continue
  for profile in "$base"/*.default*/; do
    [ -d "$profile" ] || continue
    mkdir -p "$profile/chrome"
    cp "$src/userChrome.css" "$profile/chrome/userChrome.css"
    cp "$src/user.js" "$profile/user.js"
    echo "thunderbird: updated $profile"
  done
done
