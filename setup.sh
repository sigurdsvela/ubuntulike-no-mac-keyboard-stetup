cd $(dirname $0)

## Add the custom layout to the "NO" xkb layout file
echo "- Create custom keybaord map"
sudo ln -fs ./no-mac-xkb/no_mac.xkb-symbol /usr/share/X11/xkb/symbols/no_mac

# Make sure we have xkeysnail and kinto dependencies
echo "- apt update"
sudo apt update &> /dev/null
echo "- check for xkeysnail and kinto dependencies"
sudo apt install python3 &> /dev/null

echo "- Setup kinto; This part will be interactive!"

sleep 2

# Setup kinto
./kinto/setup


cd -
