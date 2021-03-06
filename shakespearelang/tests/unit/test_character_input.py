from shakespearelang.shakespeare_interpreter import Shakespeare
from io import StringIO

def test_reads_characters_accurately(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('ab\nAB\t&@ '))
    s = Shakespeare()
    s.run_dramatis_persona('Juliet, a test.')
    s.run_dramatis_persona('Romeo, a test.')
    s.run_event('[Enter Romeo and Juliet]')

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 97

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 98

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 10

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 65

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 66

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 9

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 38

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 64

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 32

    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == ''

def test_unicode(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('ʘɥӜआઔඦᢶᨆᵇḤ'))
    s = Shakespeare()
    s.run_dramatis_persona('Juliet, a test.')
    s.run_dramatis_persona('Romeo, a test.')
    s.run_event('[Enter Romeo and Juliet]')

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 664

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 613

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 1244

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 2310

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 2708

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 3494

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 6326

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 6662

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 7495

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 7716

    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == ''

def test_eof_character_code(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('&'))
    s = Shakespeare()
    s.run_dramatis_persona('Juliet, a test.')
    s.run_dramatis_persona('Romeo, a test.')
    s.run_event('[Enter Romeo and Juliet]')

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 38

    # shakespearelang assumes an implicit \n at the end of files
    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 10

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == -1

    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == ''

def test_past_eof(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(''))
    s = Shakespeare()
    s.run_dramatis_persona('Juliet, a test.')
    s.run_dramatis_persona('Romeo, a test.')
    s.run_event('[Enter Romeo and Juliet]')

    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == -1

    monkeypatch.setattr('sys.stdin', StringIO('a'))
    s.run_sentence('Open your mind!', s._on_stage_character_by_name('Juliet'))
    assert s._character_by_name('Romeo').value == 97
    captured = capsys.readouterr()

    assert captured.out == ''
    assert captured.err == ''
