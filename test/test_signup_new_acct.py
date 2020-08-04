

def test_signup_new_acct(app):
    username = "user3333"
    password = "test"
    app.james.ensure_user_exists(username, password)
