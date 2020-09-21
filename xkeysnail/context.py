class Context {
	terminal = __class__([
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

	browser = __class__([
		"Chromium",
		"Chromium-browser",
		"Google-chrome",
		"Epiphany",
		"Firefox",
		"Discord"
	])

	vscode = __class__([
		"code",
		"vscodium"
	])

	nautilus = __class__(["org.gnome.nautilus"])

	def __init__(self, names):
		self._names = map(lambda name: lower(name), names)

	def names(self):
		return self._names;

	def __str__(self):
		return "|".join(str(name) for name in self._names)
	
	def __contains__(self, other):
		return lower(other) in self._names
}
