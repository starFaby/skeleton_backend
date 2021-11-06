from database.dataBase import *

def createDB():
    db.drop_all()
    db.create_all()

def initDB():
    createDB()
    admin = User(
        nombres = "edgar fabian",
        apellidos = "estrella guambuguete",
        username = "starfaby",
        email = "star._faby@hotmail.com",
        isAdmin = True,
        cellPhone = "0983856136",
    )
    admin.onGetSetPassword("star123")
    db.session.add(admin)
    db.session.commit()