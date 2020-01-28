from Card import Card
import Text
import manage


def main():
    card_id = manage.check_card_id(input("请输入卡牌ID："))
    card_type = manage.check_number(input(Text.choose_type_text), 0, 3)
    card = Card(card_id, card_type)
    card.create_content()
    card.create_file()


if __name__ == '__main__':
    print(Text.welcome_text)
    main()
