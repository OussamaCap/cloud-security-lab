def set_password():
    print("Please set a new login password") 
    user_input = input("enter password: ")
    return len(user_input) >= 12
    
def test_set_password_success(monkeypatch):
    # correct user input simulation
    monkeypatch.setattr("builtins.input", lambda _: "secret123543212")
    
    assert set_password() is True
    
def test_set_password_failure(monkeypatch):
    # correct user input simulation
    monkeypatch.setattr("builtins.input", lambda _: "secret123")
    
    assert set_password() is False