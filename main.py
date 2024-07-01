from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


caminho = os.getcwd()
arquivo = caminho + r'\login.html'
navegador.get(r'C:\Users\Tiago\Desktop\Projetos Python\Selenium\automação de nota fiscal\login.html')
navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('Tiago')
navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys(12345)
navegador.find_element(By.XPATH, '/html/body/div/form/button').click()


navegador.find_element(By.ID, 'nome').send_keys('Teste')
navegador.find_element(By.NAME, 'endereco').send_keys('Rua um')
navegador.find_element(By.NAME, 'bairro').send_keys('Lagos')
navegador.find_element(By.NAME, 'municipio').send_keys('Rio de janeiro')
navegador.find_element(By.NAME, 'cep').send_keys('25954-532')
navegador.find_element(By.NAME, 'uf').send_keys('RJ')
navegador.find_element(By.NAME, 'cnpj').send_keys(123.456-00)
navegador.find_element(By.NAME, 'inscricao').send_keys(000.00)
navegador.find_element(By.NAME, 'descricao').send_keys('Produto para testes')
navegador.find_element(By.NAME, 'quantidade').send_keys(5)
navegador.find_element(By.NAME, 'valor_unitario').send_keys(2)
navegador.find_element(By.NAME, 'total').send_keys(10)
navegador.find_element(By.XPATH, '//*[@id="formulario"]/button').click()














input('press enter')