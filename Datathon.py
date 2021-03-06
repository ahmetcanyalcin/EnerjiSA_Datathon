#####################################################
# EnerjiSA Veri Maratonu
#####################################################

# Store Item Demand Forecasting Challenge
# https://www.kaggle.com/c/enerjisa-enerji-veri-maratonu/overview/evaluation


#İş Problemi

# Paylaşılan veri setinde 01.01.2019 – 30.11.2021 arasında Başkent bölgesinde yer alan lisanssız güneş santrallerinin saatlik bazda toplam üretim miktarları verilmiştir. Bu bölge içerisinde Ankara, Çankırı, Kırıkkale, Bartın, Karabük, Kastamonu, Zonguldak illerinde yer alan toplam 848 santral bulunmaktadır. Toplam üretime ek olarak; üretim ağırlığı Ankara ilinde olduğu için Ankara ilinin sıcaklık değişkenleri 01.01.2019 – 31.12.2021 tarih aralığında paylaşılmıştır.

#Paylaşılan verilere ek olarak açık kaynaklı veri kaynaklarından veri kullanarak veri zenginleştirme yapılabilir.
#Tahmin edilmesi istenen tarih aralığı 01.12.2021 – 31.12.2021 olarak belirlenmiştir.


# Veri Seti Hikayesi

#DateTime: Sıcaklık değişkenlerinin gözlemlendiği saat aralığını belirtir.
#AirTemperature: Saat aralığındaki hava sıcaklığını Celsius biriminde belirtir.
#ComfortTemperature: Saat aralığındaki hissedilen hava sıcaklığını Celsius biriminde belirtir.
#RelativeHumidity: Saat aralığındaki nem oranını belirtir.
#WindSpeed: Saat aralığındaki rüzgar hızını km/s biriminde belirtir.
#WindDirection: Saat aralığındaki rüzgar yönünü belirtir.
#WWCode: Saat aralığındaki hava durumu kodunu belirtir.
#EffectiveCloudCover: Saat aralığındaki bulutluluk oranını sekizlik ölçü birimi cinsinden belirtir.



#Veri Setinin Çağarılması
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
warnings.filterwarnings('ignore')

df = pd.read_csv('EnerjiSA Data/Veri_Setleri/temperature.csv', parse_dates=['DateTime'], sep=';')

#*****    EDA (Keşifsel veri Analizi)   *****

df.head()

#Bu kısımda kendi yazdığımız fonksiyon ile Veri Setini keşfetmeyi hedefliyoruz.
def check_df(dataframe, head=10):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

#Yapılan kontrollerde veri setinde NaN değerler olduğu görüldü. Bu değerler .cvs dosyasından boş geliyor. Dolayısıyla bu boş değerleri veri setinden çıkarmak bir sorun yaratmayacaktır.
#NaN değerleri hangi satırdan sonra geliyor görmek istedik.
display(df.iloc[26295:26315])

#Boş satır olarak yer alan verileri(26304'den sonrası) sildik.
df = pd.concat([df.iloc[:26304].reset_index(drop=True)], axis=1)


#Veri setini tekrar kontrol ediyoruz.
check_df(df)
# Hala WWCode'da 6254 boş değer görünüyor.
###################### NA #####################
#DateTime                  0
#AirTemperature            0
#ComfortTemperature        0
#RelativeHumidity          0
#WindSpeed                 0
#WindDirection             0
#WWCode                 6254
#EffectiveCloudCover       0