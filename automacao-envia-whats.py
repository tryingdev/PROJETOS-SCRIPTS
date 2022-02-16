from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.x = 0
        self.mensagem = "Oi teteu"
        self.gp_ou_contatos = ["Teteu"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        while self.x < 50:
            for gp_ou_contato in self.gp_ou_contatos:
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{gp_ou_contato}']")
                time.sleep(1)
                campo_grupo.click()
                chat_box = self.driver.find_element_by_xpath("//div[@title='Mensagem']")
                time.sleep(1)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(1)
                botao_enviar.click()
                time.sleep(1)
                self.x = self.x + 1


bot = WhatsappBot()
bot.EnviarMensagens()
