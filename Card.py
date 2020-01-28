import Text
import manage


class Card:

    def __init__(self, card_id, card_type):
        self.card_id = card_id
        self.card_type = card_type
        if card_type == 0:
            self.function = ""
        elif card_type == 1:
            num_trigers = manage.check_number(
                input(Text.choose_cardtrigers_text), 0, 15)
            self.function = manage.cardtrigers[num_trigers]
        elif card_type == 2:
            self.function = """
                public override void onCardPlay(Playfield p, bool ownplay, Minion target, int choice)
                {}"""

    def create_content(self):

        self.content = """using System;
using System.Collections.Generic;
using System.Text;

    namespace HREngine.Bots
    {
        class %s : SimTemplate
        {
            //Write your code here
            %s
        }
    }
    """ % (self.card_id, self.function)

    def create_file(self):
        try:
            f = open("Sim_"+self.card_id+".cs", "x")
            f.write(self.content)
            f.close()
            print("创建SIM成功！")
        except FileExistsError:
            print("Sim文件已存在！")
