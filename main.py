import os
import qrcode

import paramiko
from google.cloud import storage
import io

from utils import escape_ssh_string, generate_qr, generate_strong_password

# --- CONFIGURATION ---
PORT = 22
ROUTER_IP = "10.0.0.1"
ROUTER_USER = "EasyGuestBot"  # Don't use admin!
SSID = "Guest_WiFi"
GCP_BUCKET_NAME = "your-wifi-portal-bucket"
GUEST_SECURITY = "guest_security"

def update_mikrotik(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    private_key_path = os.path.expanduser("~/.ssh/mikrotik_gcp_key")

    # ssh.connect(ROUTER_IP, username=ROUTER_USER)

    # Explicitly use the key for authentication
    ssh.connect(
        ROUTER_IP,
        port=PORT,
        username=ROUTER_USER,
        key_filename=private_key_path
    )

    # Update the Security Profile directly
    # Assuming your guest security profile is named 'guest_security'
    cmd = f'/interface/wifi/security/set [find name="{GUEST_SECURITY}"] passphrase="{password}"'

    print(f"sending command:\n{cmd}")

    ssh.exec_command(cmd)
    ssh.close()


# def upload_qr_to_gcp(password):
#     # Create the specialized Wi-Fi string
#     wifi_data = f"WIFI:T:WPA;S:{SSID};P:{password};;"
#
#     # Generate QR in memory (don't need to save local file first)
#     qr = qrcode.QRCode(border=2)
#     qr.add_data(wifi_data)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#
#     # Save to a byte buffer
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format='PNG')
#     img_byte_arr.seek(0)
#
#     # Upload to Google Cloud Storage
#     client = storage.Client()
#     bucket = client.bucket(GCP_BUCKET_NAME)
#     blob = bucket.blob("wifi-qr.png")
#     blob.upload_from_file(img_byte_arr, content_type='image/png')
#     # Optional: Set cache control so the browser doesn't show the old QR
#     blob.cache_control = "no-cache, max-age=0"
#     blob.patch()


if __name__ == "__main__":
    new_password = generate_strong_password(16)
    safe_password = escape_ssh_string(new_password)
    print(f"setting new pw: {new_password}")
    update_mikrotik(safe_password)
    qr_code = generate_qr(wifi_text=f"WIFI:T:WPA;S:{SSID};P:{new_password};;", preview=True)
    # upload_qr_to_gcp(NEW_PASSWORD)
    # print("Router updated and QR uploaded to GCP!")
