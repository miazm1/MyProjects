import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import plotly.graph_objects as go
import streamlit as st

st.title('Google Political Ads in United States')
st.write('This dashboard visualize and analyze the data statistically of Google Political Ads in United States dataset.')
st.write('Created by : Maulana Azmi Izzuddin FTDS-013')
#Section Map distribution total_ads
based_geo_long_lat = pd.read_csv('geo_distribution_data.csv')
based_geo_long_lat.sort_values('total_ads',ascending=True,inplace=True)
based_geo_long_lat.reset_index(inplace=True)
based_geo_long_lat.drop(columns='index',inplace=True)
stages= ["< 4000","4001-4500","4501-5000","5000+"]
tuple1 = (0, based_geo_long_lat[based_geo_long_lat.total_ads <= 4000].index[-1]+1)
tuple2 = (tuple1[1], based_geo_long_lat[(based_geo_long_lat.total_ads > 4000) & (based_geo_long_lat.total_ads <=4500)].index[-1]+1)
tuple3 = (tuple2[1], based_geo_long_lat[(based_geo_long_lat.total_ads > 4501) & (based_geo_long_lat.total_ads <=5000)].index[-1]+1)
tuple4 = (tuple3[1], based_geo_long_lat[based_geo_long_lat.total_ads > 5001].index[-1]+1)
limits = [tuple1, tuple2, tuple3, tuple4]
colors = ["#F4C2C2","#FF6961","#FF1C00","#D73B3E","#A40000", "#321414"]
fig = go.Figure()
stage_counter = 0
for i in range(len(limits)):
    lim = limits[i]
    df_sub = based_geo_long_lat[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['longitude'],
        lat = df_sub['latitude'],
        text = df_sub['name'],
        marker = dict(
            size = df_sub['total_ads']*0.1,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{}'.format(stages[stage_counter])))
    stage_counter = stage_counter+1
fig.update_layout(
        title_text = 'Total Political Ads Distribution In The United States By Geography',
        title_x=0.5,
        showlegend = True,
        legend_title = 'Range Of Total Ads',
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
            projection=go.layout.geo.Projection(type = 'albers usa'),
        )
    )

#Section Map distribution total_spend
based_geo_long_lat.sort_values('total_spend',ascending=True,inplace=True)
based_geo_long_lat.reset_index(inplace=True)
based_geo_long_lat.drop(columns='index',inplace=True)
based_geo_long_lat.drop(columns='Unnamed: 0',inplace=True)

stage_spend= ["< 5.000.000","5.000.001-10.000.000","10.000.001-20.000.000","20.000.001-30.000.000","30.000.001-40.000.000","40.000.001-50.000.000", "50.000.001-60.000.000","60.000.001-70.000.000","70.000.001-80.000.000", "80.000.000+"]
tuple1_spend = (0, based_geo_long_lat[based_geo_long_lat.total_spend <= 5000000].index[-1]+1)
tuple2_spend = (tuple1_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 5000000) & (based_geo_long_lat.total_spend <=10000000)].index[-1]+1)
tuple3_spend = (tuple2_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 10000000) & (based_geo_long_lat.total_spend <=20000000)].index[-1]+1)
tuple4_spend = (tuple3_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 20000000) & (based_geo_long_lat.total_spend <=30000000)].index[-1]+1)
tuple5_spend = (tuple4_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 30000000) & (based_geo_long_lat.total_spend <=40000000)].index[-1]+1)
tuple6_spend = (tuple5_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 40000000) & (based_geo_long_lat.total_spend <=50000000)].index[-1]+1)
tuple7_spend = (tuple6_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 50000000) & (based_geo_long_lat.total_spend <=60000000)].index[-1]+1)
tuple8_spend = (tuple7_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 60000000) & (based_geo_long_lat.total_spend <=70000000)].index[-1]+1)
tuple9_spend = (tuple8_spend[1], based_geo_long_lat[(based_geo_long_lat.total_spend > 70000000) & (based_geo_long_lat.total_spend <=80000000)].index[-1]+1)
tuple10_spend = (tuple9_spend[1], based_geo_long_lat[based_geo_long_lat.total_spend > 80000000].index[-1]+1)

limits_spend = [tuple1_spend, tuple2_spend, tuple3_spend, tuple4_spend, tuple5_spend, tuple6_spend, tuple7_spend, tuple8_spend, tuple9_spend,tuple10_spend]
colors_spend = ["#B2EC5D","#7CFC00","#ACE1AF","#77DD77","#85BB65", "#03C03C","#008000","#78866B","#556B2F","#414833"]
fig_spend = go.Figure()
stage_spend_counter = 0
for i in range(len(limits_spend)):
    lim_spend = limits_spend[i]
    df_sub_spend = based_geo_long_lat[lim_spend[0]:lim_spend[1]]
    fig_spend.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub_spend['longitude'],
        lat = df_sub_spend['latitude'],
        text = df_sub_spend['name'],
        marker = dict(
            size = df_sub_spend['total_spend']*0.00002,
            color = colors_spend[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{}'.format(stage_spend[stage_spend_counter])))
    stage_spend_counter = stage_spend_counter+1
fig_spend.update_layout(
        title_text = 'Total Spending on Political Ads Distribution In The United States By Geography',
        title_x=0.5,
        showlegend = True,
        legend_title = 'Range Of Total Spending in US Dollar',
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
            projection=go.layout.geo.Projection(type = 'albers usa'),
        )
    )
st.header('Google Political Ads Distribution in United States')

a1 = st.radio("Select variable of distribution based on Geography :",['Total Ads','Total Spend'])
if a1 == 'Total Ads':
    st.plotly_chart(fig)
else:
    st.plotly_chart(fig_spend)

show_data = st.checkbox('Show Table Data')
if show_data:
    st.write('Here the Data:')
    if 'number_of_rows' not in st.session_state or 'type' not in st.session_state:
        st.session_state['number_of_rows'] = 5
        st.session_state['type'] = 'Categorical'
    increment = st.button('Show more columns ⬇️')
    if increment:
        st.session_state.number_of_rows +=1
    decrement = st.button('Show less columns ⬆️')
    if decrement:
        st.session_state.number_of_rows -=1
    st.table(based_geo_long_lat.head(st.session_state['number_of_rows']))
# Data ads
ads_data =pd.read_csv('data_ads.csv')
ads_data.drop(columns='Unnamed: 0',inplace=True)

st.subheader('Central Tendency Analysis')
mean_imperesions_per_ads = round(ads_data['impressions_per_ads'].mean(),2)
median_imperesions_per_ads = round(ads_data['impressions_per_ads'].median(),2)
mode_imperesions_per_ads = round(ads_data['impressions_per_ads'].mode(),2)
skew_impressions_per_ads = round(ads_data['impressions_per_ads'].skew(),2)
kurt_impressions_per_ads = round(ads_data['impressions_per_ads'].kurt(),2)
mean_usd_per_ads = round(ads_data['usd_per_ads_day'].mean(),2)
median_usd_per_ads = round(ads_data['usd_per_ads_day'].median(),2)
mode_usd_per_ads = round(ads_data['usd_per_ads_day'].mode(),2)
skew_usd_per_ads = round(ads_data['usd_per_ads_day'].skew(),2)
kurt_usd_per_ads = round(ads_data['usd_per_ads_day'].kurt(),2)

analysis_1 = st.radio(
    "Choose variable for Central Tendency Analysis:",
    ("Impressions per ads per day", "USD per ads per day")
)
if analysis_1 == 'Impressions per ads per day':
    fig_imp = plt.figure(figsize=(16,8))
    sns.distplot(ads_data['impressions_per_ads'],color = 'red').set(title = 'Distribution of Impressions of ads per day in United States',xlabel ='Impressions')
    st.pyplot(fig_imp)
    st.write(f"Mean dari impressions per ads per day {mean_imperesions_per_ads}")
    st.write(f"Median dari impressions per ads per day {median_imperesions_per_ads}")
    st.write(f"Mode dari impressions per ads per day {mode_imperesions_per_ads[0]}")
    st.write(f"Skewness dari impressions per ads per day {skew_impressions_per_ads}")
    st.write(f"Kurtosis dari impressions per ads per day {kurt_impressions_per_ads}")
    show_a2 = st.checkbox('Show Impressions per ads per day Central Tendency Analysis')
    if show_a2:
        st.write("Berdasarkan analisa central tendecy dari jumlah impression per iklan dalam sehari ini memiliki distribusi positive skew yang dimana mean > median. Hal ini berarti total impression lebih banyak frekuensinya di sebelah kiri dari nilai rata-ratanya. Selain itu juga didukung dengan nilai skewness yang positive >0. Selain itu pada distribusi ini sangat runcing atau terpusat mendekati pada 1 value yang dapat dilihat pada distribusi. Setelah dilihat, hal ini didukung karena nilai kurtosis nya yang sangat tinggi.")
        st.write("Rata-rata di US untuk dalam political google ads didapat dalam satu ads per harinya sebanyak 3866 impressions. Dari persebaran data impression per ads per harinya paling banyak frekuensi impressions didapat sebanyak 250 impressions")
else:   
    fig_imp2 = plt.figure(figsize=(16,8))
    sns.distplot(ads_data['usd_per_ads_day'],color='green').set(title = 'Distribution of US Dolar Spend in ads per day in United States',xlabel ='Total Spend in US Dollar')
    st.pyplot(fig_imp2)
    st.write(f"Mean dari USD per ads per day {mean_usd_per_ads}")
    st.write(f"Median dari USD per ads per day {median_usd_per_ads}")
    st.write(f"Mode dari USD per ads per day {mode_usd_per_ads[0]}")
    st.write(f"Skewness dari USD per ads per day {skew_usd_per_ads}")
    st.write(f"Kurtosis dari USD per ads per day {kurt_usd_per_ads}")
    show_a3 = st.checkbox('Show Central USD spend per ads per day Tendency Analysis')
    if show_a3:
        st.write("Berdasarkan analisa central tendecy dari jumlah impression per iklan dalam sehari ini memiliki distribusi positive skew yang dimana mean > median. Hal ini berarti total impression lebih banyak frekuensinya di sebelah kiri dari nilai rata-ratanya. Selain itu juga didukung dengan nilai skewness yang positive >0. Selain itu pada distribusi ini sangat runcing atau terpusat mendekati pada 1 value yang dapat dilihat pada distribusi. Setelah dilihat, hal ini didukung karena nilai kurtosis nya yang sangat tinggi.")
        st.write("Rata-rata di US melakukan spending per ads per harinya untuk political google ads sebanyak 89 US Dollar. Dari persebaran data impression per ads per harinya paling banyak frekuensi spending didapat sebanyak 100 US Dollar.")
st.subheader('Distributions of Total Spend in US dollar with Total Impression')
fig_3 = plt.figure(figsize=(16,8))
plt.scatter(y=ads_data['impressions_per_ads'],x=ads_data['usd_per_ads_day'])
plt.xlabel('Spend in US Dollar')
plt.ylabel('Impressions')
plt.title("The Distributions of Total Spending with Total Impressions ")
st.pyplot(fig_3)
show_a4 = st.checkbox('Show Analysis of the Distributions')
if show_a4:
    st.write("Pada scatter plot di atas, dapat dilihat bahwa pada umumnya di United States untuk setiap organisasi atau individu melakukan budgeting untuk political ads di google untuk 1 iklannya dalam 1 hari di bawah 7.500 US Dollar dengan mendapatkan impression di bawah 300.000 impressions. Walupun terdapat juga tidak banyak berada di angka di atas spend dan impression yang telah disebutkan.")
show_a5 = st.checkbox('Show Table data of the Distributions')
if show_a5:
    st.write('Here the Data:')
    if 'number_of_rows' not in st.session_state or 'type' not in st.session_state:
        st.session_state['number_of_rows'] = 5
        st.session_state['type'] = 'Categorical'
    increment = st.button('Show more columns ⬇️')
    if increment:
        st.session_state.number_of_rows +=1
    decrement = st.button('Show less columns ⬆️')
    if decrement:
        st.session_state.number_of_rows -=1
    st.table(ads_data.head(st.session_state['number_of_rows']))

#Gender
st.header('Target Gender Distribution on Google Political Ads')
based_gender_sum = pd.read_csv('gender.csv')
myexplode = [0.2, 0, 0, 0]
pie_chart = plt.figure(figsize=(8,8))
fig_pie,ax = plt.subplots()
ax.pie(based_gender_sum.persentase, labels = based_gender_sum.gender, explode= [0.2, 0.2, 0.2], colors = ['green','hotpink','blue'],autopct='%1.1f%%')
ax.legend()
ax.axis('equal')
st.pyplot(fig_pie)
show_a1 = st.checkbox('Show Analysis')
if show_a1:
    st.write('Berdasarkan pada pie chart di atas, kita dapat mendapatkan informasi bahwa 80.2 persen dari total ads bertarget pada semua gender, 10.7 persen bertarget pada gender perempuan, dan 8.1 persen bertarget pada gender laki-laki. ')
show_data1 = st.checkbox('Show Data')
if show_data1:
    st.write('Here the Data:')
    based_gender_sum.drop(columns='Unnamed: 0',inplace=True)
    st.table(based_gender_sum)

#Ads type


st.header('Ads Type on Google Political Ads')
text = pd.read_csv('text.csv')
text.drop(columns='Unnamed: 0',inplace=True)
image = pd.read_csv('image.csv')
image.drop(columns='Unnamed: 0',inplace=True)
video = pd.read_csv('video.csv')
video.drop(columns='Unnamed: 0',inplace=True)
st.header('Ads Type Outlier Detection Filtering')
#text
mean_impression_text = text['impressions'].mean()
median_impression_text = text['impressions'].median()
mode_impression_text = text['impressions'].mode()
skew_impression_text = text['impressions'].skew()
kurt_impression_text = text['impressions'].kurt()
var_impression_text = text['impressions'].var()
std_impression_text = text['impressions'].std()
quartiles_impression_text = np.percentile(text['impressions'],[25,50,75])
min_impression_text,max_impression_text = text['impressions'].min(),text['impressions'].max()

IQR_text = quartiles_impression_text[2] - quartiles_impression_text[0]
batas_bawah_text = quartiles_impression_text[0] - 1.5*IQR_text
batas_atas_text = quartiles_impression_text [2] + 1.5*IQR_text

new_text = text.copy()
new_text = np.where(
    new_text['impressions'] > batas_atas_text,
    batas_atas_text,
    np.where(
        new_text ['impressions'] < batas_bawah_text,
        batas_bawah_text,
        new_text ['impressions']
    )
)
st.subheader('Text Ads Type')
analysis_2 = st.radio(
    "Choose Distribution Plot or Box Plot:",
    ("Distribution Plot", "Box Plot")
)
if analysis_2 == "Distribution Plot":
    show_fig1 = st.checkbox('Show before Outlier filtering')
    if show_fig1:
        fig12_before =plt.figure(figsize=(30,20))
        sns.distplot(text['impressions'],color = 'blue').set(title = 'Distribution of Impressions of Text Ads in United States before Outlier Filtering',xlabel ='Impression')
        st.pyplot(fig12_before)
    show_fig2 = st.checkbox('Show after Outlier filtering')
    if show_fig2:
        fig12_after =plt.figure(figsize=(30,20))    
        sns.distplot(new_text).set(title = 'Distribution of Impressions of Text Ads in United States',xlabel ='Impression')
        st.pyplot(fig12_after)    
else:
    show_fig1 = st.checkbox('Show before Outlier filtering')
    if show_fig1:
        fig21_before =plt.figure(figsize=(30,20))
        sns.boxplot(text['impressions']).set(title = 'Boxplot of Impressions of Text Ads in United States',xlabel ='Impression ')
        st.pyplot(fig21_before)
    show_fig2 = st.checkbox('Show after Outlier filtering')
    if show_fig2:
        fig21_after =plt.figure(figsize=(30,20))    
        sns.boxplot(new_text).set(title = 'Boxplot of Impressions of Text Ads in United States',xlabel ='Impression ')
        st.pyplot(fig21_after)  

#image
st.subheader('Image Ads Type')
mean_impression_image = image['impressions'].mean()
median_impression_image = image['impressions'].median()
mode_impression_image = image['impressions'].mode()
skew_impression_image = image['impressions'].skew()
kurt_impression_image = image['impressions'].kurt()
var_impression_image = image['impressions'].var()
std_impression_image = image['impressions'].std()
quartiles_impression_image = np.percentile(image['impressions'],[25,50,75])
min_impression_image,max_impression_image = image['impressions'].min(),image['impressions'].max()

IQR_image = quartiles_impression_image[2] - quartiles_impression_image[0]
batas_bawah_image = quartiles_impression_image[0] - 1.5*IQR_image
batas_atas_image = quartiles_impression_image [2] + 1.5*IQR_image

new_image = image.copy()
new_image = np.where(
    new_image['impressions'] > batas_atas_image,
    batas_atas_image,
    np.where(
        new_image['impressions'] < batas_bawah_image,
        batas_bawah_image,
        new_image['impressions']
    )
)
analysis_3 = st.radio(
    "Choose Distribution Plot / Box Plot:",
    ("Distribution Plot", "Box Plot")
)
if analysis_3 == "Distribution Plot":
    show_fig3 = st.checkbox('Before Outlier filtering')
    if show_fig3:
        fig13_before =plt.figure(figsize=(30,20))
        sns.distplot(image['impressions'],color = 'blue').set(title = 'Distribution of Impressions of image Ads in United States',xlabel ='Impression')
        st.pyplot(fig12_before)
    show_fig4 = st.checkbox('After Outlier filtering')
    if show_fig4:
        fig13_after =plt.figure(figsize=(30,20))    
        sns.distplot(new_image).set(title = 'Distribution of Impressions of image Ads in United States',xlabel ='Impression')
        st.pyplot(fig12_after)    
else:
    show_fig3 = st.checkbox('Before Outlier filtering')
    if show_fig3:
        fig31_before =plt.figure(figsize=(30,20))
        sns.boxplot(image['impressions']).set(title = 'Boxplot of Impressions of image Ads in United States',xlabel ='Impression ')
        st.pyplot(fig31_before)
    show_fig4 = st.checkbox('After Outlier filtering')
    if show_fig4:
        fig31_after =plt.figure(figsize=(30,20))    
        sns.boxplot(new_image).set(title = 'Boxplot of Impressions of image Ads in United States',xlabel ='Impression ')
        st.pyplot(fig31_after)  
#video
st.subheader('Video Ads Type') 
mean_impression_video = video['impressions'].mean()
median_impression_video = video['impressions'].median()
mode_impression_video = video['impressions'].mode()
skew_impression_video = video['impressions'].skew()
kurt_impression_video = video['impressions'].kurt()
var_impression_video = video['impressions'].var()
std_impression_video = video['impressions'].std()
quartiles_impression_video = np.percentile(video['impressions'],[25,50,75])
min_impression_video,max_impression_video = video['impressions'].min(),video['impressions'].max()
           
IQR_video = quartiles_impression_video[2] - quartiles_impression_video[0]
batas_bawah_video = quartiles_impression_video[0] - 1.5*IQR_video
batas_atas_video = quartiles_impression_video [2] + 1.5*IQR_video

new_video = video.copy()
new_video = np.where(
    new_video['impressions'] > batas_atas_video,
    batas_atas_video,
    np.where(
        new_video['impressions'] < batas_bawah_video,
        batas_bawah_video,
        new_video['impressions']
    )
)

analysis_4 = st.radio(
    "Choose Distribution Plot , Box Plot:",
    ("Distribution Plot", "Box Plot")
)
if analysis_4 == "Distribution Plot":
    show_fig5 = st.checkbox('Before filtering outlier')
    if show_fig5:
        fig14_before =plt.figure(figsize=(30,20))
        sns.distplot(video['impressions'],color = 'blue').set(title = 'Distribution of Impressions of video Ads in United States',xlabel ='Impression')
        st.pyplot(fig14_before)
    show_fig6 = st.checkbox('After filtering outlier')
    if show_fig6:
        fig14_after =plt.figure(figsize=(30,20))    
        sns.distplot(new_video).set(title = 'Distribution of Impressions of video Ads in United States',xlabel ='Impression')
        st.pyplot(fig14_after)    
else:
    show_fig5 = st.checkbox('Before filtering outlier')
    if show_fig5:
        fig41_before =plt.figure(figsize=(30,20))
        sns.boxplot(video['impressions']).set(title = 'Boxplot of Impressions of video Ads in United States',xlabel ='Impression ')
        st.pyplot(fig41_before)
    show_fig6 = st.checkbox('After filtering outlier')
    if show_fig6:
        fig41_after =plt.figure(figsize=(30,20))    
        sns.boxplot(new_video).set(title = 'Boxplot of Impressions of video Ads in United States',xlabel ='Impression ')
        st.pyplot(fig41_after)  

#ANOVA Analysis
st.header('ANOVA Analysis on Ads Type')
st.write('Saya ingin menganalisa dengan menggunakan ANOVA pada ketiga variabel tersebut (text, image, video) apakah memiliki kesamaan dalam mendapatkan impression atau statistically significant.')
f_stat,p_value = stats.f_oneway(pd.DataFrame(new_text),pd.DataFrame(new_image),pd.DataFrame(new_video))
show_hyp = st.checkbox('Show hypothesis')
if show_hyp:
    st.write('H0 : Antar Tipe Ads tidak memiliki perbedaan terhadap impression yang di dapat, μtext = μimage = μvideo.')
    st.write('H1 : Antar Tipe Ads memiliki perbedaan significant terhadap impression yang di dapat, μtext != μimage != μvideo.')
show_res = st.checkbox('Show Result and Analysis')
if show_res:
    st.write('P-value:',p_value[0])
    st.write('f-stat:',f_stat[0])
    st.write('Sehingga didapat p-value < 0,05, maka H0 di reject.')
    st.write('Dapat disimpulkan bahwa terdapat perbedaan statistically significant antara Ads Type Text, Image, dan Video terhadap impressions yang di dapat.')

# Mean,max,min
#st.header('ANOVA Analysis on Ads Type')
mean_m=[round(new_text.mean(),2),round(new_image.mean(),2),round(new_video.mean(),2)]
min_m=[round(new_text.min(),2),round(new_image.min(),2),round(new_video.min(),2)]
max_m =[round(new_text.max(),2),round(new_image.max(),2),round(new_video.max(),2)]
data_mean_min_max_type = pd.DataFrame()
data_mean_min_max_type['Text'] = [round(new_text.mean(),2),round(new_text.min(),2),round(new_text.max(),2)]
data_mean_min_max_type['Image'] = [round(new_image.mean(),2),round(new_image.min(),2),round(new_image.max(),2)]
data_mean_min_max_type['Video'] = [round(new_video.mean(),2),round(new_video.min(),2),round(new_video.max(),2)]
data_mean_min_max_type = data_mean_min_max_type.set_axis(['Average','Minimum','Maximum'])

fig_bar = data_mean_min_max_type.plot(kind='bar',stacked = True, title = 'Ads Type Comparison in Average, Minimum, and Maximum')
fig_rab = fig_bar.get_figure()
st.pyplot(fig_rab)
show_ana = st.checkbox('Show Analysis of Comparison')
if show_ana:
    st.write('Sehingga dapat dilihat pada barplot bahwa proporsi impression yang di hasilkan dari tiap ads type. Di dapatkan bahwa ads type video memiiki impression rata-rata dan maximum tertinggi, lalu diikuti oleh Image, kemudian yang terakhir adalah Text. Untuk Minimum memiliki value yang sama yaitu 1000 impression.')

st.subheader("Relation between Impression and Spending (US Dollar)")
based_ads_type = pd.read_csv('colorplot.csv')
scat = plt.figure(figsize=(20,20))
fig_scat,axs = plt.subplots()
plt.style.use('ggplot')
plt.title('Relation between Impression and Spending (US Dollar)')
plt.xlabel('Spending (US Dollar)')
plt.ylabel('Impressions')
axs.scatter(x=based_ads_type['spend_usd'],y=based_ads_type['impressions'],s=50,c=based_ads_type['color'],alpha=0.3,marker='o',label = {'Text' : 'blue', 'Image': 'black', 'Video': 'red'})
plt.legend() 
st.pyplot(fig_scat)
show_analy = st.checkbox('Show Analysis between Ads Type')
if show_analy:
    st.write('Berdasarkan scatter plot di atas bahwa, pada data political_ads ini banyak yang spending besar pada ads tipe Text dengan impressions yang di dapat tidak cukup besar, berbeda dengan ads_type Image dan Video, dimana spending yang dikeluarkan lebih kecil dibanding text, tetapi memiliki impressions yang lebih besar.')
show_a7 = st.checkbox('Show Table data of Ads Type')
if show_a7:
    st.write('Here the Data:')
    if 'number_of_rows' not in st.session_state or 'type' not in st.session_state:
        st.session_state['number_of_rows'] = 5
        st.session_state['type'] = 'Categorical'
    increment = st.button('Show more columns ⬇️')
    if increment:
        st.session_state.number_of_rows +=1
    decrement = st.button('Show less columns ⬆️')
    if decrement:
        st.session_state.number_of_rows -=1
    st.table(based_ads_type.head(st.session_state['number_of_rows']))
st.header('Reference Dataset')
st.write('Google Poltical Ads Dataset = https://console.cloud.google.com/marketplace/details/transparency-report/google-political-ads')