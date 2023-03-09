class Usuario:
    Nome = ""
    Sabor = ""
    def __init__(self, nome, sabor):
        self.Id = id
        self.Nome = nome
        self.Sabor = sabor
    def Ler(Usuarios):
        line = ""
        f = open('usuarios.txt')
        line = f.readlines()
        for i in line:
            datas = i.split(";")
            Usuario.Nome = datas[0]
            Usuario.Sabor = datas[1]
            Usuarios.append(Usuario(Usuario.Nome, Usuario.Sabor))