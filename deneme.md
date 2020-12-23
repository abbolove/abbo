# Komutlar ve Kullanım Örnekleri

* komutlarda boşluklar önemli

### anlık fiyat verisi için 
```
abbo fiyat
```
sürekli işlemdeyken kullanılmalı


### anlık fiyat ve bazı indikatörlerin 5 dk'lık, 15dk'lık, 1 saatlik ve günlük verisine ulaşmak için
```
abbo veri
```
sürekli işlemdeyken kullanılmalı


### hangi kademede ne kadar lot alınıp satılmış bilgisi için
```
abbo kademe
```
seans dışında çalışmıyor sanırım


### grafikli takas verileri için
```
abbo takas grafikli
```
35 günlük değişimleri gösteriyor ve biraz karışık oluyor


### sadece sayısal takas verileri için
```
abbo takas
```
bugün ve dün arasındaki farkı listeler. örnek olarak 11 günlük fark isteniyorsa eğer\
```
abbo takas 11
```
şeklinde yazabilirsiniz. 1-500 arası tam sayı uygundur


### bedelsiz sermaye arttırımlarında bazı hesaplamalar için
```
abbo bedelsiz lot=200 yüzde=65
```
gibi bir kullanımı var. lot ve yüzde değerlerini kendinize uygun şekilde yazarsınız \
şu anki fiyattan değil de belirli fiyattan bölününce ne oluyor diye bir merakınız varsa
```
abbo bedelsiz lot=1250 yüzde=120 fiyat=23
```
olarak komut verebilirsiniz. 


### bedelli sermaye arttırımlarında bazı hesaplamalar için
```
abbo bedelli lot=3000 yüzde=75 rhf=1
```
gibi bir kullanımı var. rhf, rüçhan hakkı fiyatı demek \
genelde 1 lira oluyor ama değerleri kendinize uygun şekilde girin \
yine şu anki fiyattan değil de belirli fiyattan bölününce ne oluyor diye bir merakınız varsa\
```
abbo bedelli lot=2200 yüzde=46 rhf=1 fiyat=12
```
olarak komut verebilirsiniz






07) abbo grafik ciz=[bbands()&macd()...&rsi(20)] periyot=1h mum=20
    istenilen indikatörlere göre grafik çizer.
    hem kendisi sıkıntılı bir komut. hem de anlatması sıkıntılı.
    öncelikle "mum" parametresini yazmak zorunlu değil.
    20-200 arası bir değer girebilirsiniz. girmezseniz 60 değerini alır
    "periyot" parametresini yazmak da zorunlu değil.
    15, 30, 1h, 5h, 1d, 1w, 1m yazılabilir. yazmazsanız günlük değeri alır.
    "ciz" içerisinde boşluksuz şekilde indikatör fonksiyonları & işareti ile ayrılmalı
    peki hangi indikatörler var?
    https://github.com/mrjbq7/ta-lib#indicator-groups
    buradaki indikatörler var. ama kullanırken indikatör isimlerini küçük harfle yazın
    indikatör fonksiyonları değişik ve farklı sayıda parametre alabilir.
    indikatörlere parametre girmek zorunlu değil. hepsinin default değerleri var
    genellikle tradingview ve investing.com'daki gibi kullanımları var.
    ema(20) yazarsan 20 günlük ema'yı hesaplar. 
    normalde macd(12,26,9) kullanılır ama macd() gibi ya da 
    macd(10,30,10) gibi yazabilirsin mesela seçebeğin bol
    indikatör kullanımları ta-lib'li linkten araştırılabilir
    bu bot'ta kolaylık olsun diye her seferinde "inputs" yazılmasını kaldırdım
    stoch(inputs,5,3,0,3,0) yazarsanız bot hata verir
    stoch(5,3,0,3,0) yazarsan vermez. stoch() yazarsan vermez

08) abbo tv
    tradingviewdeki son analizi forumda paylaşır. görselli.
09) abbo sev beni
    goygoy komutu. sana "yürür"
10) abbo şarkı
    goygoy komutu. şarkı söyler
11) abbo müzik
    goygoy komutu. müzik ismi paylaşır
12) abbo gıybet
    goygoy komutu. dedikodu yapar.
    "abbo gıybet kötü" dersen kötü anlamda "abbo gıybet iyi" dersen iyi anlamda
    sadece "abbo gıybet" dersen rastgele
13) abbo naber
    goygoy komutu. rastgele bir cevap seçer yazar 

14) abbo laklak
    sadece benim kullanabildiğim komut. forumda en çok konuşanları listeliyor
15) abbo haber
    sadece benim kullanabildiğim komut. 
    bloomberghtteki son dakika haberlerini paylaşıyor

komut olmayan özellikler

- belli saatlerde selam-sabah işlerini yapar
- sharematriks linki görünce foruma yükler. abbo'nun sevdiği insanlardansanız
    sonu resim uzantısıyla biten linkleri de foruma yükleyebilir.
    adınızın listede olması lazım bunun için
- hesap makinesi özelliği de vardı ama şimdilik kaldırdım. belki eklerim
