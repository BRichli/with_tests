import pytest
import sys
import re
import importlib


@pytest.mark.parametrize(' test_num, in1, ou',
                            [

                                ( 1, ["HI"], r"HI WORLD"),  
                           
                                
                                
                            
                            ]


                          )
def test_valid_inputs(capsys, monkeypatch, test_num, in1, ou):
    
    anything = r"(\n|[^\n])*"

    
    it1 = iter(in1)
    monkeypatch.setattr('builtins.input', lambda x: next(it1))

    
    import lab3_1 #change this to the name of the file you want to test 
    if(test_num > 1):
       importlib.reload(lab3_1) #same here remember don't add .py at end


    
    outputs = capsys.readouterr().out
    reg = ""
    for val in ou:
        reg += anything + val + anything

    results = bool(re.search(reg, outputs, flags=re.IGNORECASE))
    
    x = "Failed on test number {x}".format(x = test_num)
    print(x)
    print("output was:\n" + outputs)
    print("expected regex matches:")
    for i in ou:
        print(i)

    print("see comments for what was being tested")
    assert results
   

