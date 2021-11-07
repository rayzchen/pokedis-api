from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO
import urllib.request
import io

def get_image(species):
    link = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/" + str(species) + ".png"
    url = urllib.request.urlopen(link)
    file = io.BytesIO(url.read())
    return Image.open(file).convert("RGBA")

app = Flask(__name__)

@app.route("/image")
def image():
    img1 = get_image(int(request.args["a"])).transpose(Image.FLIP_LEFT_RIGHT)
    img2 = get_image(int(request.args["b"]))
    img = Image.new("RGBA", (360, 180))
    img.paste(img1.resize((180, 180)), (0, 0))
    img.paste(img2.resize((180, 180)), (180, 0))

    fp = BytesIO()
    img.save(fp, "PNG")
    fp.seek(0)
    return send_file(fp, mimetype="image/png")

app.run(host="0.0.0.0", port=5000)
