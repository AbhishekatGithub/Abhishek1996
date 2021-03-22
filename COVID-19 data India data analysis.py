
# coding: utf-8

# In[118]:


import numpy as np
import folium
import pandas as pd


# In[140]:


location = pd.read_html("http://www.quickgs.com/latitudinal-and-longitudinal-extents-of-india-indian-states-and-cities/") 
coords=pd.DataFrame(location[0])
coords.head()


# In[126]:


covidstats = pd.read_html('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/India_medical_cases_by_state_and_union_territory')
covid_data=pd.DataFrame(covidstats[0])
covid_data=covid_data.iloc[3:39]
covid_data


# In[141]:


def data_pre(cord):
    return cord[0:5]
coords['Latitude']  = coords['Latitude'].apply(data_pre).astype('float')
coords['Longitude'] = coords['Longitude'].apply(data_pre).astype('float')
coords.head()
#coords


# In[142]:


# Renaming Attribute Names for simplicity
covid_data.columns = ['State','Total cases','Deaths','Recoveries','Active cases']
covid_data=covid_data.reset_index(drop=True)
covid_DATA=covid_data.drop([0,5,7,8,17,18,26,31])
covid_DATA=covid_DATA.reset_index(drop=True)
covid_DATA


# In[145]:


final_data = pd.merge(coords, covid_DATA, how ='inner', on ='State')
final_data.head()


# In[148]:


# retreiving the data from final table and plotting it on the INDIA map
# creating the map object zooming on INDIA, location here shows the lat and long of INDIA
India = folium.Map(location = [20.5937,78.9629],zoom_start=4.5)
#adding to map
for state,lat,long,total_cases,Death,Recov,Active in zip(list(final_data['State']),list(final_data['Latitude']),list(final_data['Longitude']),list(final_data['Total cases']),list(final_data['Deaths']),list(final_data['Recoveries']),list(final_data['Active cases'])):
    #for creating circle marker
    folium.CircleMarker(location = [lat,long],
                       radius = 5,
                       color='red',
                       fill = True,
                       fill_color="red").add_to(India)
    #for creating marker
    folium.Marker(location = [lat,long],
                  # adding information that need to be displayed on popup
                  popup=folium.Popup(('<strong><b>State  : '+state+'</strong> <br>' +
                    '<strong><b>Total Cases : '+total_cases+'</striong><br>' +
                    '<strong><font color= red>Deaths : </font>'+Death+'</striong><br>' +
                    '<strong><font color=green>Recoveries : </font>'+Recov+'</striong><br>' +
                    '<strong><b>Active Cases : '+Active+'</striong>' ),max_width=200)).add_to(India)
#to show the map
India

