# GDPR-Compliant SESN Experimental Setup

This repository provides a **Python-based experimental framework** for evaluating GDPR-compliant operations in a **Spontaneous and Ephemeral Social Network (SESN)** using **BigchainDB**, **MongoDB**, **OpenSSL**, and **Docker**.

---

# GDPR-Compliant SESN Experimental Framework

This repository contains the implementation and experimental evaluation of a **GDPR-compliant Spontaneous and Ephemeral Social Network (SESN)**. The system combines **BigchainDB**, **MongoDB**, **OpenSSL**, and **Docker** to evaluate how GDPR rights can be enforced efficiently in decentralized environments.

## ✨ Key Features
- GDPR-compliant data management for SESNs
- Crypto-shredding for Right to be Forgotten (Art. 17)
- Fast encrypted data access (Art. 15)
- Immutable consent audit trail (Art. 7 & 21)
- Docker-based reproducible deployment

## 🧱 Architecture Overview
- **BigchainDB**: Immutable ledger for consent metadata
- **MongoDB**: Storage for encrypted personal data
- **OpenSSL**: Cryptographic key management
- **Python**: Workload generation and experimentation

## 📁 Project Structure

SESN-GDPR-Experiment/
├── docker/
├── scripts/
├── data/
├── results/
└── requirements.txt


## ⚙️ Setup Instructions
### 1. Start backend services

docker-compose up -d


### 2. Install Python dependencies


pip install -r requirements.txt


### 3. Generate synthetic dataset


python scripts/user_generator.py


### 4. Run workload experiments

python scripts/workload_generator.py


### 5. Generate plots and statistics

python scripts/plot_latency.py
python scripts/statistics.py


## 📊 Metrics Collected

* Average latency per GDPR operation
* Latency variability under load


## 🔬 Experimental Parameters

* Dataset size: 10,000 users
* Load levels: 100, 1,000, 5,000, 10,000 requests
* Metrics: latency (seconds)



## 👤 data/users.json (Sample Content)

[
  {
    "user_id": "9f8b7a2e-41c5-4b92-a9b2-0eab3c5b11d9",
    "name": "User4821",
    "email": "user4821@sesn.org",
    "public_key": "keys/9f8b7a2e-41c5-4b92-a9b2-0eab3c5b11d9_public.pem",
    "private_key": "keys/9f8b7a2e-41c5-4b92-a9b2-0eab3c5b11d9_private.pem",
    "consent": {
      "data_processing": true,
      "profiling": false,
      "sharing": true
    }
  }
]


🔹 *Note:* The real file contains **10,000 entries** with the same structure.



## 📈 results/latency_logs.csv (Sample Content)

operation,requests,latency
RTBF,100,0.00198
RTBF,100,0.00211
DAR,100,0.00153
DAR,100,0.00160
CONSENT,100,0.00237
CONSENT,100,0.00244
RTBF,1000,0.00202
DAR,1000,0.00158
CONSENT,1000,0.00241
```

