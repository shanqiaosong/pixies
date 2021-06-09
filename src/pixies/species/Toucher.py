import random
from ..helper.log import logPixie


class Toucher:
    def __init__(self, page):
        self.driver = page.driver
        self.page = page

    def run(self):
        page = self.page
        moveArray = []

        for i in range(random.randint(2, 5)):
            x = random.random() * page.width
            y = random.random() * page.height
            moveArray.append([x, y])

        page.touchMove(moveArray)
        logPixie(
            'Toucher',
            f'Touch from ({int(moveArray[0][0])},{int(moveArray[0][1])}) '
            + f'to ({int(moveArray[len(moveArray)-1][0])},'
            + f'{int(moveArray[len(moveArray)-1][1])})')
