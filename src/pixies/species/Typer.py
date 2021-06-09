import random
import string
from selenium.webdriver.common.keys import Keys
from ..helper.log import logPixie


class Typer:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page
        self.controlKeys = [
            Keys.ENTER,
            Keys.SHIFT,
            Keys.BACK_SPACE,
            Keys.ESCAPE,
            Keys.CONTROL
        ]
        self.candidates = list(string.ascii_uppercase) + \
            list(string.digits) + self.controlKeys

    def run(self):
        page = self.page
        content = ''.join(random.choices(
            self.candidates +
            [chr(random.randint(0, 0xffff)) for i in range(10)], k=5))
        if random.random() > 0.7:
            # 向当前元素输入
            page.key(content)
            logPixie(
                'Typer', f'Typed "{repr(content)}" '
                + 'into the current active element')
        else:
            # 向可输入元素输入
            while not page.key(
                content,
                element=random.choice(page.keyable)
            ):
                page.analyzeElement()

            logPixie(
                'Typer', f'Typed "{repr(content)}" into an input element')
