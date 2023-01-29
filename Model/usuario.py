
##
# Usuario
#   nome
#   sobreNome
#   telefone 
#   email
#   usuario
#   senha
# #

class Usuario:
    
    def __init__(self, nome:str, sobreNome:str, cpf:str, telefone:str, email:str,usuario:str, senha:str) -> None:
        
        self.nome = nome
        self.sobreNome = sobreNome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
        

# setter  class Usuario
def nome(self) -> str:
    return self.nome

def sobreNome(self) -> str:
    return self.sobreNome

def telefone(self) -> set:
    return self.telefone

def cpf(self) -> str:
    return self.cpf

def email(self) -> str:
    return self.email

def usuario(self) -> str:
    return self.usuaio

def senha(self) -> str:
    return self.senha

#getter
def nome(self, nome) -> str:
    self.nome = nome
    
def sobreNome(self, sobreNome) -> str:
    self.sobreNome = sobreNome
    
def telefone(self, telefone) -> str:
    self.telefone = telefone
    
def cpf(self, cpf) -> str:
    self.cpf = cpf
    
def email(self, email) -> str:
    self.email = email
    
def usuaio(self, usuaio) -> str:
    self.usuaio = usuaio
    
def senha(self, senha) -> str:
    self.senha = senha 