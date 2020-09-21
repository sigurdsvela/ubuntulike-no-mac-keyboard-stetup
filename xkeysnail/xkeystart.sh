#!/bin/bash
# >/dev/null 2>&1
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"


if [ -f /usr/local/bin/xkeysnail ];then
	xkeyfullpath="/usr/local/bin/xkeysnail"
elif [ -f /usr/bin/xkeysnail ];then
	xkeyfullpath="/usr/bin/xkeysnail"
else
	xkeyfullpath=`which xkeysnail`
fi

"$xkeyfullpath" --quiet --watch $DIR/config.py &

# inotifywait -m -e close_write,moved_to,create,modify /tmp/kinto/xkeysnail |

# while read -r path; do
# 	/usr/bin/killall xkeysnail
# 	"$xkeyfullpath" --quiet --watch "$1" &
# done