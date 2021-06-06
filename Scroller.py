import random


class Scroller:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page

    def run(self):
        driver = self.driver
        driver.execute_script(
            """
            window.scrollTo(
                {
                    top: document.body.scrollHeight * arguments[0],
                    left: document.body.scrollWidth * arguments[1],
                    behavior: "smooth"
                }
            )
            """,
            random.random(),
            random.random()
        )
        self.page.indicateControl()
