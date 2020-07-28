import geopandas as gpd
from flask import Flask, render_template
import bs4 as bs
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm
import pandas as pd
# def scrape(url):
#     list=[[],[],[],[],[]]
#     l=[]
#     sauce =urllib.request.urlopen(url).read()
#     soup=bs.BeautifulSoup(sauce,features='lxml')
#     k=soup.find('table',class_="table table-striped")
#     sauce =str(k)
#     soup=bs.BeautifulSoup(sauce,features='lxml')
#     k=soup.find_all('tr')
#     c=0
#     for i in k:
#         l=[]
#         sauce =str(i)
#         soup=bs.BeautifulSoup(sauce,features='lxml')
#         k1=soup.find_all('td')
#         if len(k1)==6 and c<=34:
#             c=c+1
#             for n in range(5):
#                 l.append(k1[n].text)
#             for p in range(5):
#                 list[p].append(l[p])
#     return list
#
# def convert(x):
#     if(x[-1]=='#'):
#         return int(x[:-1])
#     return int(x)
# def convert1(x):
#     if(x[-1]=='#'):
#         return x[:-1]
#     return x
#
# a=[]
#
# def run():
#     global a
#     a=scrape('https://www.mohfw.gov.in/')
#
#     data=map(convert1,a[1])
#     a[1]=list(data)
#     data1=map(convert,a[2])
#
#     a[2]=list(data1)
#     data=map(convert,a[3])
#     a[3]=list(data)
#     data=map(convert,a[4])
#     a[4]=list(data)
#     data=pd.DataFrame({'area':a[1],'count':a[2],'cured':a[3],'deaths':a[4]})
#     data.loc[0,'area']='Andaman & Nicobar Island'
#     data.loc[8,'area']='NCT of Delhi'
#
#     fp = "static/Igismap/Indian_States.shp"
#     map_df = gpd.read_file(fp)
#     merged = map_df.set_index('st_nm').join(data.set_index('area'))
#     merged.head()
#     merged.fillna(0,inplace=True)
#
#     fig, ax = plt.subplots(figsize=(10,9))
#     plt.style.use("dark_background")
#
#     ax.axis('off')
#
#     merged.plot(column='cured', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8')
#     mapper = matplotlib.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=data['cured'].max()), cmap='Greens')
#
#     mapper.set_array(data['cured'])
#     cbar=plt.colorbar(mapper)
#     cbar.ax.set_title('Cured/Discharged/Migrated',color='white')
#     plt.rcParams['savefig.facecolor']='#343a40'
#     plt.savefig('static/map1.png',bbox_inches='tight')
#
#
#
#
#     fig, ax = plt.subplots(figsize=(10,9))
#     plt.style.use("dark_background")
#
#     ax.axis('off')
#
#     merged.plot(column='deaths', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8')
#     mapper = matplotlib.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=data['deaths'].max()), cmap='YlOrRd')
#
#     mapper.set_array(data['deaths'])
#     cbar=plt.colorbar(mapper)
#     cbar.ax.set_title('Deaths',color='white')
#     plt.rcParams['savefig.facecolor']='#343a40'
#     plt.savefig('static/map2.png',bbox_inches='tight')
#
#
#
#
#     fig, ax = plt.subplots(figsize=(10, 9))
#     plt.style.use("dark_background")
#
#     ax.axis('off')
#
#     merged.plot(column='count', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
#     mapper = matplotlib.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=data['count'].max()), cmap='Blues')
#
#     mapper.set_array(data['count'])
#     cbar=plt.colorbar(mapper)
#     cbar.ax.set_title('Active Cases',color='white')
#     plt.rcParams['savefig.facecolor']='#343a40'
#     plt.savefig('static/map.png',bbox_inches='tight')
#
#
#
#     active=sum(a[2])
#     cured=sum(a[3])
#     dead=sum(a[4])
#
#     a.append(active)
#     a.append(cured)
#     a.append(dead)

app = Flask(__name__)

@app.route('/')
def data():
    # run()
    # return render_template('maintenance.html',data=a)
    return render_template('maintenance.html')

if __name__ == '__main__':
   app.run(debug = True)
