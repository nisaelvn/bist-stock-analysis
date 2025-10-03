import os
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# --- Ayarlar ---
TICKER = "THYAO.IS"
YIL_SAYISI = 5

# --- Klasörler ---
DATA_DIR = "data"
FIG_DIR = "figures"
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

# --- Tarih aralığı ---
end = datetime.today()
start = end - timedelta(days=365 * YIL_SAYISI)
print(f"[INFO] {TICKER} verisi indiriliyor: {start.date()} → {end.date()}")

# --- Veri çek ---
df = yf.download(TICKER, start=start.date(), end=end.date(), progress=False)
if df.empty:
    print("[UYARI] Veri boş döndü. Sembol doğru mu?")
    raise SystemExit
df = df.dropna()

# --- CSV kaydet ---
csv_path = os.path.join(DATA_DIR, f"{TICKER.replace('.', '_')}.csv")
df.to_csv(csv_path)
print(f"[OK] CSV kaydedildi: {csv_path}")

# --- Kapanış fiyatı ---
plt.figure(figsize=(10,5))
df["Close"].plot(title=f"{TICKER} Kapanış Fiyatı")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")
fig_path = os.path.join(FIG_DIR, f"{TICKER.replace('.', '_')}_close.png")
plt.savefig(fig_path, dpi=150)
plt.close()
print(f"[OK] Grafik kaydedildi: {fig_path}")

# --- Günlük getiri ---
df["Daily Return"] = df["Close"].pct_change()
plt.figure(figsize=(10,5))
df["Daily Return"].plot(title=f"{TICKER} Günlük Getiriler")
plt.xlabel("Tarih")
plt.ylabel("Getiri")
dr_fig = os.path.join(FIG_DIR, f"{TICKER.replace('.', '_')}_daily_returns.png")
plt.savefig(dr_fig, dpi=150)
plt.close()
print(f"[OK] Günlük getiri grafiği kaydedildi: {dr_fig}")

# --- Hareketli ortalamalar ---
df["SMA20"] = df["Close"].rolling(20).mean()
df["SMA50"] = df["Close"].rolling(50).mean()
plt.figure(figsize=(10,5))
df["Close"].plot(label="Close", alpha=0.7)
df["SMA20"].plot(label="SMA20")
df["SMA50"].plot(label="SMA50")
plt.title(f"{TICKER} Fiyat ve Hareketli Ortalamalar")
plt.xlabel("Tarih"); plt.ylabel("Fiyat")
plt.legend()
sma_fig = os.path.join(FIG_DIR, f"{TICKER.replace('.', '_')}_sma.png")
plt.savefig(sma_fig, dpi=150)
plt.close()
print(f"[OK] SMA grafiği kaydedildi: {sma_fig}")

# --- Volatilite ---
df["RollingStd20"] = df["Daily Return"].rolling(20).std() * (252 ** 0.5)
plt.figure(figsize=(10,5))
df["RollingStd20"].plot(title=f"{TICKER} 20 Günlük Yıllıklaştırılmış Volatilite")
plt.xlabel("Tarih")
plt.ylabel("Volatilite")
vol_fig = os.path.join(FIG_DIR, f"{TICKER.replace('.', '_')}_volatility.png")
plt.savefig(vol_fig, dpi=150)
plt.close()
print(f"[OK] Volatilite grafiği kaydedildi: {vol_fig}")

print("\n[SON VERİLER]")
print(df.tail())

# --- Mini rapor (istatistikler) ---
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