
from flask import Flask, render_template
import bs4 as bs
import urllib.request
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import matplotlib.cm
import pandas as pd
def scrape(url):
    list=[[],[],[],[],[]]
    l=[]
    sauce =urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(sauce,features='lxml')
    k=soup.find('table',class_="table table-striped")
    sauce =str(k)
    soup=bs.BeautifulSoup(sauce,features='lxml')
    k=soup.find_all('tr')
    for i in k:
        l=[]
        sauce =str(i)
        soup=bs.BeautifulSoup(sauce,features='lxml')
        k1=soup.find_all('td')
        if len(k1)==5:
            for n in range(5):
                l.append(k1[n].text)
            for p in range(5):
                list[p].append(l[p])
    return list
a=scrape('https://www.mohfw.gov.in/')

def convert(x):
    if(x[-1]=='#'):
        return int(x[:-1])
    return int(x)
def convert1(x):
    if(x[-1]=='#'):
        return x[:-1]
    return x

data=map(convert1,a[1])
a[1]=list(data)
data1=map(convert,a[2])

a[2]=list(data1)
data=map(convert,a[3])
a[3]=list(data)
data=map(convert,a[4])
a[4]=list(data)
data=pd.DataFrame({'area':a[1],'count':a[2],'cured':a[3],'deaths':a[4]})
data.loc['area',0]='Andaman & Nicobar Island'
data.loc['area',7]='NCT of Delhi'




fig, ax = plt.subplots(figsize=(10,20))
map=Basemap(
    llcrnrlon=67,
    llcrnrlat=6,
    urcrnrlon=98,
    urcrnrlat=38,
    lat_0=27,
    lon_0=76)
i=map.readshapefile("Igismap\\Indian_States","states",color='#444444',linewidth=2)

df_poly = pd.DataFrame({
        'shapes': [Polygon(np.array(shape), True) for shape in map.states],
        'area': [area['st_nm'] for area in map.states_info]
    })
df_poly = df_poly.merge(data, on='area', how='left')
cmap = plt.get_cmap('Greens')
pc = PatchCollection(df_poly.shapes, zorder=2)
norm = Normalize()

pc.set_facecolor(cmap(norm(df_poly['cured'].fillna(0).values)))
ax.add_collection(pc)

mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

mapper.set_array(df_poly['cured'])
cbar=plt.colorbar(mapper, shrink=0.4)
cbar.ax.set_title('Cured/Discharged/Migrated',color='white')
# plt.legend('')
# ax.set_xlabel('Country Population', size = 8)
ax.axis('off')
plt.rcParams['savefig.facecolor']='#343a40'
plt.rcParams["ytick.color"] = 'white'
plt.rcParams["xtick.color"] = 'white'
plt.savefig('static\\map1.png',bbox_inches='tight')




fig, ax = plt.subplots(figsize=(10,20))
map=Basemap(
    llcrnrlon=67,
    llcrnrlat=6,
    urcrnrlon=98,
    urcrnrlat=38,
    lat_0=27,
    lon_0=76)
i=map.readshapefile("Igismap\\Indian_States","states",color='#444444',linewidth=2)

df_poly = pd.DataFrame({
        'shapes': [Polygon(np.array(shape), True) for shape in map.states],
        'area': [area['st_nm'] for area in map.states_info]
    })
df_poly = df_poly.merge(data, on='area', how='left')
cmap = plt.get_cmap('YlOrRd')
pc = PatchCollection(df_poly.shapes, zorder=2)
norm = Normalize()

pc.set_facecolor(cmap(norm(df_poly['deaths'].fillna(0).values)))
ax.add_collection(pc)

mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

mapper.set_array(df_poly['deaths'])
cbar=plt.colorbar(mapper, shrink=0.4)
plt.rcParams["ytick.color"] = 'white'
plt.rcParams["xtick.color"] = 'white'
cbar.ax.set_title('Deaths',color='white')
# plt.legend('')
# ax.set_xlabel('Country Population', size = 8)
ax.axis('off')
plt.rcParams['savefig.facecolor']='#343a40'
plt.rcParams["ytick.color"] = 'white'
plt.rcParams["xtick.color"] = 'white'
plt.savefig('static\\map2.png',bbox_inches='tight')



fig, ax = plt.subplots(figsize=(10,20))
map=Basemap(
    llcrnrlon=67,
    llcrnrlat=6,
    urcrnrlon=98,
    urcrnrlat=38,
    lat_0=27,
    lon_0=76)
i=map.readshapefile("Igismap\\Indian_States","states",color='#444444',linewidth=2)

df_poly = pd.DataFrame({
        'shapes': [Polygon(np.array(shape), True) for shape in map.states],
        'area': [area['st_nm'] for area in map.states_info]
    })
df_poly = df_poly.merge(data, on='area', how='left')
cmap = plt.get_cmap('Blues')
pc = PatchCollection(df_poly.shapes, zorder=2)
norm = Normalize()

pc.set_facecolor(cmap(norm(df_poly['count'].fillna(0).values)))
ax.add_collection(pc)

mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

mapper.set_array(df_poly['count'])
cbar=plt.colorbar(mapper, shrink=0.4)
plt.rcParams["ytick.color"] = 'white'
plt.rcParams["xtick.color"] = 'white'
cbar.ax.set_title('Active Cases ',color='white')
# plt.legend('')
# ax.set_xlabel('Country Population', size = 8)
ax.axis('off')
plt.rcParams['savefig.facecolor']='#343a40'

plt.savefig('static\\map.png',bbox_inches='tight')





active=sum(a[2])
cured=sum(a[3])
dead=sum(a[4])

a.append(active)
a.append(cured)
a.append(dead)

app = Flask(__name__)

@app.route('/')
def data():

    return render_template('index.html',data=a)

if __name__ == '__main__':
   app.run(debug = True)
