import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageTool:
    # 用于对页面进行操作的工具类
    def __init__(self, driver):
        self.driver = driver
        # 可点击的范围
        self.width = 0
        self.height = 0
        # 最大化后的大小
        self.maxWidth = 0
        self.maxHeight = 0
        # 最小的大小
        self.minWidth = 0
        self.minHeight = 0
        self.pageInit()

    def getViewportSize(self):
        # 查询视窗大小
        driver = self.driver
        window_size = driver.execute_script(
            """
            return [window.innerWidth, window.innerHeight];
            """
        )
        return window_size

    def setWindowSize(self, width, height):
        # 设置视窗大小
        if width > self.maxWidth or height > self.maxHeight:
            return
        driver = self.driver
        driver.set_window_size(width, height)
        self.refreshSize()

    def closeOther(self):
        # 关闭其他页面，回到主页面
        driver = self.driver
        mainWindow = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != mainWindow:
                driver.switch_to.window(handle)
                driver.close()
        driver.switch_to.window(mainWindow)

    def makeAnchor(self):
        # 视窗（viewport）左上角添加一个锚点，用于定位cursor
        driver = self.driver
        driver.execute_script(
            """
            let point=document.createElement('div')
            point.style.width=0
            point.style.height=0
            point.style.position='fixed'
            point.style.top=0
            point.style.left=0
            point.id='anchorPoint'
            document.querySelector('body').append(point)
            """
        )
        self.anchorPoint = driver.find_element(By.CSS_SELECTOR, "#anchorPoint")

    def indicateClick(self, x, y):
        # 在页面中xy坐标处提示点击
        driver = self.driver
        driver.execute_script(
            '''
            let point=document.createElement('div')
            point.style.width='20px'
            point.style.height='20px'
            point.style.background='red'
            point.style.borderRadius='10px'
            point.style.position='fixed'
            point.style.top="'''
            + str(y - 10)
            + '''px"
            point.style.left="'''
            + str(x - 10)
            + """px"
            point.style.zIndex=100000
            point.style.opacity=0.7
            point.style.transition='all 0.5s'
            point.style.boxShadow='red 0 0 10px'
            document.querySelector('body').append(point)
            setTimeout(()=>{
                point.style.opacity=0
            },200)
            setTimeout(()=>{
            document.querySelector('body').removeChild(point)
            },700)
            """
        )

    def indicateKey(self, element, key):
        # 在页面element处提示输入键盘key
        driver = self.driver
        driver.execute_script(
            '''
            let point=document.createElement('div')
            point.innerText="'''
            + key
            + '''"
            point.style.color='white'
            point.style.lineHeight='30px'
            point.style.textAlign='center'
            point.style.width='fit-content'
            point.style.padding='5px'
            point.style.height='30px'
            point.style.background='red'
            point.style.borderRadius='5px'
            point.style.position='absolute'
            point.style.top="'''
            + str(element.location["y"] - 10)
            + '''px"
            point.style.left="'''
            + str(element.location["x"] - 10)
            + """px"
            point.style.zIndex=100000
            point.style.opacity=0.7
            point.style.transition='all 0.5s'
            point.style.boxShadow='red 0 0 10px'
            document.querySelector('body').append(point)
            setTimeout(()=>{
                point.style.opacity=0
            },200)
            setTimeout(()=>{
            document.querySelector('body').removeChild(point)
            },700)
            """
        )

    def indicateControl(self):
        # 在页面提示受控区域
        driver = self.driver
        driver.execute_script(
            '''
            let point=document.createElement('div')
            point.style.boxSizing='border-box'
            point.style.width="'''
            + str(self.width-40) +
            '''px"
            point.style.height="'''
            + str(self.height-40) +
            '''px"
            point.style.margin=0
            point.style.position='fixed'
            point.style.top='20px'
            point.style.left='20px'
            point.style.border='8px solid red'
            point.style.zIndex=100000
            point.style.opacity=0.7
            point.style.transition='all 0.5s'
            document.querySelector('body').append(point)
            setTimeout(()=>{
                point.style.opacity=0
            },200)
            setTimeout(()=>{
            document.querySelector('body').removeChild(point)
            },700)
            '''
        )

    def pageInit(self):
        # 用于对页面进行初始化：设置锚点，防止导航，设置视窗
        driver = self.driver
        self.makeAnchor()
        driver.execute_script(
            "document.querySelectorAll('a').forEach((a)=>{a.target='_blank'})"
        )
        driver.set_window_size(1, 1)
        [self.minWidth, self.minHeight] = [
            driver.get_window_size()['width'],
            driver.get_window_size()['height']
        ]
        driver.maximize_window()
        [self.maxWidth, self.maxHeight] = [
            driver.get_window_size()['width'],
            driver.get_window_size()['height']
        ]
        self.refreshSize()

    def refreshSize(self):
        # 用于更新页面大小信息
        [self.width, self.height] = self.getViewportSize()

    def reset(self):
        # 将光标设置到视窗左上角
        driver = self.driver
        anchorPoint = self.anchorPoint
        return webdriver.ActionChains(driver).move_to_element(anchorPoint)

    def click_locxy(self, x, y, left_click=True):
        # 点击坐标
        self.reset().move_by_offset(x, y).click().perform()

    def click(self, x, y):
        # 点击坐标并提示，并防止新页面（如果产生则关闭并自动返回）
        self.click_locxy(x, y, True)
        self.indicateClick(x, y)
        self.indicateControl()
        self.closeOther()

    def key(self, chars):
        driver = self.driver
        # 在目前的活跃节点输入chars
        element = driver.switch_to.active_element
        element.send_keys(chars)
        self.indicateKey(element, chars)
        self.indicateControl()
