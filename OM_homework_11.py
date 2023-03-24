def cat_with_hats(number_of_cats: int, number_of_rounds: int) -> List[int]:
    '''
    Returns the list of cats with hats after a certain number of rounds.

    Parameters:
    number_of_cats (int): The number of cats.
    number_of_rounds (int): The number of rounds.

    Returns:
    List[int]: The list of cats with hats.
    '''
    cat_list = [False] * number_of_cats  # List of each cat's status hat. at the start none of them have
    for round_number in range(1, number_of_rounds + 1):
        for hat in range(round_number - 1, number_of_cats, round_number):
            cat_list[hat] = not cat_list[hat]  # Change the hat status
    return [hat + 1 for hat in range(number_of_cats) if cat_list[hat]]


number_of_cats = 100
number_of_rounds = 100
print("Cats with following numbers have hats: ", cat_with_hats(number_of_cats, number_of_rounds))
