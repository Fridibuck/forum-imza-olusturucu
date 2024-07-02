# Made with ❤ by @forNINE
from PIL import Image, ImageDraw, ImageFont
import imageio
import requests

# İmza boyutları
width, height = 800, 300

# Yazı fontunu ayarlama
font_path_bold = "C:/Windows/Fonts/arialbd.ttf"
font_path_regular = "C:/Windows/Fonts/consola.ttf"
font_large = ImageFont.truetype(font_path_bold, 50)
font_code = ImageFont.truetype(font_path_regular, 16)

# Yazı rengi
text_color = (255, 255, 255, 255)

# Büyük yazıyı sağ alt köşeye ortalama
text_large = "forNINE"
text_bbox_large = ImageDraw.Draw(Image.new('RGBA', (0, 0))).textbbox((0, 0), text_large, font=font_large)
text_width_large = text_bbox_large[2] - text_bbox_large[0]
text_height_large = text_bbox_large[3] - text_bbox_large[1]
text_x_large = width - text_width_large - 20  # Sağdan 20 piksel içeride
text_y_large = height - text_height_large - 20  # Alttan 20 piksel yukarıda

# Arka planda kullanılacak metin
background_text = "code"

# Arka planda Python kodu parçaları ekleme
code_template = """if (BotVariables.anti_afk_state)
{{
{actions}
}}"""

# Kod renkleri
code_colors = [
    (255, 69, 0, 200),   # Red-Orange
    (50, 255, 50, 200),  # Green
    (255, 215, 0, 200),  # Gold
    (0, 191, 255, 200)   # Deep Sky Blue
]

padding = 20
line_spacing = 25

# Her bir karakter için action oluştur
actions = "\n".join([f'    SendKeys.SendWait("{char}");\n    Thread.Sleep(1);' for char in background_text])
code = code_template.format(actions=actions)

code_lines = code.split('\n')

# GIF oluşturma
frames = []
y_offset = padding

# Toplam adım sayısı belirleme
max_steps = max(len(code_lines), len(text_large))

# Kare oluşturma
for i in range(max_steps + 1):
    image = Image.new('RGBA', (width, height), (30, 30, 30, 255))
    draw = ImageDraw.Draw(image)

    # Arka planı süsleme
    for x in range(0, width, 40):
        draw.line((x, 0, x, height), fill=(50, 50, 50, 255))
    for y in range(0, height, 40):
        draw.line((0, y, width, y), fill=(50, 50, 50, 255))

    # Arka plan kodunu çizme
    for j, line in enumerate(code_lines[:i]):
        draw.text((padding, padding + j * line_spacing), line, font=font_code, fill=code_colors[j % len(code_colors)])

    # Ön plan yazısını tek tek karakter ekleyerek çizme
    partial_text = text_large[:i]
    text_bbox_partial = draw.textbbox((0, 0), partial_text, font=font_large)
    text_width_partial = text_bbox_partial[2] - text_bbox_partial[0]
    text_x_partial = width - text_width_partial - 20

    for idx, char in enumerate(partial_text):
        draw.text((text_x_partial + draw.textbbox((0, 0), partial_text[:idx], font=font_large)[2], text_y_large),
                  char, font=font_large, fill=code_colors[idx % len(code_colors)])

    # Her adımda bir kare ekleme
    frames.append(image)

# GIF olarak kaydetme
gif_path = 'imza.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], optimize=False, duration=300, loop=0)

# Imgur'a yükleme
def upload_to_imgur(file_path):
    url = "https://api.imgur.com/3/upload"
    client_id = "91edbc30714b491"  # Buraya kendi Imgur Client ID'nizi ekleyin
    headers = {
        "Authorization": f"Client-ID {client_id}"
    }
    with open(file_path, "rb") as file:
        response = requests.post(url, headers=headers, files={"image": file})
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'link' in data['data']:
            return data['data']['link']
    return None

# GIF'i yükleme ve URL'yi alma
uploaded_url = upload_to_imgur(gif_path)
if uploaded_url:
    bbcode_link = f"[img]{uploaded_url}[/img]"
    print("GIF başarıyla yüklendi. BBCode (Forums) link: ", bbcode_link)
else:
    print("GIF yüklenemedi.")
