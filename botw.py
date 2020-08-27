from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "teste de envio de mensagem através de bot"
        self.grupos = ["Churras na casa da Suzi"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
        
    def EnviarMensagens (self):
        # <span dir="auto" title="Churras na casa da Suzi" class="_3ko75 _5h6Y_ _3Whw5">Churras na casa da Suzi</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()