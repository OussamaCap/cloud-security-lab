def login():
    saved_password ="secret123"
    user_input = input("enter password: ")
    return user_input == saved_password
    
def test_login_success(monkeypatch):
    # correct user input simulation
    monkeypatch.setattr("builtins.input", lambda _: "secret123")
    
    assert login() is True
    

def test_login_failure(monkeypatch):
    # correct user input simulation
    monkeypatch.setattr("builtins.input", lambda _: "wrongpass")
    
    assert login() is False