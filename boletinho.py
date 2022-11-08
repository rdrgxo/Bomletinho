from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Firefox()
navegador.get('https://app.empresas.bs2.com/bs2/autenticacao')

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
    
    sleep(5)
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
    
def tratar_mes(mes):
    meses_extenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    mes_tratado = ''

    for pos, var in enumerate(meses_extenso):
        if pos == int(mes)-1:
            mes_tratado = var
            return mes_tratado    
      
      
def emitir_boleto():
    
    planilha = pd.read_excel(r'D:\boletinho\lojistas.xlsx')
    data_vencimento = (input('Digite a data de vencimento: \n'))
    
    dia = int(data_vencimento[0:2])
    mes = data_vencimento[3:5]
    ano = data_vencimento[6::]
    
    mes1 = tratar_mes(mes)
    
    resto = (f'"{dia} de {mes1} de {ano}"]')
    td = (f"td[aria-label={resto}")
    
    locator = td
    
    for i, Cnpj in enumerate(planilha["Cnpj"]): 
        print(planilha) 
        Controle = planilha.loc[i, "Controle"]
        Valor = planilha.loc[i, "Valor"]
        if Valor == 0:
         break   
        placa = planilha.loc[i, "Placa"]
     
        sleep(5)
        valor =  navegador.find_element('css selector','input[name="valorcobranca"]').send_keys(str(Valor))
        sleep(2)
        calendario = navegador.find_element('css selector', 'input[id="dataVencimento"]').click()
        sleep(2)
        data_pagamento =  navegador.find_element('css selector', locator).click()
        sleep(2)            
        Controle = navegador.find_element('css selector','input[name="seuNumero"]').send_keys(str(Controle))
        sleep(5)
        Cnpj = navegador.find_element('css selector','input[name="nome"]').send_keys(Cnpj)
        sleep(5)
        sacado = navegador.find_element('css selector','span[class="mat-option-text"] div[class="text _mask ng-star-inserted"]').click()
        sleep(5)
        info_placa = navegador.find_element('css selector','textarea[id="descricao"]').send_keys(placa)
        sleep(5)                              
        navegador.find_element('css selector', 'div[class="bx-field carteira"]').click()
        sleep(5)
        navegador.find_element('css selector', 'span[class="mat-option-text"]').click()
        sleep(5)
        proximo = navegador.find_element('css selector', 'button[id="previous_page"] span[class="mat-button-wrapper"]').click()
        sleep(5)
        proximo2 = navegador.find_element('css selector', 'button[id="previous_page"] span[class="mat-button-wrapper"]').click()
        sleep(5)
        baixar_boleto = navegador.find_element('css selector', 'button-loader[cssclass="secundary"]').click()
        sleep(5)
        novo_boleto = navegador.find_element('css selector', 'a[class="mat-focus-indicator mat-button mat-button-base"]').click() 
        
    print(Cnpj)
    
if __name__ == '__main__':
    login()
    tipo_boleto()
    tela_boleto()
    emitir_boleto()
    tratar_mes()
