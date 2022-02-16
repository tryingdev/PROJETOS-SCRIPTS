from secrets import randbelow
from selenium import webdriver
import time


class BotVoto:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def AcessarVoto(self):
        self.driver.get('https://ragnatales.com.br/')
        time.sleep(15)
        click_conta = self.driver.find_element_by_xpath("//a[@href='/conta']")
        click_conta.click()
        usuario = self.driver.find_element_by_xpath("//*[@placeholder='Insira seu endereço de e-mail']")
        usuario.send_keys("########")
        senha = self.driver.find_element_by_xpath("//*[@placeholder='Digite sua senha']")
        senha.send_keys("########")
        time.sleep(30)
        time.sleep(randbelow(5))
        self.driver.find_element_by_xpath("//a[normalize-space()='Vote por Pontos']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[normalize-space()='Votar']").click()
        time.sleep(30)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@src='https://www.topragnarok.org/images/votebanner.gif']").click()


bot = BotVoto()
bot.AcessarVoto()
