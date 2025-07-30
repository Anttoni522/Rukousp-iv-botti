from telegram.ext import Updater, CommandHandler
import logging
import datetime

# Lisää oma token tähän
TOKEN = 8311587140:AAEJvcGUUQu9CQRVyblzvanFEdgC_uv3dtM

# Lokia asetukset (hyvä virheiden seurantaan)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Päivittäinen rukousviesti (voit laajentaa tätä listaa myöhemmin)
RUKOUKSET = [
    "Rukoilemme tänään rauhaa ja viisautta.",
    "Jumalan siunausta uuteen päivään.",
    "Kiitä Herraa kaikesta hyvästä!",
    "Herra johdattakoon sinua tänään.",
]

def start(update, context):
    update.message.reply_text("Tervetuloa Rukouspäivä-bottiin! Saat päivittäin rukouksen ja raamatunjakeen.")

def rukous(update, context):
    today = datetime.datetime.now().day
    rukous = RUKOUKSET[today % len(RUKOUKSET)]
    update.message.reply_text(rukous)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rukous", rukous))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
