import BizBot


def read_token():
    with open('token.txt', 'r') as f:
        return f.readlines()[0].strip()


bot = BizBot.Bot('biz')
bot.run(read_token())