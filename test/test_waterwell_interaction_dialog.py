# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'diogo.sousa@inema.ba.gov.br'
__date__ = '2024-09-25'
__copyright__ = 'Copyright 2024, Diogo Caribé de Sousa'

import unittest

from qgis.PyQt.QtGui import QDialogButtonBox, QDialog

from waterwell_interaction_dialog import waterwell_interactionDialog

from utilities import get_qgis_app
QGIS_APP = get_qgis_app()


class waterwell_interactionDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.dialog = waterwell_interactionDialog(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_dialog_ok(self):
        """Test we can click OK."""

        button = self.dialog.button_box.button(QDialogButtonBox.Ok)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Accepted)

    def test_dialog_cancel(self):
        """Test we can click cancel."""
        button = self.dialog.button_box.button(QDialogButtonBox.Cancel)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Rejected)

if __name__ == "__main__":
    suite = unittest.makeSuite(waterwell_interactionDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

