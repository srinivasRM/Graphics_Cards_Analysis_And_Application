#Importing all the libraries 
# This for building the front end for user interaction 
import pandas as pd
import numpy as np
#The following libraries were used to scrape data from the website 
import requests
from bs4 import BeautifulSoup
#datetime and scheduler were used to run a function everyday on a given particular time
# import schedule
import datetime as dt


#Function for extracting the information from the online stores
def data_scrraping():
    source = 'https://www.vedantcomputers.com/pc-components/graphics-card?sort=p.price&order=ASC&limit=100'

    # print("after:\n", soup.prettify())

    req = requests.get(source)
    soup = BeautifulSoup(req.content, 'html.parser')

    name = list(soup.find_all('span'))

    graphic_card_model = []
    prices = []
    for y, x in enumerate(name):
        if str(x) == '''<span class="stats-label">Model:</span>''':
            graphic_card_model.append(
                str(name[y + 1]).split('<span>')[1].split('</span>')[0])
            prices.append(
                float(
                    str(name[y + 2]).split(' ')[1].split('₹')[1].split(
                        '</span>')[0].replace(',', '')))

    name_card = list(soup.find_all('img'))

    names_ascending = name_card[23:186:1]

    names_asc = []
    for x in names_ascending:
        if names_asc.count(str(x).split('"')[1]) == 0:
            if str(x).find('Nvidia') >= 0 or str(x).find('RTX') >= 0 or str(
                    x).find('RX') >= 0 or str(x).find('GT') >= 0:
                names_asc.append(str(x).split('"')[1])

    today_date = str(dt.date.today())

    df = pd.DataFrame(columns=['Name', 'Model', 'Price'])

    df['Name'] = names_asc
    df['Model'] = graphic_card_model
    df['Price'] = prices
    df['Date'] = today_date

    x = df['Name'][0].find('GB')

    vram = []
    vram_type = []
    for x, y in enumerate(df['Name']):
        z = df['Name'][x].find('GB')
        q = df['Name'][x].find('DDR')
        if z == -1:
            vram.append(np.NAN)
        else:
            vram.append(str(df['Name'][x][z - 2:z + 2]))
        if q == -1:
            vram_type.append(np.NAN)
        else:
            vram_type.append(str(df['Name'][x][q - 1:q + 5]))

    df['vram'] = vram
    df['vram_type'] = vram_type

    x, y, z = 0, 0, 0
    OC = []
    for x, y in enumerate(df['Name']):
        z = df['Name'][x].find('OC')
        if z == -1:
            OC.append(0)
        else:
            OC.append(1)
    df['feature'] = OC

    x, y, z = 0, 0, 0
    Brand = []
    for x, y in enumerate(df['Name']):
        if df['Name'][x].find('RTX') >= 0 or df['Name'][x].find(
                'GT') >= 0 or df['Name'][x].find('Nvidia') >= 0:
            Brand.append('NVIDEA')
        elif df['Name'][x].find('RX') >= 0:
            Brand.append('AMD')
        else:
            Brand.append(np.NAN)

    df['Brand'] = Brand

    provider = []
    for x, y in enumerate(df['Name']):
        provider.append(df['Name'][x].split(' ')[0])
    df['provider'] = provider


    df.to_csv('raw_data.csv', index=False)
    
# schedule.every().day.at("11:13").do(data_scrraping)

data_scrraping()