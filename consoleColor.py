#!/usr/bin/python
# -*- coding: utf-8 -*-

class Color():
	reset = "\033[0m"
	styles = {
		"bold"       :    "\033[1m",
		"underline"  :    "\033[4m",
		"reverse"    :    "\033[7m"}
	colors = {
		"black"      :    "\033[30m", 
		"red"        :    "\033[31m",
		"green"      :    "\033[32m",
		"yellow"     :    "\033[33m",
		"blue"       :    "\033[34m",
		"magenta"    :    "\033[35m",
		"cyan"       :    "\033[36m",
		"white"      :    "\033[37m"}
	backgroundColors = {
		"on_black"   :    "\033[40m", 
		"on_red"     :    "\033[41m",
		"on_green"   :    "\033[42m",
		"on_yellow"  :    "\033[43m",
		"on_blue"    :    "\033[44m",
		"on_magenta" :    "\033[45m",
		"on_cyan"    :    "\033[46m",
		"on_white"   :    "\033[47m"}

	def out(self, message, color, style=None, bg=None):
		options = self.colors[color]
		if style:
			options += self.styles[style]
		if bg:
			options += self.backgroundColors[bg]

		return options+message+self.reset