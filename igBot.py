from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import datetime
import os 
import getpass 


print('='*30)
print('BOT COMENTAR NO INSTAGRAM')
print('='*30)
usuario = input('Digite seu email: ')
senha = getpass.getpass('Digite sua senha: ')
link = input('Coloque o link do sorteio aqui: ')
#enderecoGeckoDriver = os.path.abspath("geckodriver.exe")'''



class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r'C:\Users\rafae\Documents\Projetos\BotComentariosInstagram\geckodriver.exe'
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(10)
        
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(7)

        self.comente_no_sorteio('p/B8ujLBplVLk')
        
    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,9)/30)
            

    def comente_no_sorteio(self,sorteio):
        driver = self.driver
        #COLOCA O LINK DO SORTEIO AI EM BAIXO
        driver.get(link)
        time.sleep(3) 
        
        contador=0
        while(0!=1):
            try:
                #COLOQUE LISTA DOS USUARIOS ABAIXO. A LISTA TEM QUE SER DA SEGUINTE FORMA:
                #PARA ESCREVER UM USUARIO DE CADA VEZ, PRECISA SER ADICIONADA DA SEGUINTE FORMA : ("@username1","@username2","@username3")
                #PARA ESCREVER TRES USUARIO DE CADE VEZ, PRECISA SER ADICIONADA DA SEGUINTE FORMA: ("@username1 @username2 @username3","@username4 @username5 @username6") 
                comentarios = ["COLOQUE SUA LISTA DE USUARIOS AQUI CONFORME ESCRITO ACIMA!!"]
                i=0
                while(i!=20000):
                    time.sleep(random.randint(160,180))
                    driver.find_element_by_class_name("Ypffh").click()
                    campo_comentario = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(4,10)) #Define o tempo para começar a escrever o comentario
                    campo_comentario.clear()
                    amigos = random.choice(comentarios)
                    #self.digite_como_uma_pessoa(random.choice(eu),campo_comentario)
                    self.digite_como_uma_pessoa(amigos,campo_comentario)
                    time.sleep(random.randint(5,10))
                    campo_comentario.send_keys(Keys.RETURN)
                    campo_comentario.send_keys(Keys.RETURN)
                    campo_comentario.send_keys(Keys.RETURN)
                    contador = contador + 1
                    horaagora = datetime.now()
                    hora = horaagora.hour
                    minutos = horaagora.minute
                    segundos = horaagora.second

                    print(str(hora)+":"+str(minutos)+":"+str(segundos)+" | "+str(contador)+" | "+str(amigos))
                    i = i + 1
                    time.sleep(random.randint(15,18))
                time.sleep(random.randint(240,300))
            except Exception as e:
      
                print(e)
                time.sleep(5)

Bot = InstagramBot(usuario,senha)
Bot.login()
