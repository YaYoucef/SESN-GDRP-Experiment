# GDPR-Compliant SESN Experimental Setup

We present a Python-based experimental framework to evaluate GDPR-compliant operations in a Spontaneous and Ephemeral Social Network (SESN). The system integrates **BigchainDB** as an immutable audit ledger finalized via **Tendermint BFT consensus**, **MongoDB** for mutable user data, **OpenSSL for encryption and crypto-shredding**, and **Docker** for reproducible deployment.

The objective is to assess how **GDPR requirements—consent management (Art. 7, 21)**, **data access (Art. 15)**, and **right to be forgotten (Art. 17)**—can be enforced efficiently in a decentralized setting. **BigchainDB** ensures transparency and non-repudiation, while **MongoDB** enables low-latency updates and deletions

---

# GDPR-Compliant SESN Experimental Framework

This repository contains the implementation and experimental evaluation of a **GDPR-compliant Spontaneous and Ephemeral Social Network (SESN)**. The system combines **BigchainDB**, **MongoDB**, **OpenSSL**, and **Docker** to evaluate how GDPR rights can be enforced efficiently in decentralized environments.

Each GDPR-related operation is recorded as a signed BigchainDB transaction, ensuring auditability and consistency across nodes. Tendermint provides deterministic finality and tolerates Byzantine failures. MongoDB stores encrypted user profiles, consent state, and key metadata; destroying encryption keys enforces logical deletion without modifying blockchain history.

Deployment relies on Docker containers hosting BigchainDB and MongoDB instances. Multiple BigchainDB nodes are instantiated via docker-compose to emulate a decentralized network.

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


## Interaction Flow

-User triggers CONSENT, ACCESS, or RTBF operation

-Payload is encrypted using OpenSSL

-Transaction is submitted to BigchainDB

-Tendermint executes BFT consensus

-Transaction is finalized and latency logged

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





