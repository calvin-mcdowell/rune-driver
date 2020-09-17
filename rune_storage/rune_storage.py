"""
https://github.com/calvin-mcdowell/rune-driver

Class to provide methods for managing storage of rune pages on the host system
"""
import json
import os


class RuneStorage:
    """
    """

    def __init__(self):
        self.validate_runes_folder()

    def validate_runes_folder(self):
        """
        Verify that the rune pages directory exists and if not, attempt to create it
        """
        try:
            if not os.path.exists('rune_storage/runes'):
                os.makedirs('rune_storage/runes')
        except OSError as err:
            # TODO: Add logging functions here
            print(f'Error creating runes folder at {os.path.abspath(os.path.curdir)}/runes:\n\t{err}')

    def list_rune_pages(self):
        pass

    def save_rune_page(self, page):
        pass

    def load_rune_page(self):
        pass

    def delete_rune_page(self):
        pass