import lists
import json
import sys

from logging import StreamHandler, Formatter, LogRecord

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import logging
logger = logging.getLogger('WDM')
logger.propagate = False
logger.disabled = True

WINDOW_SIZE = "1080,900"
options = webdriver.ChromeOptions()

#options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_argument("--window-size=%s" % WINDOW_SIZE)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

default_url = "https://phasmophobia.fandom.com/ru/wiki/"
behavior_xpath = '//*[@id="mw-content-text"]/div/p[5]'
evidences_xpath = '//*[@id="mw-content-text"]/div/table[1]/tbody'
advantages_xpath = '//*[@id="mw-content-text"]/div/ul'
strategy_xpath = '//*[@id="mw-content-text"]/div/p[6]'

dict = {}

ghost = "Джинн"

def filter_python(record: LogRecord) -> bool:
    return record.getMessage().find('python') != -1

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(Formatter(fmt='[%(funcName)s: %(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(handler)

for ghost in lists.ghosts:
    logger.info(f"{ghost}: Start!")
    temp_dict = {}
    driver.get(default_url + ghost)
    driver.implicitly_wait(8)

    behavior_text = ""

    try:
        pars = True
        parsed = driver.find_element(By.XPATH, '//*[@id="Поведение"]')
        parsed = parsed.find_element(By.XPATH, "..")
        while pars:
            try:
                parsed = parsed.find_element(By.XPATH, "following-sibling::p")
                behavior_text += parsed.text
            except:
                pars = False
        logger.info(f"{ghost}: 25%")
    except:
        pass

    try:
        parsed = driver.find_element(By.XPATH, value = evidences_xpath)
        evds = parsed.text.split('\n')
        evds_list = []
        for evd in evds:
            evds_list.append(lists.evidences_dict_ru.get(evd))
        logger.info(f"{ghost}: 50%")
    except:
        pass
    
    try:
        parsed = driver.find_element(By.XPATH, value = advantages_xpath)
        advantages_text = parsed.text
        logger.info(f"{ghost}: 75%")
    except:
        pass

    strategy_text = ""

    try:
        pars = True
        parsed = driver.find_element(By.XPATH, f'//*[@id="Стратегия"]')
        parsed = parsed.find_element(By.XPATH, "..")
        while pars:
            try:
                parsed = parsed.find_element(By.XPATH, "following-sibling::p")
                strategy_text += parsed.text
            except:
                pars = False
    except:
        pass

    behavior_text = behavior_text.replace(strategy_text,"")
    
    logger.info(f"{ghost}: Done!")
    logger.info(f"")

    temp_dict['behavior'] = behavior_text
    temp_dict['evidences'] = evds_list
    temp_dict['advantages'] = advantages_text
    temp_dict['strategy'] = strategy_text
    

    dict[ghost] = temp_dict





with open("dict.json","w", encoding='utf8') as f:
    json.dump(dict, f, ensure_ascii=False)