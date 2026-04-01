from flask import Flask, render_template, request
from urllib.parse import quote
from cryptography.fernet import Fernet
import qrcode
import os
import time
import base64
from PIL import Image

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode())


@app.route('/', methods=["GET", "POST"])
def home():
    img_name = None

    if request.method == "POST":
        qr_type = request.form.get("type")
        data = ""

        # 🎨 Get colors (FIXED)
        qr_color = request.form.get("qr_color") or "black"
        bg_color = request.form.get("bg_color") or "white"

        # URL
        if qr_type == "url":
            data = request.form.get("url")

        # 🔐 SECRET
        elif qr_type == "secret":
            message = request.form.get("message")
            password = request.form.get("secret_password")

            if message and password:
                    key = generate_key(password)
                    f = Fernet(key)

                    encrypted = f.encrypt(message.encode()).decode()

                    # ✅ IMPORTANT: create link instead of raw text
                    encoded = quote(encrypted)

                    # 👉 LOCAL (for testing)
                    base_url = request.host_url  # auto handles localhost or live

                    data = f"{base_url}decode?data={encoded}"

        # EMAIL
        elif qr_type == "email":
            email = request.form.get("email")
            data = f"mailto:{email}"

        # PHONE
        elif qr_type == "phone":
            phone = request.form.get("phone")
            data = f"tel:{phone}"

        # WIFI
        elif qr_type == "wifi":
            ssid = request.form.get("ssid")
            password = request.form.get("wifi_password")
            data = f"WIFI:T:WPA;S:{ssid};P:{password};;"

        # LOCATION
        elif qr_type == "location":
            lat = request.form.get("lat")
            long = request.form.get("long")
            data = f"https://maps.google.com/?q={lat},{long}"

        # ✅ Generate QR ONLY if data exists
        if data:
            filename = f"qr_{int(time.time())}.png"
            filepath = os.path.join("static", filename)

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )

            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')

            # 🖼️ Add logo
            logo_path = "static/logo.png"

            if os.path.exists(logo_path):
                logo = Image.open(logo_path).convert("RGBA")

                # Remove background (force white bg)
                white_bg = Image.new("RGBA", logo.size, (255, 255, 255, 255))
                logo = Image.alpha_composite(white_bg, logo)

                # Resize logo
                logo_size = img.size[0] // 4
                logo = logo.resize((logo_size, logo_size))

                # Position center
                pos = ((img.size[0] - logo_size) // 2,
                    (img.size[1] - logo_size) // 2)

                img.paste(logo, pos)

            img.save(filepath)
            img_name = filename

    return render_template("index.html", img_name=img_name)

from urllib.parse import unquote

@app.route('/decode', methods=["GET", "POST"])
def decode():
    message = None
    encoded_text = ""

    # ✅ When opened from QR (GET request)
    data = request.args.get("data")
    if data:
        encoded_text = unquote(data)

    # ✅ When user submits password
    if request.method == "POST":
        encoded_text = request.form.get("encoded")
        password = request.form.get("password")

        try:
            key = generate_key(password)
            f = Fernet(key)

            decrypted = f.decrypt(encoded_text.encode()).decode()
            message = decrypted

        except:
            message = "Wrong Password ❌"

    return render_template("decode.html", message=message, encoded_text=encoded_text)
# Delete old QR files
for file in os.listdir("static"):
    if file.startswith("qr_"):
        os.remove(os.path.join("static", file))


if __name__ == "__main__":
    app.run()