#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"

#########################
####### -- XKB -- #######
#########################

## Add the custom layout to the "NO" xkb layout file
echo "- Create custom keybaord map"
if [ ! -d /usr/share/X11/xkb/symbols/ ]; then sudo mkdir -p /usr/share/X11/xkb/symbols/; fi
sudo ln -fs $DIR/no-mac-xkb/no_mac.xkb-symbol /usr/share/X11/xkb/symbols/no_mac



#####################################
####### -- SETUP XKEYSNAIL -- #######
#####################################

echo "- Setup xkeysnail"

# Make sure we have xkeysnail and kinto dependencies
echo "- apt update"
sudo apt update &> /dev/null
echo "- check for xkeysnail and kinto dependencies"
sudo apt install python3 &> /dev/null

# -- XHOST FIX --
LINE='xhost +SI:localuser:root'
if [ ! -e "~/.xprofile" ]; then
  echo "$LINE" > ~/.xprofile
fi
grep -qF -- "$LINE" ~/.xprofile || echo "$LINE" >> ~/.xprofile
/bin/bash $LINE # Exec now so reboot not required

# -- CREATE XKEYSANIL CONFIG DIR --
mkdir -p ~/.config/
ln -s $DIR/xkeysnail-config ~/.config/xkeysnail

# -- CREATE XKEYSNAIL SERVICE --
service=/etc/systemd/system
sudo ln -s $DIR/xkeysnail.service $service/xkeysnail.service && echo "Created soft symlink..." || echo "Failed to create soft symlink..."
sudo chown -R root:root $service/xkeysnail.service && echo "Ownership set for root..." || echo "Failed to set ownership..."
sudo chmod 644 $service/xkeysnail.service && echo "Permissions set to 644..." || echo "Failed to set permissions..."

if [ -d $service/graphical.target.wants/ ]; then
  sudo ln -s $service/xkeysnail.service $service/graphical.target.wants/xkeysnail.service && echo "Created soft symlink for graphical target..." || echo "Failed to create soft symlink for graphical target..."
fi
