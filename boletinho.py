from ast import While
from operator import index
from textwrap import indent
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import pandas as pd
 
navegador= webdriver.Chrome()
navegador.get('https://app.empresas.bs2.com/bs2/boleto/boletos/individual')


def login():
    sleep(2)
    login_element = navegador.find_element('css selector', 'input[name="usuario"]')
    sleep(2)
    password_element = navegador.find_element('css selector', 'input[type="password"]')
    sleep(2)
    enter_element = navegador.find_element('css selector', 'span[class="mat-button-wrapper"]')

    login_element.send_keys('anasantana')
    password_element.send_keys('Avonale@22')
    enter_element.click()
    
    sleep(10)
    plataforma_cobrança = navegador.find_element('css selector', 'a[id="PlataformaCobranca"]')
    sleep(2)
    plataforma_cobrança.click()

def tipo_boleto():
    sleep(5)
    conta = navegador.find_element('css selector', 'div[class="dropdown-conta"]').click()
    parceiro = input('Digite o parceiro: \n')
    if parceiro == 'bv':
        sleep(2)
        navegador.find_element('css selector', 'div[class="item 51e970dc-f871-4bc4-a3f7-b97b2881d2a8 ng-star-inserted"]').click()
    elif parceiro == 'portoseguro': 
        sleep(2)
        navegador.find_element('css selector', 'div[class="item ba457589-00a0-4adf-a193-9edb4822da15 ng-star-inserted"]').click()  
    elif parceiro == 'localiza':
        sleep(2)
        navegador.find_element('css selector', 'div[class="item active"]').click()
          
def tela_boleto():
    sleep(2)
    carteira = navegador.find_element('css selector', 'a[id="link-emitir-boleto"]').click()
    sleep(2)
    tipo_carteira = navegador.find_element('css selector','a[id="link-emitir-individual"]').click()    
      

def emitir_boleto():
    
    planilha = pd.read_excel(r'D:\boletinho\lojistas.xlsx')
  
    for i, Cnpj in enumerate(planilha["Cnpj"]): 
        print(planilha) 
        Controle = planilha.loc[i, "Controle"]
        Valor = planilha.loc[i, "Valor"]
        placa = planilha.loc[i, "Placa"]
        sleep(2)
        navegador.find_element('css selector','input[name="valorcobranca"]').send_keys(str(Valor))
        sleep(2)
        navegador.find_element('css selector','input[name="seuNumero"]').send_keys(str(Controle))
        sleep(2)
        navegador.find_element('css selector','input[name="nome"]').send_keys(Cnpj)
        sleep(2)
        sacado = navegador.find_element('css selector','span[class="mat-option-text"] div[class="text _mask ng-star-inserted"]').click()
        sleep(2)
        info_placa = navegador.find_element('css selector','textarea[id="descricao"]').send_keys(placa)
        sleep(2)                              
        navegador.find_element('css selector', 'div[class="bx-field carteira"]').click()
        sleep(2)
        navegador.find_element('css selector', 'span[class="mat-option-text"]').click()
        sleep(5)
        proximo = navegador.find_element('css selector', 'button[id="previous_page"] span[class="mat-button-wrapper"]').click()
        sleep(5)
        proximo2 = navegador.find_element('css selector', 'button[id="previous_page"] span[class="mat-button-wrapper"]').click()
        sleep(5)
        baixar_boleto = navegador.find_element('css selector', 'button-loader[cssclass="secundary"]').click()
        sleep(5)
        novo_boleto = navegador.find_element('css selector', 'a[class="mat-focus-indicator mat-button mat-button-base"]').click() 
        
        break
                    
if __name__ == '__main__':
    login()
    tipo_boleto()
    tela_boleto()
    emitir_boleto()
    
with open('hoje.txt','w') as arquivo: 
    for valor in emitir_boleto(): 
        arquivo.write(str(valor))       