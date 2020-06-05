from selenium import webdriver
from selenium.webdriver.common.Keys import Keys
import time

#Atribuição de variaveis
email = "Aqui vai seu endereço de E-mail!!"
senha = "******"
destinatario = "Aqui vai o E-mail pra quem deseja mandar a mensagem!!"
assunto = "E-mail enviado pelo o Botmail"
mensagem = "Primeiro E-mail enviado por Botmail"

driver = webdriver.Chrome("/home/user/Desktop/robos/chromedriver")

print("Iniciando nosso robô... \n")
print("Acessando nosso Gmail...")
driver.get("https://gmail.com.br")

#Essa parte do código serve para identificar o campo onde coloca o endereço de E-mail no site do Gmail.
login = driver.find_element_by_id("identifierId")
login.clear()
login.send_Keys(email)
login.send_Keys(Keys.RETURN)
time.sleep(2)

#Essa parte do código serve para identificar o campo onde coloca a senha do E-mail no site do Gmail.
password = driver.find_element_by_name("password")
password = clear()
password.send_Keys(senha)
password.send_Keys(Keys.RETURN)
time.sleep(6)
print("Login realizado")

#Essa parte do código serve para identificar o campo onde escreve a mensagem no site do Gmail.
print("Abrindo caixa de E-mail")
driver.get("https://mail.google.com/mail/u/O/#inbox?compose=new")
time.sleep(7)

print("Escrevendo o E-mail")
para = driver.find_element_by_name("to")
para.send_Keys(destinatario)
para.send_Keys(Keys.RETURN)

titulo = driver.find_element_by_name("subjectbox")
titulo.send_Keys(assunto)
titulo.send_Keys(Keys.RETURN)

corpo_de_texto = driver.find_element_by_xpath("//div[@role='textbox']")
corpo_de_texto.send_Keys(mensagem)

#Essa parte do código serve para enviar a mensagem.
enviar = driver.find_element_by_xpath("//div[@aria-label='Enviar (Ctrl-Enter)']")
enviar.click()
print("Enviando o E-mail...")
time.sleep(5)
print("E-mail enviado com sucesso")

driver.close()