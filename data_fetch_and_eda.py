import os
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# --- Hisse Senedi Sembolü (örnek: THYAO.IS, ASELS.IS, BIMAS.IS) ---
TICKER = "THYAO.IS"  # İstediğini buradan değiştirebilirsin

# --- Kaç yıl geriye gidelim ---
YIL_SAYISI = 5

# --- Veri Klasörleri ---
os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)

# --- Tarih Aralığı ---
end = datetime.today()
start = end - timedelta(days=365 * YIL_SAYISI)

print(f"[INFO] {TICKER} verisi indiriliyor: {start.date()} → {end.date()}")

# --- Veri Çekme ---
df = yf.download(TICKER, start=start, end=end)

if df.empty:
    print("[UYARI] Veri indirilemedi. Sembol doğru mu? Örn: ASELS.IS")
else:
    # CSV kaydet
    csv_path = f"data/{TICKER.replace('.', '_')}.csv"
    df.to_csv(csv_path)
    print(f"[OK] CSV kaydedildi: {csv_path}")

    # Grafik kaydet
    plt.figure(figsize=(10,5))
    df["Close"].plot(title=f"{TICKER} Kapanış Fiyatı")
    plt.xlabel("Tarih")
    plt.ylabel("Fiyat")
    fig_path = f"figures/{TICKER.replace('.', '_')}_close.png"
    plt.savefig(fig_path, dpi=150)
    print(f"[OK] Grafik kaydedildi: {fig_path}")

    # Konsolda son 5 satırı göster
    print("\n[SON VERİLER]")
    print(df.tail())
