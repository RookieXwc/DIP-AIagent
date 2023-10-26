from easy_ernie import FastErnie


def get_qa(question, bot):
    # baidu_id = 'your id'
    # bduss_bfess = 'your bd'
    # bot = FastErnie(baidu_id, bduss_bfess)
    ans = bot.ask(question)['answer']
    # bot.close()

    return ans


# print(get_qa('hello'))
