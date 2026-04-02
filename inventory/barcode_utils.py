import barcode
from barcode.writer import ImageWriter
from io import BytesIO
import base64
import os
from django.conf import settings


def generate_barcode_base64(value):
    """Generate a Code128 barcode and return as base64 PNG string."""
    if not value or not value.strip():
        value = "NO-TAG"
    value = str(value).strip()
    try:
        CODE128 = barcode.get_barcode_class('code128')
        writer = ImageWriter()
        writer.set_options({
            'module_width': 0.35,
            'module_height': 15.0,
            'quiet_zone': 4.0,
            'font_size': 10,
            'text_distance': 4.0,
            'background': 'white',
            'foreground': 'black',
            'write_text': True,
            'dpi': 150,
        })
        buf = BytesIO()
        bc = CODE128(value, writer=writer)
        bc.write(buf)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode('utf-8')
        return f"data:image/png;base64,{b64}"
    except Exception as e:
        return None


def save_barcode_file(value, filename):
    """Save barcode as PNG file to media/barcodes/."""
    if not value or not value.strip():
        value = "NO-TAG"
    value = str(value).strip()
    try:
        CODE128 = barcode.get_barcode_class('code128')
        writer = ImageWriter()
        writer.set_options({
            'module_width': 0.4,
            'module_height': 18.0,
            'quiet_zone': 5.0,
            'font_size': 12,
            'text_distance': 5.0,
            'dpi': 200,
        })
        save_dir = os.path.join(settings.MEDIA_ROOT, 'barcodes')
        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, filename)
        bc = CODE128(value, writer=writer)
        bc.save(filepath)
        return f"{settings.MEDIA_URL}barcodes/{filename}.png"
    except Exception as e:
        return None
