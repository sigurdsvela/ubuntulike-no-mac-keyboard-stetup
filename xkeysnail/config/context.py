class Context:
	terminal=0
	browser=0
	vscode=0
	nautilus=0

	def __init__(self, names):
		self._names = map(lambda name: name.lower(), names)

	def names(self):
		return self._names

	def __str__(self):
		return "|".join(str(name) for name in self._names)
	
	def __contains__(self, other):
		return other.lower() in self._names

Context.terminal = Context([
	"gnome-terminal",
	"konsole",
	"io.elementary.terminal",
	"terminator",
	"sakura",
	"guake",
	"tilda",
	"xterm",
	"eterm",
	"kitty",
	"alacritty",
	"mate-terminal",
	"tilix",
	"xfce4-terminal"
])

Context.browser = Context([
	"Chromium",
	"Chromium-browser",
	"Google-chrome",
	"Epiphany",
	"Firefox",
	"Discord"
])

Context.vscode = Context([
	"code",
	"vscodium"
])

Context.nautilus = Context(["org.gnome.nautilus"])

