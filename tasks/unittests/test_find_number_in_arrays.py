import tasks

def test_list_and_set():
    t = tasks.find_number_in_arrays([1, 2, 4, 5], [3, 3, 4], [2, 3, 4, 5, 6])
    
    assert t.search_digit_list_and_set() == [4]

def test_search_digit_for_and_if():
    t = tasks.find_number_in_arrays([1, 2, 4, 5], [3, 3, 4], [2, 3, 4, 5, 6])

    assert t.search_digit_for_and_if() == [4]

def test_serch_digit_list_digit_and_full_search():
    t = tasks.find_number_in_arrays([1, 2, 4, 5], [3, 3, 4], [2, 3, 4, 5, 6])
    t2 = tasks.find_number_in_arrays([1, 2, 11, 4, 5], [3, 3, 4, 11], [11, 2, 3, 4, 5, 6])

    assert t.serch_digit_list_digit_and_full_search() == [4]
    assert t2.serch_digit_list_digit_and_full_search() == [4, 11]