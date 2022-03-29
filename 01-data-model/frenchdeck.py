import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 一副牌
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 黑桃 方块 梅花 红心
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # 得到一个纸牌对象，方块7
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    # 查看一副牌有多少张
    print(len(deck))

    # [start_index:end_index:step] start-index=0,1,2
    print(deck[:3])
    # start-index=12 step=13
    print(deck[12::13])
