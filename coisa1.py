import requests
import hashlib
from bs4 import BeautifulSoup

class Downloader:

    def obtem_pagina_de_caderno_de_data_especifica(self, data):
        data_padronizada = self.verifica_padrao_de_data(data)
        ano_personalizado = data[0:4]
        print(ano_personalizado)
        url = (
            'http://portal.stf.jus.br/servicos/dje/'
            'listarDiarioJustica.asp?tipoVisualizaDJ=periodoDJ'
            '&txtNumeroDJ='
            f'&txtAnoDJ={ano_personalizado}'
            f'&dataInicial={data_padronizada}'
            f'&dataFinal={data_padronizada}'
            '&tipoPesquisaDJ=&argumento='
        )
        print(url)
        
    def verifica_padrao_de_data(self, data):
        #como implementar?
        return data
        
    def obtem_caminho_para_acessar_pdfs_dos_cadernos(self):
        # utiliza-se da data e do numero do diario para montar o link
        # https://www.stf.jus.br/arquivo/djEletronico/DJE_20220217_032.pdf

        url = (f'http://portal.stf.jus.br/servicos/dje/listarDiarioJustica.asp?tipoVisualizaDJ=periodoDJ&txtNumeroDJ=&txtAnoDJ=2022&dataInicial=2022-02-18&dataFinal=2022-02-18&tipoPesquisaDJ=&argumento=')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'}
        response = requests.get(url, headers=headers)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        # valor = soup.find_all('td')


        pass

    def obtem_os_pdfs(self):
        # mesmo processo anterior
        pass

    def baixa_os_pdfs(self):
        # r = requests.get(url, headers=headers)
        pass

    def obtem_os_md5s_dos_cadernos(self):
        # for data in r.iter_content():
        #   m.update(data)
        # print(f'{m.hexdigest()}')
        pass

    def salva_pdfs(self):
        pass


downloader = Downloader()
data_usuario = input('Insira no formato AAAA-MM-DD: ')
# downloader.obtem_pagina_de_caderno_de_data_especifica(data_usuario)
downloader.obtem_caminho_para_acessar_pdfs_dos_cadernos()


# - acessar o site (http://www.stf.jus.br)
# - acessar (http://portal.stf.jus.br/servicos/dje/listarDiarioJustica.asp?tipoVisualizaDJ=ultimoDJ)
# - acessar (http://portal.stf.jus.br/servicos/dje/pesquisarDiarioJustica.asp)
# - pesquisar por data e informar a data de inicio e fim 
# - exemplo de site que retorna (http://portal.stf.jus.br/servicos/dje/listarDiarioJustica.asp?tipoVisualizaDJ=periodoDJ&txtNumeroDJ=&txtAnoDJ=2022&dataInicial=2022-02-16&dataFinal=2022-02-16&tipoPesquisaDJ=&argumento=)
# - existem dois links para possiveis cadernos
# - primeiro link(http://portal.stf.jus.br/servicos/dje/listarDiarioJustica.asp?tipoVisualizaDJ=numeroDJ&txtNumeroDJ=30&txtAnoDJ=2022)
#     - retorna uma pagina com caderno na integra ou paginado
# - segundo link(http://portal.stf.jus.br/servicos/dje/listarDiarioJustica.asp?tipoVisualizaDJ=numeroDJ&txtNumeroDJ=0&txtAnoDJ=)
#     - retorna um erro (500)
# - a primeira opçao(integral) do primeiro link retorna um caderno(pdf)(https://www.stf.jus.br/arquivo/djEletronico/DJE_20220215_030.pdf)
# - baixar o caderno[fim]

# - obter o md5 do caderno baixado
# - salvar o caderno localmente. O nome do caderno será o md5
