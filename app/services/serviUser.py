from database.dataBase import *
def onGetUserByid(username):
    return User.query.filter_by(username = username)

def onGetRegisterUser(userData):
    user = User(
        nombres = userData['nombres'],
        apellidos = userData['apellidos'],
        username = userData['username'],
        email = userData['email'],
        isAdmin = userData['isAdmin'],
        cellPhone = userData['cellPhone']
    )
    User.onGetSetPassword(userData['password'])
    db.session.add(user)
    db.session.commit()