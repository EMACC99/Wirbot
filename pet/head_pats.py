import os
from PIL import Image, ImageSequence


class headpats:
    @staticmethod
    def head_pats():
        gif_template = Image.open("dac (1).gif")
        width, height = gif_template.size
        # portrait = webp.load_image("profile.png").convert('RGBA')
        portrait = Image.open("profile.png").convert("RGBA")
        portrait = portrait.resize((width - 10, height - 10))

        frames = []

        for filename in os.listdir("./frames"):
            # print(filename)
            aux = Image.open(f"frames/{filename}").convert("RGBA")
            template = Image.new("RGBA", aux.size, (0, 0, 0, 0))
            template.paste(portrait, (15, 15))
            template.paste(aux, (0, 0), mask=aux)
            # frames.append(Image.alpha_composite(gen_frame(portrait.convert('RGBA')), gen_frame(aux.convert('RGBA'))))
            frames.append(template)

        frames[0].save(
            "output.gif",
            save_all=True,
            append_images=frames[1:],
            optimize=False,
            duration=40,
            loop=0,
        )
