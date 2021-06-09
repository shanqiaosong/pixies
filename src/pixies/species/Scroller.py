import random
from ..helper.log import logPixie


class Scroller:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page

    def run(self):
        driver = self.driver
        x = random.random()
        y = random.random()
        result = driver.execute_script(
            """
            window.scrollTo(
                {
                    top: document.body.scrollHeight * arguments[0],
                    left: document.body.scrollWidth * arguments[1],
                    behavior: "smooth"
                }
            )
            return [
                document.body.scrollHeight * arguments[0],
                document.body.scrollWidth * arguments[1]
            ]
            """,
            x,
            y
        )
        self.page.indicateControl()
        logPixie(
            'Scroller', f'Scrolled to position ' +
            f'({int(result[0])},{int(result[1])})')
