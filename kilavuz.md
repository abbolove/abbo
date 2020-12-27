## Komutlar ve Kullanım Örnekleri

* komutlarda boşluklar önemli

#### anlık fiyat verisi için 
```
abbo fiyat
```
sürekli işlemdeyken kullanılmalı


#### anlık fiyat ve bazı indikatörlerin 5 dk'lık, 15dk'lık, 1 saatlik ve günlük verisine ulaşmak için
```
abbo veri
```
sürekli işlemdeyken kullanılmalı


#### hangi kademede ne kadar lot alınıp satılmış bilgisi için
```
abbo kademe
```
seans dışında çalışmıyor sanırım


#### grafikli takas verileri için
```
abbo takas grafikli
```
35 günlük değişimleri gösteriyor ve biraz karışık oluyor


#### sadece sayısal takas verileri için
```
abbo takas
```
bugün ve dün arasındaki farkı listeler. örnek olarak 11 günlük fark isteniyorsa eğer
```
abbo takas 11
```
şeklinde yazabilirsiniz. 1-500 arası tam sayı uygundur


#### bedelsiz sermaye arttırımlarında bazı hesaplamalar için
```
abbo bedelsiz lot=200 yüzde=65
```
gibi bir kullanımı var. lot ve yüzde değerlerini kendinize uygun şekilde yazarsınız \
şu anki fiyattan değil de belirli fiyattan bölününce ne oluyor diye bir merakınız varsa
```
abbo bedelsiz lot=1250 yüzde=120 fiyat=23
```
olarak komut verebilirsiniz. 


#### bedelli sermaye arttırımlarında bazı hesaplamalar için
```
abbo bedelli lot=3000 yüzde=75 rhf=1
```
gibi bir kullanımı var. rhf, rüçhan hakkı fiyatı demek \
genelde 1 lira oluyor ama değerleri kendinize uygun şekilde girin \
yine şu anki fiyattan değil de belirli fiyattan bölününce ne oluyor diye bir merakınız varsa
```
abbo bedelli lot=2200 yüzde=46 rhf=1 fiyat=12
```
olarak komut verebilirsiniz


#### grafik çizdirmek için
```
abbo grafik ciz=[bbands()&macd()] 
```
gibi bir kullanımı var. \
periyot ve mum sayısını kendiniz belirleyebilrisiniz
```
abbo grafik ciz=[sma(10)&ema(200)&rsi()] periyot=1d mum=30
```
gibi bir komut verebilirsiniz. mum parametresi için 20-200 arası bir sayı girebilirsiniz \
girmezseniz 60 değerini alır. periyot parametresi için 15, 30, 1h, 5h, 1d, 1w, 1m yazılabilir \
çizdirilecek olan indikatörler köşeli parantez içinde & işareti ile ayrılmalı \
hem indikatörler arasında hem de indikatörlerin parametreleri arasında boşluk olmamalı \
evet bbands()'a falan parametre girişi yapabiliyoruz. nasıl ve hangi indikatörler var? \
[TA-LIB](https://github.com/mrjbq7/ta-lib#indicator-groups) projesinden öğrenebilirsiniz \
komut verirken kolaylık olsun diye inputs şeklinde fiyat verisi girmeyi abbo'da kaldırdım \
yazarsanız abbo hata verir. bu komutta hata verdirmek o kadar kolay ki \
belki bir gün daha sağlam hale getiririm. ama kimin için? ben kullanıyorum aşldsöaşldö

çok kırılgan bir komut olduğu için bazı kısıtlamalar da var
birinci kısıtlama: en fazla 6 indikatör çizdirebilirsiniz
ikinci kısıtlama: [Overlap Studies](https://github.com/mrjbq7/ta-lib/#overlap-studies) harici indikatörlerden en fazla 3 tane çizdirebilirsiniz
neden? çünkü öyle!



#### indikatörlerle hesaplamalar için
```
5h@ (rsi(20)<70)&(bbands(18,3,3)['middleband']>ema(200))
```
gibi çok karışık ve anlatmaktan yorgun düşebileceğim pek çok şey yapabilirsiniz \
5h@ kısmı hangi periyotta hesaplama yapacağımızı beliriyor \
15@, 30@, 1h@, 5h@, 1d@, 1w@ falan yazılabilir. 5@ de yazılabilir muhtemelen \
mantıktaki "ve" yani "and" yerine & işareti,  "ya da" yani "or" yerine | işareti kullanılmalı \
"değil" yani "not" yerine ~ işareti kullanılmalı \
yukarıdaki örnekte 20 mumluk rsi değeri 70ten BÜYÜKSE VE; \
bolinger'in orta bandı 200 günlük ema değerinden BÜYÜKSE; TRUE değerini döndürür \
bu özelliği daha sonra biraz daha açıklarım. çok şey yapılabiliyor



#### tradingview sitesindeki son analizi investing forumuna aktarmak için
```
abbo tv
```
eğer son analizi değil de popüler analizi aktarmak istiyorsanız

```
abbo tv popular
```
ya da 

```
abbo tv populer
```


### goygoy komutlar

#### abbo'nun size yürümesi için
```
abbo sev beni
```

#### şarkı söylemesi için
```
abbo şarkı
```

#### müzik ismi paylaşması için
```
abbo müzik
```

#### halini vaktini sormak için
```
abbo naber
```

#### dedikodu için
```
abbo gıybet
```


### komut olmayan özellikler

* belli saatlerde günaydın, iyi akşamlar der
* sharematriks linki görünce foruma yükler. abbo'nun sevdiği insanlardansanız \
   sonu resim uzantısıyla biten linkleri de foruma yükleyebilir \
   adınızın listede olması lazım bunun için

