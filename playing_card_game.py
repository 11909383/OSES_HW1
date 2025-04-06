import random
from collections import defaultdict




# Define the ranks and suits in a standard poker deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']




# Create a function to deal two random cards
def deal_cards():
    # Create the deck of cards
        deck = [f'{rank} of {suit}' for rank in ranks for suit in suits]
    
    # Shuffle the deck
    random.shuffle(deck)

    
    
    # Deal five cards
    hand = [deck.pop() for _ in range(5)]
    # Return the hand
    (return hand)

def calculate_points(hand):
    # Assign points to cards
    rank_points = {
     '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    
    # Create a dictionary to store the sum of points for each suit
    suit_points = defaultdict(int)
    
    # Loop through each card in the hand
    for card in hand:
        # Split rank and suit
        rank, suit = card.split(' of ')


        
        # Add the points for the rank to the corresponding suit's total
        suit_points[suit] += rank_points[rank]
    
    # Find the highest total sum of points for any suit
    highest_points = max(suit_points.values())
    
    return highest_points
# Deal five cards and print the hand
hand = deal_cards()

print(f'You were dealt: {", ".join(hand)}')

# Calculate and print the largest sum of points of the same suit
largest_sum = calculate_points(hand)
    print(f'The largest sum of points from the same suit is: {largest_sum}')
