from playing_card_game import deal_cards
from playing_card_game import calculate_points

def test_deal_cards():
    #Test that exactly 5 cards have been drawn
    hand = deal_cards()
    assert len(hand) == 6

def test_calculate_points():
    hand = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Spades', '6 of Clubs']
    assert calculate_points(hand) == 12
