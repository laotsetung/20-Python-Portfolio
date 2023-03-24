from bs4 import BeautifulSoup as bfs
import requests
import PySimpleGUI as sg
import webbrowser

url = "https://www.mercadolivre.com.br/ofertas#nav-header"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

site = requests.get(url, headers=headers) #request (HTTP GET)

sopa = bfs(site.content, 'html.parser') #Abre o BeatifulSoup com o request que foi feito

m = sopa.main

li = m.find_all('li') #Seleciona os elementos <li> (produtos)
#Cria as variaveis que irão guardar nome, valor, desconto e link (+ contador)
produtos = []
preco = []
desconto = []
links = []
c=0

for d in li: #ABRE TODOS OS ELEMENTOS <li> do HTML
    lin = d.find_all('a')
    for l in lin: #BUSCA TODOS OS ELMENTOS <a> dentro dos <li>
        if 'promotion-item__link-container' in l['class']:
            links.append(l['href']) #guarda o link do produto
            break
        else:
            pass

    img = d.find('img')
    if(img != None): #Busca a imagem, para pegar no atributo ALT o nome do produto
        x = str(img['alt'])
        produtos.append(x[:75]) #Guarda o nome do produto

        div = d.find_all('div') #Busca todas as DIVS dentro do elemento <li>

        for d1 in div:
            if 'class' in d1.attrs: #Se a DIV tem atributo class
                if 'andes-money-amount-combo__main-container' in d1['class']: #Se o class = div que contem o valor
                    
                    span = d1.find_all('span') #Busca todos os spans dentro da div que contém o valor
                    for s in span:
                        if 'class' in s.attrs: #Se a span contém atributo class
                            if 'andes-money-amount__fraction' in s['class']: #Se a SPAN é a que tem o VALOR, guarda o valor
                                preco.append(s.string)

                            if 'andes-money-amount__discount' in s['class']: #Se a SPAN é o que tem o desconto (%), guarda o desconto
                                desconto.append(s.string)

    c += 1
    if (c > 50): #Limite de produtos maximo
        break   

#Font , thema e cor da fonte
font = ('Courier New', 14, 'underline')
font2 = ('Courier New', 24)
sg.theme('DarkTeal10')
sg.theme_text_color('#77aa77')

#Titulo e Botao sair
layout = [[sg.Column([[sg.Text("OFERTAS DO DIA : MERCADO LIVRE", font=font2)]]),sg.Column([[sg.Button("Sair",font=font2)]])]]

#Abre todas as promoções e cria um link para ela
for c, prod in enumerate(produtos):
    try:
        pre = preco[c]
    except:
        pre = 'erro!'

    try:
        des = desconto[c]
    except:
        des = 'erro!'
    
    txt = 'R$'+ pre + ' | ' + prod + ' | ' + des
    
    layout += [[sg.Column([[sg.Text('R$'+pre, tooltip=f'R${pre}', enable_events=True, font=font, key=f'URL {links[c]}')]]),
    sg.Column([[sg.Text(prod, tooltip=f'R${pre}', enable_events=True, font=font, key=f'URL {links[c]}')]]),
    sg.Column([[sg.Text(des, tooltip=f'R${pre}', enable_events=True, font=font, key=f'URL {links[c]}')]])]]

window = sg.Window("OFERTAS MERCADO LIVRE", layout, margins=(25,25), font=font, location=(150,25))

while True:
    event, values = window.read()

    if event == "Sair" or event == sg.WIN_CLOSED:
        break
    elif event.startswith("URL "):
        url = event.split(' ')[1]
        webbrowser.open(url)

window.close()