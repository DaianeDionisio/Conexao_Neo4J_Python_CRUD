from db.EscolaDB import EscolaDB

escolaDB = EscolaDB()


#criando os professores
escolaDB.createProfessor("João","25","TI")
escolaDB.createProfessor("Maria","30","TI")
escolaDB.createProfessor("Fabio","40","Exatas")
escolaDB.createProfessor("Rita","23","Exatas")

#criando as materias
escolaDB.createMateria("Banco de Dados", "Sexta-feira as 7:30")
escolaDB.createMateria("Calculo", "Segunda feira as 9:00")

#criando as relações
escolaDB.createRelacao("nome","João","assunto","Banco de Dados","2016")
escolaDB.createRelacao("nome","Maria","assunto","Banco de Dados","2020")
escolaDB.createRelacao("nome","Fabio","assunto","Calculo","2015")
escolaDB.createRelacao("nome","Rita","assunto","Calculo","2019")


