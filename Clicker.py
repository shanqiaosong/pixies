import random


class Clicker:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page

    def run(self):
        page = self.page
        x = random.random() * page.width
        y = random.random() * page.height
        print(x, y)
        try:
            page.click(x, y)
        except Exception:
            page.makeAnchor()
            page.click(x, y)
