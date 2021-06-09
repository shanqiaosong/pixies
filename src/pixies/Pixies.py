from .helper.log import logError, logEvent
from .helper.PageTool import PageTool
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from .species import Clicker, Scroller, Toucher, Typer, Resizer
import random


class Cage:
    def __init__(
        self,
        url,
        pixieList=[
            Clicker, Scroller, Toucher, Typer, Resizer
        ],
        weightList=[],
        browser='chrome',
        stopAtError=True
    ) -> None:
        self.pixieList = pixieList
        self.weightList = weightList
        self.url = url
        self.browser = browser
        self.errors = set()
        self.stopAtError = stopAtError
        self.openBrowser()

    def openBrowser(self):
        logEvent('Configuring...')
        options = Options()
        options.add_experimental_option('w3c', False)
        options.add_argument('start-maximized')
        options.add_argument('--auto-open-devtools-for-tabs')
        if len(self.weightList) != 0 and\
                len(self.weightList) != len(self.pixieList):
            raise Exception('Weight list illegal!')
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome(options=options)
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox(options=options)
        elif self.browser == 'safari':
            self.driver = webdriver.Safari(options=options)
        else:
            raise Exception("Browser unrecognized!")
        self.driver.get(self.url)
        self.page = PageTool(self.driver)
        logEvent('Page ready, you can release the cage now!')

    def release(self, length=100):
        logEvent('Releasing pixies...')
        pixieIntances = []
        for i in self.pixieList:
            pixieIntances.append(i(self.page))
        for i in range(length):
            if len(self.weightList):
                ins = random.choices(
                    pixieIntances, weights=self.weightList, k=1)[0]
            else:
                ins = random.choice(pixieIntances)
            ins.run()
            if self.errorDetection() and self.stopAtError:
                logEvent('Error detected, Peskipiksi Pesternomi!')
                self.driver.maximize_window()
                return
        self.driver.maximize_window()
        logEvent('No error detected, Peskipiksi Pesternomi!')

    def errorDetection(self):
        logs = self.driver.get_log('browser')
        for i in logs:
            if i['level'] != 'SEVERE' or i['source'] == 'network':
                continue
            if i['message']+str(i['timestamp']) in self.errors:
                continue
            logError(i['message'])
            self.errors.add(i['message']+str(i['timestamp']))
            return True
        return False
