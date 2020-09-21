#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
cd $DIR

## Add the custom layout to the "NO" xkb layout file
echo "- Create custom keybaord map"
if [ ! -d /usr/share/X11/xkb/symbols/ ]; then sudo mkdir -p /usr/share/X11/xkb/symbols/; fi
sudo ln -fs $(pwd)/no-mac-xkb/no_mac.xkb-symbol /usr/share/X11/xkb/symbols/no_mac

# Make sure we have xkeysnail and kinto dependencies
echo "- apt update"
sudo apt update &> /dev/null
echo "- check for xkeysnail and kinto dependencies"
sudo apt install python3 &> /dev/null

echo "- Setup kinto; This part will be interactive!"

sleep 2

# Setup kinto
./kinto/setup.sh


cd -
