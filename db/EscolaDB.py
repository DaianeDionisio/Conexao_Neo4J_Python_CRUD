from db.database import Graph

class EscolaDB:

    def __init__(self):
        self.db = Graph("bolt://44.201.21.71:7687", "neo4j", "yell-hose-construction")

#------------------------CRUD PROFESSOR-------------------------------

    def createProfessor(self, nome, idade, area):
        query = "CREATE (:Professor{nome: \"" + nome + "\", idade: \"" + idade + "\", area: \"" + area + "\"})"
        self.db.execute_query(query)

    def retriveProfessor(self, campoBusca, valorBusca):
        query = "MATCH (p:Professor{"+ campoBusca +": \"" + valorBusca + "\"}) RETURN p"
        self.db.execute_query(query)

    def updateProfessor(self, campoBusca, valorBusca, campo, valor):
        query = "MATCH (p:Professor{"+ campoBusca +": \"" + valorBusca + "\"}) SET p." + campo + " = " + "\"" + valor + "\""
        self.db.execute_query(query)

    def deleteProfessor(self, campoBusca, valorBusca):
        query = "MATCH (p:Professor{" + campoBusca + ": \"" + valorBusca + "\"}) DETACH DELETE p"
        self.db.execute_query(query)

#------------------------CRUD MATERIA-------------------------------

    def createMateria(self, assunto, horario):
        query = "CREATE (:Materia{assunto: \"" + assunto + "\", horario: \"" + horario + "\"})"
        self.db.execute_query(query)

    def retriveMateria(self, campoBusca, valorBusca):
        query = "MATCH (p:Materia{"+ campoBusca +": \"" + valorBusca + "\"}) RETURN p"
        self.db.execute_query(query)

    def updateMateria(self, campoBusca, valorBusca, campo, valor):
        query = "MATCH (p:Materia{"+ campoBusca +": \"" + valorBusca + "\"}) SET p." + campo + " = " + "\"" + valor + "\""
        self.db.execute_query(query)

    def deleteMateria(self, campoBusca, valorBusca):
        query = "MATCH (p:Materia{" + campoBusca + ": \"" + valorBusca + "\"}) DETACH DELETE p"
        self.db.execute_query(query)

    # ------------------------CRUD RELACOES-------------------------------

    def createRelacao(self, campoBuscaProfessor, valorBuscaProfessor, campoBuscaMateria, valorBuscaMateria, ano):
        query = "MATCH (p:Professor{" + campoBuscaProfessor + ": \"" + valorBuscaProfessor + "\"})"
        query = query + "MATCH (m:Materia{" + campoBuscaMateria + ": \"" + valorBuscaMateria + "\"})"
        query = query + "CREATE(p)-[:LECIONA{desde:\"" + ano + "\"}]->(m)"
        self.db.execute_query(query)

    def retriveRelacaoBuscaProfessor(self, campoBuscaProfessor, valorBuscaProfessor):
        query = "MATCH(p:Professor{\"" + campoBuscaProfessor + "\": \"" + valorBuscaProfessor + "\"})-[r:LECIONA]->(m:Materia)"
        query = query + "RETURN r"
        self.db.execute_query(query)

    def retriveRelacaoBuscaMateria(self, campoBuscaMateria, valorBuscaMateria):
        query = "MATCH(p:Professor)-[r:LECIONA]->(m:Materia{\"" + campoBuscaMateria + "\": \"" + valorBuscaMateria + "\"})"
        query = query + "RETURN r"
        self.db.execute_query(query)

    def retriveRelacaoBuscaAno(self, ano):
        query = "MATCH(p:Professor)-[r:LECIONA{desde:\"" + ano + "\"}]->(m:Materia)"
        query = query + "RETURN r"
        self.db.execute_query(query)

    def updateRelacaoBuscaProfessor(self, campoBuscaProfessor, valorBuscaProfessor, ano):
        query = "MATCH(p:Professor{\"" + campoBuscaProfessor + "\": \"" + valorBuscaProfessor + "\"})-[r:LECIONA]->(m:Materia)"
        query = query + "SET r.desde = \"" + ano + "\""
        self.db.execute_query(query)

    def updateRelacaoBuscaMateria(self, campoBuscaMateria, valorBuscaMateria, ano):
        query = "MATCH(p:Professor)-[r:LECIONA]->(m:Materia{\"" + campoBuscaMateria + "\": \"" + valorBuscaMateria + "\"})"
        query = query + "SET r.desde = \"" + ano + "\""
        self.db.execute_query(query)

    def updateRelacaoBuscaAno(self, ano):
        query = "MATCH(p:Professor)-[r:LECIONA{desde:\"" + ano + "\"}]->(m:Materia)"
        query = query + "SET r.desde = \"" + ano + "\""
        self.db.execute_query(query)

    def deleteRelacao(self, ano):
        query = "MATCH(p:Professor)-[r:LECIONA{desde:\"" + ano + "\"}]->(m:Materia)"
        query = query + "DETACH DELETE r"
        self.db.execute_query(query)
