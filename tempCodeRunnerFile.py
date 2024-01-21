def logout():
    session.pop('user_id')
    return redirect('/')