import random
from ..helper.log import logPixie


class Resizer:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page

    def run(self):
        page = self.page
        width = page.minWidth+(page.maxWidth-page.minWidth)*random.random()
        height = page.minHeight+(page.maxHeight-page.minHeight)*random.random()
        page.setWindowSize(width, height)
        logPixie('Resizer', f'Resized to ({int(width)},{int(height)})')
