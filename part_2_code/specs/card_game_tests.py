import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("spade", 8)
        self.card2 = Card("club", 3)
        self.card3 = Card("heart", 4)
        self.card4 = Card("diamond", 1)

        self.cards = [self.card1, self.card2, self.card3, self.card4]
        self.card_game = CardGame("ring of fire", self.cards)
    

    def test_check_for_ace_true(self):
        actual = self.card_game.check_for_ace(self.card4)
        self.assertEqual(actual, True)
    
    def test_check_for_ace_false(self):
        actual = self.card_game.check_for_ace(self.card3)
        self.assertEqual(actual, False)
    
    def test_highest_card_is_card1(self):
        actual = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(actual, self.card1)
    
    def test_highest_card_is_card2(self):
        actual = self.card_game.highest_card(self.card2, self.card4)
        self.assertEqual(actual, self.card2)
    
    def test_cards_total(self):
        actual = self.card_game.cards_total(self.cards)
        expected = "You have a total of 16"
        self.assertEqual(actual, expected)        