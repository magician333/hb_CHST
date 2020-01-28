def check_number(num, min_num, max_num):
    try:
        num = int(num)
        if min_num <= num <= max_num:
            return num
        else:
            print("输入错误！")
            exit()
    except ValueError:
        print("输入错误！")
        exit()


def check_card_id(card_id):
    if "_" in card_id and card_id.count("_") == 1:
        # 判断卡牌id是否正确，并将下划线前的单词大写
        return card_id[:card_id.index("_")].upper()+card_id[card_id.index("_"):]
    else:
        print("卡牌ID错误！")
        exit()


cardtrigers = [
    """
            public override void getBattlecryEffect(Playfield p, Minion own, Minion target, int choice)
            {

            }
        """,
    """
            英雄获得治疗时产生特效
        """,
    """
            public virtual void onAMinionGotHealedTrigger(Playfield p, Minion triggerEffectMinion, int minionsGotHealed)
            {
                
            }
        """,
    """
            public override void onAuraStarts(Playfield p, Minion own)
            {
                
            }
            public override void onAuraEnds(Playfield p, Minion m)
            {
                
            }
        """,
    """
            public override void onCardIsGoingToBePlayed(Playfield p, Handmanager.Handcard hc, bool wasOwnCard, Minion triggerEffectMinion)
            {

            }
        """,
    """
        oncardwasplayed
        """,
    """
            public override void onDeathrattle(Playfield p, Minion m)
            {

            }
        """,
    """
            public override void onEnrageStart(Playfield p, Minion m)
            {

            }
            public override void onEnrageStop(Playfield p, Minion m)
            {

            }
        """,
    """
            public virtual void onMinionDiedTrigger(Playfield p, Minion triggerEffectMinion, Minion diedMinion)
            {

            }
        """,
    """
            public virtual void onMinionGotDmgTrigger(Playfield p, Minion triggerEffectMinion, int anzOwnMinionsGotDmg, int anzEnemyMinionsGotDmg, int anzOwnHeroGotDmg, int anzEnemyHeroGotDmg)
            {

            }
        """,
    """
            public override void onMinionIsSummoned(Playfield p, Minion triggerEffectMinion, Minion summonedMinion)
            {

            }
        """,
    """
            onMinionWasSummoned
        """,
    """
            public override void onSecretPlay(Playfield p, bool ownplay, Minion attacker, Minion target, out int number)
            {

            }
        """,
    """
            public virtual void onTurnStartTrigger(Playfield p, Minion triggerEffectMinion, bool turnStartOfOwner)
            {

            }
        """,
    """
            public virtual void onTurnEndsTrigger(Playfield p, Minion triggerEffectMinion, bool turnEndOfOwner)
            {

            }
        """
]
