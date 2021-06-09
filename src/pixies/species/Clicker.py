import random
from ..helper.log import logPixie


class Clicker:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page

    def run(self):
        page = self.page
        if random.random() > 0.7:
            # 随机点击
            x = random.random() * page.width
            y = random.random() * page.height
            try:
                page.click(x, y)
            except Exception:
                page.makeAnchor()
                page.click(x, y)
            logPixie('Clicker', f'Clicked at position ({int(x)},{int(y)})')
        else:
            # 定向点击
            while not page.clickElement(random.choice(page.clickable)):
                page.analyzeElement()
            logPixie('Clicker', f'Clicked at a clickable element')
