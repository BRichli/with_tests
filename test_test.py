import pytest
import sys
import re
import importlib



def test_valid_output(capsys, monkeypatch):
    reg = r"hello world"
    monkeypatch.setattr('builtins.input', lambda x: " world")
    import labs
    importlib.reload(labs) #same here
    results = capsys.readouterr().out
    output  = bool(re.search(reg, results, flags = re.IGNORECASE))
    assert output
   
