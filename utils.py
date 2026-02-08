import io
import re
import secrets
import string

import qrcode


def escape_ssh_string(text):
    # Characters to escape: "$\?
    # We use a regex character class [] and escape characters as needed
    pattern = r'(["$\?])'
    return re.sub(pattern, r'\\\1', text)


def generate_qr(wifi_text, preview=False) -> io.BytesIO:
    img = qrcode.make(wifi_text)

    if preview:
        try:
            # Import only when needed for local testing
            from PIL import Image
            img.show()
        except ImportError:
            print("Pillow not installed. Skipping local preview.")

    # Save to memory (Standard behavior)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf


def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


if __name__ == "__main__":
    new_password = generate_strong_password(16)

    print(f"\nGenerated Password: {new_password}")
    print("\n" + "=" * 30)
    input("Press Enter to close...")