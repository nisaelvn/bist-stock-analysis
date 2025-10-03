[13:53, 03.10.2025] Nisa: # --- Mini rapor (istatistikler) ---
summary = {
    "son_tarih": str(df.index.max().date()),
    "son_fiyat": float(df["Close"].iloc[-1]),
    "ortalama_getiri(%)": float(df["Daily Return"].mean() * 100),
    "std_getiri(%)": float(df["Daily Return"].std() * 100),
    "yillik_volatilite(%)": float(df["RollingStd20"].iloc[-1] * 100),
}

# SMA kesişimleri (son 2 yıl)
cross = (df["SMA20"] > df["SMA50"]).astype(int).diff()
golden = df.index[cross == 1]   # yukarı kesişim
death  = df.index[cross == -1]  # aşağı kesişim

lines = [
    "# THYAO.IS – Otomatik Özet\n",
    f"- Son tarih: {summary['son_tarih']}",
    f"- Son kapanış: {summary['son_fiyat']:.2f}",
    f"- Ortalama günlük getiri: {summary['ortalama_getiri(%)']:.3f}%",
    f"- Günlük getiri std: {summary['std_getiri(%)']:.3f}%",
    f"- 20g yıllıklaştırılmış volatilite: {summary['yillik_volatilite(%)']:.2f}%",
    f"- Golden cross sayısı: {len(golden)}",
    f"- Death cross sayısı: {len(death)}",
    "\n*Golden cross tarihleri (ilk 5):*",
    *[f"- {d.date()}" for d in list(golden[-5:])],
    "\n*Death cross tarihleri (ilk 5):*",
    *[f"- {d.date()}" for d in list(death[-5:])],
]

with open("SUMMARY.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("[OK] SUMMARY.md oluşturuldu.")
[14:04, 03.10.2025] Nisa: # Hisse Senedi Analizi (THYAO.IS Örneği)

Bu proje, Borsa İstanbul hisseleri için *Python ile veri çekme, analiz etme ve görselleştirme* örneği sunar.  
İlk testimizde *Türk Hava Yolları (THYAO.IS)* kullanılmıştır.

---

## 🚀 Kullanılan Teknolojiler
- [Python](https://www.python.org/)  
- [pandas](https://pandas.pydata.org/)  
- [yfinance](https://pypi.org/project/yfinance/)  
- [matplotlib](https://matplotlib.org/)

---

## 📊 Özellikler
- Yahoo Finance üzerinden veri çekme  
- Kapanış fiyatı grafiği  
- Günlük getiri hesaplama ve grafiği  
- 20 ve 50 günlük hareketli ortalamalar (SMA)  
- 20 günlük yıllıklaştırılmış volatilite grafiği  
- Otomatik özet raporu (SUMMARY.md)

---

## 📂 Proje Yapısı

Projemin klasör düzeni şu şekilde:

- *data/* → Hisse senedi verilerinin CSV dosyaları burada saklanıyor.  
- *figures/* → Grafikleri burada bulabilirsiniz (kapanış fiyatı, getiriler, SMA, volatilite).  
- *data_fetch_and_eda.py* → Tüm işlemleri yapan Python dosyası.  
- *SUMMARY.md* → Programın otomatik oluşturduğu özet rapor (istatistikler + analiz). 