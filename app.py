Token = ""
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from btc_price.btc_price import get_btc_price
from email_files.send_email import build_send_email
from email_files.retrive_add_email import retrive_emails
from email_files.check_format_email import check_format_email
import logging
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('De útil ate agora so faço café')


def falar(bot, update):
    """Adiciona falas comuns ao bot ao digitar o comando /falar

    Args:
        bot (bot): bot em execuçao
        update (Updater): objeto de atualizaçao do chat
    """
    dialogo = ["Vocês querem café?", "Não entendi", "Petrini explica para min isso daqui",
               "Tomei pau denovo", " (assobio)", "O que que foi fi?",
               "Esse tarique tem que deixar de ser vagabundo", "Café está pronto", "Comprou minha placa de video?"]

    bot.send_message(chat_id=update.message.chat_id,
                     text=random.choice(dialogo))


def help(bot, update):
    pass


def echo(bot, update):

    update.message.reply_text(
        f"Não entendi o que vc quis dizer com {update.message.text}")


def error(bot, update, error):

    logger.warning('Update "%s" caused error "%s"', update, error)


def btc(bot, update):
    price = get_btc_price(convert="BRL", limit=0)
    message = f"Colé olha o preço ae \n{price}\nDaora né? "
    update.message.reply_text(message)


def send_email(bot, update):

    bot.send_message(chat_id=update.message.chat_id,
                     text="Enviando mensagem...")
    try:
        build_send_email(subject="Cafe", sender="vicesabot@gmail.com", body="O café esta pronto!",
                         passw="vicentemito", user=update.message.from_user.first_name)

        bot.send_message(chat_id=update.message.chat_id,
                         text="Mensagem enviada para todos os emails com sucesso!")
    except Exception as e:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Houve um problema ao tentar enviar as mesagens, aguarde a assistência técnica")
        print(e)


def retrive_emails(bot, update):

    emails = ";".join(retrive_emails)
    bot.send_message(chat_id=update.message.chat_id,
                     text=f"Lista de emails cadastrados:\n{emails}")


def add_email(bot, update):
    pass


def main():

    updater = Updater(Token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("falar", falar))
    dp.add_handler(CommandHandler("btc", btc))
    dp.add_handler(CommandHandler("cafepronto", send_email))
   # dp.add_handler()

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
