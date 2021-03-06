## Pixies

A front-end monkey testing suite based on Python webdriver.

Watch out for the flying pixies!

### Usage

#### Quick start

```bash
$ pip install pixies
```

Download [Chrome Webdriver binary](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/), and add it to the System PATH.

Make sure when entering ```chromedriver``` in the terminal, the following prompt appears:

```bash
$ ChromeDriver was started successfully.
```

Use pixies in python:

```python
import pixies

cage = pixies.Cage('https://news.baidu.com')
cage.release()
```

If you'd like to specify the species (which have different behavior) of pixies:

```python
import pixies
from pixies.species import Clicker, Scroller, Toucher, Typer, Resizer

cage = pixies.Cage(
    'https://news.baidu.com',
    pixieList=[
        Clicker, Scroller, Toucher, Typer, Resizer
    ])
cage.release()
```

#### Params

``` python
class pixies.Cage(
    url, # necessary
    pixieList = [
        Clicker, Scroller, Toucher, Typer, Resizer
    ], # optional, all pixie species by default
    weightList = [], # optional, equal weight by default
    browser = 'chrome', # optional, 'safari'|'chrome'|'firefox'
    stopAtError = True, # optional
)
method pixies.Cage.release(
    length = 100 # optional, times to run pixies
)
```

### Species

Different pixie species do different things to the page.

#### Clicker

- Randomly click on the page visible area

- Prevent navigation automatically

- Switch back immediately when new pages are openned

- Identify clickable objects and focus on them

#### Scroller

- Randomly scroll to different places of the main page

#### Resizer

- Resize the page randomly

- Identify the max and min size of the page automatically

#### Typer

- Generates random UTF-8 BMP characters and control keys (such as shift, enter, ESC stc.) and send them to the currently active element

- Prevent the page from navigating away

- Identify input objects and send keys to them

#### Toucher

- Imitate touch events, supporting path touching

#### Dragger

- [TODO]
