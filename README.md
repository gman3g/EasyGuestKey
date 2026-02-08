# EasyGuestKey
EasyGuestKey is an automated Wi-Fi rotation system that generates a fresh guest password, updates a MikroTik hAP ax³ router via SSH, and deploys a joinable QR code to a Google Cloud Platform (GCP) hosted portal.

## 🚀 Overview
Secure Rotation: Generates high-entropy secrets using Python's secrets module.

MikroTik Integration: Updates RouterOS v7 wifi security profiles via SSH using Ed25519 keys.

Automated QR: Generates a specialized WIFI:S:SSID;T:WPA;P:PASSWORD;; QR code and uploads it to a GCP Cloud Storage bucket.

Access Control: Designed to work behind an Identity-Aware Proxy (IAP) secured web frontend.

## 🛠️ Tech Stack
Language: Python 3.13

Libraries: paramiko (SSH), qrcode (Image Gen), google-cloud-storage

Hardware: MikroTik hAP ax³ (RouterOS v7.12+)

Cloud: Google Cloud Functions & Cloud Scheduler

## 📋 Prerequisites
MikroTik Setup:

Enable SSH on a non-standard port (e.g., 2222).

Create a dedicated automation user with minimal policies.

Import your Ed25519 public key to /system/user/ssh-keys.

GCP Setup:

Create a Cloud Storage bucket for the QR image.

Store your SSH private key in GCP Secret Manager.

Ensure the Service Account has Storage Object Admin permissions.

## 🔧 Installation
Bash
# Clone the repository
```text
git clone https://github.com/gman3g/EasyGuestKey.git
```

# Install dependencies

Requirements during development testing
```
pip install -r requirements-dev.txt
```


Requirements in GCP
```
pip install -r requirements.txt
```
## ⚙️ Configuration
Update your environment variables or config.py:

```
ROUTER_IP: Your MikroTik's DDNS address (e.g., xxxx.sn.mynetname.net).

SSH_PORT: Your forwarded SSH port (e.g., 2222).

SSID: "Guest_WiFi".

BUCKET_NAME: Your GCP storage bucket name.
```

## 🛡️ Security
No Hardcoded Secrets: All keys are pulled from Secret Manager at runtime.

SYN Cookie Protection: Router is hardened against SYN flooding via /ip/firewall/connection/settings.

IP Whitelisting: NAT rules restricted to Google Cloud IP ranges.
