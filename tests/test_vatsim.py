"""
vatsim
Copyright (C) 2018  Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of vatsim.

vatsim is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

vatsim is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with vatsim.  If not, see <http://www.gnu.org/licenses/>.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_vatsim
----------------------------------

Tests for `vatsim` module.
"""

import unittest

import vatsim


class TestVatsim(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(vatsim.__version__)

    def tearDown(self):
        pass
