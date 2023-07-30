import tasks

def test_word_finder_01():
    o = tasks.word_finder('some word')
    assert o.countWord() == 0

def test_word_finder_02():
    o = tasks.word_finder('some word')
    o.search_string = 'tinkoff'
    assert o.countWord() == 1

def test_word_finder_03():
    o = tasks.word_finder('some word')
    o.search_string = 'tinkoff tinkoff fitnko'
    assert o.countWord() == 2

def test_word_finder_04():
    o = tasks.word_finder('some word')
    o.search_string = 'tinkoff tinkoff fitnkof fffffiiiinnnkkkk'
    assert o.countWord() == 3

def test_word_finder_05():
    o = tasks.word_finder('some word')
    o.search_string = 'tinkoff tinkoff fitnkof fffffiiiinnnkkTkkOOO'
    assert o.countWord() == 4

def test_word_finder_06():
    o = tasks.word_finder('some word')
    o.search_string = 'tinkoff tinkoff fitnkof fffffiiiinnnkkTTkkOOO'
    assert o.countWord() == 5

def test_word_finder_07():
    o = tasks.word_finder('some word')
    o.search_string = 'asjkFtdlfj kl;asdj fl;kasdjfioaweiof jeowijf qwo iefjt - asdkj ;z lsdkjv;nnnklxcnv weriovqtj-r iovjmzxcld;kv thjkj FVJAS-EP[O IFJ-ASEtOKVN n MOPnSDTFKJVO  v n [KDFJV-WOQIRJ  n N V-OW    N    T QIF T J-OVW IJ-OVI fM DF;Kn f LVSJ FKL;GJ O[PSIORJ- WGIOJ  t T ;LZXDFJK VASDL;KF OIWERH GUIWRTHNG MCVNS;KL ADFJFV KLSDFJIKJ]]]'
    assert o.countWord() == 10

def test_word_finder_08():
    o = tasks.word_finder('tinkof')
    assert o.countWord() == 0

def test_word_finder_09():
    o = tasks.word_finder('tinkoff')
    assert o.countWord() == 1

def test_word_finder_10():
    o = tasks.word_finder('tinkofftinko')
    assert o.countWord() == 1

def test_word_finder_11():
    o = tasks.word_finder('tinkofftinkof')
    assert o.countWord() == 1

def test_word_finder_12():
    o = tasks.word_finder('tinkoff tinko')
    assert o.countWord() == 1

def test_word_finder_13():
    o = tasks.word_finder('tinkoff tinkof')
    assert o.countWord() == 1

def test_word_finder_14():
    o = tasks.word_finder('tinkoff tinkoff')
    assert o.countWord() == 2

def test_word_finder_15():
    o = tasks.word_finder('This is Tinkoff Is this tinkoff? ?foknit siht sI')
    assert o.countWord() == 2

def test_word_finder_16():
    o = tasks.word_finder('This is Tinkoff Is this tinkoff? ?foknit siht sI f Yes?')
    assert o.countWord() == 3