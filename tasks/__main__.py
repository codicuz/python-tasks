import tasks

o = tasks.find_number_in_arrays()

def main():
    print("Tasks")

def task01_search_digit_list_and_set():
    o.search_digit_list_and_set()

def task01_search_digit_for_and_if():
    o.search_digit_for_and_if()

def task01_serch_digit_list_digit_and_full_search():
    o.serch_digit_list_digit_and_full_search()

def task02_word_finder():
    o = tasks.word_finder('some word string')
    o.countWord()
    o.search_string = 'Kate got a job offer from Invest team'
    o.countWord()
    o.search_string = 'Kate got a job offer from Tinkoff Invest'
    o.countWord()
    o.search_string = 'tinkoff Tinkoff ffoknit has a good ffokint tfnikof'
    o.countWord()
    o.search_string = '   fff  tinkoff Tinoff ffoknit f HAS A GOOD fokint tfnikof'
    o.countWord()

if __name__ == '__main__':
    main()
    task01_search_digit_list_and_set()
    task01_search_digit_for_and_if()
    task01_serch_digit_list_digit_and_full_search()
    task02_word_finder()