import requests
import json

def create_vps():
    API_KEY = input("Masukkan API Key Anda: ")
    VPS_NAME = input("Masukkan nama VPS Anda: ")
    VPS_REGION = input("Masukkan region VPS Anda: ")
    VPS_SIZE = input("Masukkan ukuran VPS Anda: ")
    VPS_IMAGE = input("Masukkan gambar VPS Anda: ")

    DIGITALOCEAN_API_URL = "https://api.digitalocean.com/v2/droplets"

    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    VPS_DATA = {
        "name": VPS_NAME,
        "region": VPS_REGION,
        "size": VPS_SIZE,
        "image": VPS_IMAGE,
        "tags": ["tag1", "tag2"],
        "backups": True,
        "ipv6": True,
        "user_data": None
    }

    response = requests.post(DIGITALOCEAN_API_URL, headers=HEADERS, json=VPS_DATA)
    response_json = response.json()

    if response.status_code == 201:
        print("VPS berhasil dibuat!")
        print(f"ID VPS: {response_json['droplet']['id']}")
        print(f"Nama VPS: {response_json['droplet']['name']}")
        print(f"Region VPS: {response_json['droplet']['region']['slug']}")
        print(f"Ukuran VPS: {response_json['droplet']['size']['slug']}")
        print(f"Gambar VPS: {response_json['droplet']['image']['slug']}")
    else:
        print("Terjadi kesalahan saat membuat VPS:")
        print(response.text)

if __name__ == "__main__":
    create_vps()
