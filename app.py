import geopandas as gpd
from flask import Flask, render_template
import bs4 as bs
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm
import pandas as pd


# def convert(x):
#     if(x[-1]=='#'):
#         return int(x[:-1])
#     return int(x)
# def convert1(x):
#     if(x[-1]=='#'):
#         return x[:-1]
#     return x
#
#
def run():
    data = pd.read_json("https://www.mohfw.gov.in/data/datanew.json")
    data.drop(['sno','state_code'],axis=1,inplace = True)
    data["Active since Yesterday"] = data['new_active'] - data['active']
    data["Deaths since Yesterday"] = data['new_death'] - data['death']
    data["Cured since Yesterday"] = data['new_cured'] - data['cured']
    data.loc[0,'state_name']='Andaman & Nicobar Island'
    data.loc[8,'state_name']='NCT of Delhi'

    fp = "static/Igismap/Indian_States.shp"
    map_df = gpd.read_file(fp)
    merged = map_df.set_index('st_nm').join(data.set_index('state_name'))
    merged.head()
    merged.fillna(0,inplace=True)

    fig, ax = plt.subplots(figsize=(10,9))
    plt.style.use("dark_background")

    ax.axis('off')

    merged.plot(column='new_cured', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8')
    mapper = matplotlib.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=data['new_cured'].max()), cmap='Greens')

    mapper.set_array(data['new_cured'])
    cbar=plt.colorbar(mapper)
    cbar.ax.set_title('Cured/Discharged/Migrated',color='white')
    plt.rcParams['savefig.facecolor']='#343a40'
    plt.savefig('static/map1.png',bbox_inches='tight')




    fig, ax = plt.subplots(figsize=(10,9))
    plt.style.use("dark_background")

    ax.axis('off')

    merged.plot(column='new_death', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8')
    mapper = matplotlib.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=data['new_death'].max()), cmap='YlOrRd')

    mapper.set_array(data['new_death'])
    cbar=plt.colorbar(mapper)
    cbar.ax.set_title('Deaths',color='white')
    plt.rcParams['savefig.facecolor']='#343a40'
    plt.savefig('static/map2.png',bbox_inches='tight')




    fig, ax = plt.subplots(figsize=(10, 9))
    plt.style.use("dark_background")

    ax.axis('off')

    merged.plot(column='new_active', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
    mapper = matplotlib.cm.ScalarMappable(norm=plt.Normalize(vmin=0, vmax=data['new_active'].max()), cmap='Blues')

    mapper.set_array(data['new_active'])
    cbar=plt.colorbar(mapper)
    cbar.ax.set_title('Active Cases',color='white')
    plt.rcParams['savefig.facecolor']='#343a40'
    plt.savefig('static/map.png',bbox_inches='tight')

    a=[list(data.index)[1:],data['state_name'][:-1],data['new_active'][:-1],data['new_cured'][:-1],data['new_death'][:-1]]
    active=sum(a[2])
    cured=sum(a[3])
    dead=sum(a[4])

    a.append(active)
    a.append(cured)
    a.append(dead)
    return a

app = Flask(__name__)

@app.route('/')
def data():
    a = run()
    return render_template('index.html',data=a)
    # return render_template('maintenance.html')

if __name__ == '__main__':
   app.run(debug = True)
