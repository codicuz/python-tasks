import tasks

def test_word_finder():
    o = tasks.word_finder('some word')
    assert o.countWord() == 0

    o.search_string = 'tinkoff'
    assert o.countWord() == 1

    o.search_string = 'tinkoff tinkoff fitnko'
    assert o.countWord() == 2

    o.search_string = 'tinkoff tinkoff fitnkof fffffiiiinnnkkkk'
    assert o.countWord() == 3

    o.search_string = 'tinkoff tinkoff fitnkof fffffiiiinnnkkTkkOOO'
    assert o.countWord() == 4

    o.search_string = 'tinkoff tinkoff fitnkof fffffiiiinnnkkTTkkOOO'
    assert o.countWord() == 5

    o.search_string = 'asjkFtdlfj kl;asdj fl;kasdjfioaweiof jeowijf qwo iefjt - asdkj ;z lsdkjv;nnnklxcnv weriovqtj-r iovjmzxcld;kv thjkj FVJAS-EP[O IFJ-ASEtOKVN n MOPnSDTFKJVO  v n [KDFJV-WOQIRJ  n N V-OW    N    T QIF T J-OVW IJ-OVI fM DF;Kn f LVSJ FKL;GJ O[PSIORJ- WGIOJ  t T ;LZXDFJK VASDL;KF OIWERH GUIWRTHNG MCVNS;KL ADFJFV KLSDFJIKJ]]]'
    assert o.countWord() == 10