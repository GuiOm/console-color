#!/usr/bin/python
# -*- coding: utf-8 -*-

class Color():
	RESET = "\033[0m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	REVERSE = "\033[7m"
	BLACK = "\033[30m"
	RED = "\033[31m"
	GREEN = "\033[32m"
	YELLOW = "\033[33m"
	BLUE = "\033[34m"
	MAGENTA = "\033[35m"
	CYAN = "\033[36m"
	WHITE = "\033[37m"
	ON_BLACK = "\033[40m"
	ON_RED = "\033[41m"
	ON_GREEN = "\033[42m"
	ON_YELLOW = "\033[43m"
	ON_BLUE = "\033[44m"
	ON_MAGENTA = "\033[45m"
	ON_CYAN = "\033[46m"
	ON_WHITE = "\033[47m"

	def out(self, message, *args):
		style = ""
		for s in args:
			style += s
		return style+message+self.RESET
