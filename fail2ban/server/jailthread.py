# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet :

# This file is part of Fail2Ban.
#
# Fail2Ban is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Fail2Ban is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Fail2Ban; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# Author: Cyril Jaquier
# 

__author__ = "Cyril Jaquier"
__copyright__ = "Copyright (c) 2004 Cyril Jaquier"
__license__ = "GPL"

from threading import Thread
from abc import abstractproperty, abstractmethod

class JailThread(Thread):
	"""Abstract class for threading elements in Fail2Ban.
	"""

	def __init__(self):
		"""Initialise a JailThread instance.
		"""
		super(JailThread, self).__init__()
		## Control the state of the thread.
		self.active = False
		## Control the idle state of the thread.
		self.idle = False
		## The time the thread sleeps in the loop.
		self.sleeptime = 1

	@abstractproperty
	def status(self): # pragma: no cover - abstract
		"""Abstract - Should provide status information.
		"""
		pass

	def start(self):
		"""Sets active flag and starts thread.
		"""
		self.active = True
		super(JailThread, self).start()

	def stop(self):
		"""Sets `active` property to False, to flag run method to return.
		"""
		self.active = False

	@abstractmethod
	def run(self): # pragma: no cover - absract
		"""Abstract - Called when thread starts, thread stops when returns.
		"""
		pass
