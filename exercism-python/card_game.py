
def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    round_list=[number, number+1, number+2 ]
    return round_list
    


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    list= rounds_1 + rounds_2
    return list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    average=round(sum(hand)/len(hand),2)
    return average
    


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    true_average=sum(hand)/len(hand)
    sorted(hand)
    mid=len(hand)//2
    if len(hand)%2==0:
        mediun=(hand[mid]+ hand[mid+1])/2
    else:
        mediun= hand[mid]
    if ((hand[0]+ hand[-1])/2) == true_average or mediun == true_average:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    sum_even= 0
    sum_odd= 0
    sorted(hand)
    length=len(hand)
    for i in range(0,length,2):
        sum_even+=hand[i]
    half=(length//2)+1
    average_even= sum_even/half
    for i in range(1,length,2):
        sum_odd+=hand[i]
    average_odd= sum_odd/(length-half)
    if average_odd == average_even:
        return True
    else:
        return False

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1]= hand[-1]*2
    return hand
