from db.EscolaDB import EscolaDB

escolaDB = EscolaDB()

#escolaDB.createProfessor("João","25","Banco de Dados")
escolaDB.retriveProfessor("nome","João")
escolaDB.updateProfessor("idade","25","area","POO")
escolaDB.deleteProfessor("nome", "João")