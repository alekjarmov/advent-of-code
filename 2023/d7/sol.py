from functools import cmp_to_key
from collections import Counter


def read_input():
    with open('input') as f:
        return f.read().splitlines()


card_types = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def get_hand_ranking(hand):
    hand = sorted(hand)
    counts = Counter(hand)

    if 5 in counts.values():
        return 7  # Five of a kind
    elif 4 in counts.values():
        return 6  # Four of a kind
    elif 3 in counts.values() and 2 in counts.values():
        return 5  # Full house
    elif 3 in counts.values():
        return 4  # Three of a kind
    elif list(counts.values()).count(2) == 2:
        return 3  # Two pairs
    elif 2 in counts.values():
        return 2  # One pair

    return 1  # High card


def same_rank_comparison(hand1, hand2):
    for ch1, ch2 in zip(hand1, hand2):
        if card_types.index(ch1) < card_types.index(ch2):
            return 1
        elif card_types.index(ch1) > card_types.index(ch2):
            return -1
    return 0


def high_card_comparison(hand1, hand2):
    min_index1 = min([card_types.index(x) for x in hand1])
    min_index2 = min([card_types.index(x) for x in hand2])

    if min_index1 < min_index2:
        return 1
    elif min_index1 > min_index2:
        return -1
    return 0


def compare_hands(hand1, hand2):
    # print(hand1, hand2)
    if get_hand_ranking(hand1) > get_hand_ranking(hand2):
        return 1
    elif get_hand_ranking(hand1) < get_hand_ranking(hand2):
        return - 1

    # if get_hand_ranking(hand1) == 1:
    #     comp = high_card_comparison(hand1, hand2)
    #     if comp != 0:
    #         return comp

    return same_rank_comparison(hand1, hand2)


if __name__ == "__main__":
    hands = []

    for line in read_input():
        cards, amount = line.split()
        hands.append((cards, int(amount)))
    print(hands)
    hands = sorted(hands, key=cmp_to_key(lambda i1, i2: compare_hands(i1[0], i2[0])))
    print(hands)
    sum = 0
    for i, el in enumerate(hands):
        sum += el[1] * (i + 1)
    print(sum)
