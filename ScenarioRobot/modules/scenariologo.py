from ScenarioRobot.events import register
from ScenarioRobot import OWNER_ID, BOT_NAME
from ScenarioRobot import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont

LOGO_LINKS = [
    "https://telegra.ph/file/c1ad29c189162a1404749.jpg",
    "https://telegra.ph/file/2d288450ebecc500addbd.jpg",
 ]        
@register(pattern="^/logo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id == OWNER_ID:
        pass
    else:

        if not quew:
            await event.reply("Please Give Me A Name Or Text For The Logo.")
            return
    pesan = await event.reply("Creating you logo. Please Wait...")
    try:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./aries/arieslogo/*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        w, h = draw.textsize(text, font=font)
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "Scenario.png"
        img.save(fname, "png")
        await tbot.send_file(event.chat_id, file=fname, caption=f"Made by Scenario")
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await event.reply(f"Error, Report @noobxsupport, {e}")

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 • `/logo text`*:*  Create your logo with your name
 • `/wlogo`*:*  Create your logo with your name
 """
__mod_name__ = "LOGO"
