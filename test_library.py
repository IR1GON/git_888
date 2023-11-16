import library

def test_type_definitions():
    assert library.type_definitions('5') == int(5)
    assert library.type_definitions('5.5') == float(5.5)

def test_cm_to_inches():
    assert library.cm_to_inches('2.54') == '1.0'
    assert library.cm_to_inches('5') == '1.968503937007874'

def test_round_number_round_up_no(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    library.round_number(5.5555)
    captured = capsys.readouterr()
    assert captured.out.strip() == ''
