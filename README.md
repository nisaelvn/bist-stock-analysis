# 📊 Hisse Senedi Analizi 
Bu proje, Borsa İstanbul (BIST) hisseleri için *Python ile veri toplama, analiz etme ve görselleştirme* örneği sunar.  

---

## 🚀 Kullanılan Teknolojiler
- [Python](https://www.python.org/)  
- [pandas](https://pandas.pydata.org/)  
- [yfinance](https://pypi.org/project/yfinance/)  
- [matplotlib](https://matplotlib.org/)

---

## 📊 Özellikler
- Yahoo Finance üzerinden veri toplama  
- Kapanış fiyatı grafiği  
- Günlük getiri hesaplama ve grafiği  
- 20 ve 50 günlük hareketli ortalamalar (SMA)  
- 20 günlük yıllıklaştırılmış volatilite grafiği  
- Otomatik özet raporu (SUMMARY.md) oluşturma

---

## 📂 Proje Yapısı

Projemin klasör düzeni şu şekilde:

- *data/* → Hisse senedi verilerinin CSV dosyaları burada saklanıyor.  
- *figures/* → Grafikleri burada bulabilirsiniz (kapanış fiyatı, günlük getiriler, SMA, volatilite).  
- *data_fetch_and_eda.py* → Tüm işlemleri yapan Python dosyası.  
- *SUMMARY.md* → Programın otomatik oluşturduğu özet rapor (istatistikler + analiz). 
- README.md → Projenin açıklama dosyası 

---

## ⚙️ Çalıştırma

Önce gerekli kütüphaneleri kurun:
```bash
python -m pip install yfinance pandas matplotlib 
```
Ardından çalıştırın (varsayılan sembol THYAO.IS)
```bash
python data_fetch_and_eda.py 
```

---

## 🔧 Kullanım Örnekleri

Başka bir hisseyi analiz etmek için komut satırında sembol girin:
### ASELS için 
python data_fetch_and_eda.py ASELS

### GARAN için 
python data_fetch_and_eda.py GARAN.IS

### BIMAS için 
python data_fetch_and_eda.py BIMAS

Çalıştırdıktan sonra:
	•	data/ klasörüne CSV dosyası kaydedilir
	•	figures/ klasörüne grafikler kaydedilir
	•	SUMMARY.md dosyasında özet rapor güncellenir



## 📊 Örnek Sonuçlar ve Görseller

### THYAO
| Kapanış Fiyatı | Volatilite |
| --- | --- |
| <img src="figures/THYAO_IS_close.png" width="400"> | <img src="figures/THYAO_IS_volatility.png" width="450"> |

---

### ASELS
| Kapanış Fiyatı | Volatilite |
| --- | --- |
| <img src="figures/ASELS_IS_close.png" width="400"> | <img src="figures/ASELS_IS_volatility.png" width="450"> |

---

### GARAN
| Kapanış Fiyatı | Volatilite |
| --- | --- |
| <img src="figures/GARAN_IS_close.png" width="400"> | <img src="figures/GARAN_IS_volatility.png" width="450"> |

---

### BIMAS
| Kapanış Fiyatı | Volatilite |
| --- | --- |
| <img src="figures/BIMAS_IS_close.png" width="400"> | <img src="figures/BIMAS_IS_volatility.png" width="450"> |

## 📝 Notlar

	•	Varsayılan sembol THYAO.IS / Kod kolayca diğer hisseler için de kullanılabilir:(python data_fetch_and_eda.py ASELS) 
    •   .IS uzantısını yazmasanız da otomatik eklenir (örn: ASELS → ASELS.IS)
	•	Grafikler figures/ klasörüne kaydedilir.
	•	Özet rapor SUMMARY.md dosyasında bulunur. 
