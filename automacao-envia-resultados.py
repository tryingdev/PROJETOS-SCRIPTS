from enviaemail import MandaEmail
from selenium import webdriver
import time


class EntraSite:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def AcessaExame(self):
        self.driver.get('######') #site
        time.sleep(15)
        codigoexame = self.driver.find_element_by_xpath("//*[@placeholder='Sua chave:']")
        codigoexame.send_keys("#####")#cod-login
        senha = self.driver.find_element_by_xpath("//*[@placeholder='Senha:']")
        senha.send_keys("####")#senha
        time.sleep(10)
        bota_entrar = self.driver.find_element_by_class_name('btn')
        bota_entrar.click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(10)
        botao_salvar = self.driver.find_element_by_id('btn_salvar')
        botao_salvar.click()


bot = EntraSite()
x = 0
while x <= 1:
    bot.AcessaExame()
    MandaEmail()
    x = x+1
