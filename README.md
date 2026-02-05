# it_sikkerhed_2026f
Dette er et skoleprojekt på Zealand 

def test_pass():
    # Denne test vil passere
    assert 1 + 1 == 2

def test_fail():
    # Denne test vil fejle
    assert 1 * 1 == 1

# @pytest.mark.skip(reason="Springes over med vilje") # Denne test bliver slet ikke kørt
def test_skip():
    assert True # failed test bliver ignoreret
   # raise RuntimeError("Test crashede med vilje") # crash bliver også ignoreret

def test_crash():
    # Denne test crasher med en exception
    assert True
   # assert False # failed test bliver ignoreret


# 05/02/2026 - (Test) Teknikker

# Dette repository forklarerer anvendelsen af testteknikker med password-validering i fokus. 

# Krav til password: 1. Passwordlængde: mellem 8-16. Mindre end 8 karakterer --> fej. Mere end 16 karakterer --> fejl 

# Ækvivalensklasser:

| Klasse | Længde    | Forventet resultat |
|--------|-----------|--------------------|
| 1      | 0-7 tegn  | afvist             |
| 2      | 8-16 tegn | godkendt           |
| 3      | 17+ tegn  | afvist             |


