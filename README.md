![Alt text for image](images/your_image.png)
# Uber-time-series-analysis
## 📌 1. Introduction
This project uses my personal Uber trip data (**65 rides**) to explore the **time series elements** in ride cancellations.  
The main question investigated is:  
👉 *“At what times of the day do cancellations usually happen, and how do they compare to completed rides?”*  

---

## 🛠️ 2. Data Preparation
- Converted `request_time` to datetime format.  
- Extracted the **hour of day (0–23)**.  
- Grouped rides by hour and counted trips by status.  
- Defined cancellations as any trip with status = `driver_canceled`, `rider_canceled`, or `failed`.  
- Computed:  
  - **`canceled_total`** = total cancellations per hour  
  - **`total`** = completed rides + cancellations  
  - **`cancel_rate`** = `canceled_total ÷ total`  

---

## 📊 3. Results

### 3.1 Cancellations by Hour (Counts)
- **16:00 → 5 cancellations** (highest in raw numbers)  
- **3:00, 11:00, 14:00 & 17:00 → 4 cancellations each**  

📌 *Afternoons had the most cancellations in total numbers.*  

### 3.2 Cancellation Rate (Proportion)
- **03:00 → 100% canceled**  
- **06:00 → 100% canceled**  
- **19:00 → 100% canceled**  
- **17:00 → 80% canceled**  

📌 *Late night and early morning rides were the riskiest, since most or all trips got canceled.*  

---

## ⏳ 4. Time Series Elements in the Data

- **Trend** → No long-term trend due to small dataset, but short-term clustering in afternoons.  
- **Seasonality** → Daily pattern: cancellations peak at certain hours.  
- **Cycles** → None detected (dataset too short).  
- **Noise** → Random spikes (e.g., 03:00) that don’t follow the main pattern.  

---

## ⚠️ 5. Limitations
- Only **65 rows** → limited statistical power.  
- Covers a **short time span** → no long-term cycles.  
- Data is **personal** → not representative of all Uber users.  

---

## ✅ 6. Conclusion
- **Afternoons** → highest number of cancellations (absolute).  
- **Late night / early morning** → highest cancellation *risk* (proportional).  
- Demonstrates clear **time series elements**: daily seasonality, some noise, and short-term clustering.  
- With more data, stronger insights into long-term trends and cycles could be made.  

---
