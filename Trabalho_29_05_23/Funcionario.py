from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    cpf: str
    salario: float

@dataclass
class Enfermeira(Funcionario):
    especialidade: str

@dataclass
class TecnicaEnfermagem(Funcionario):
    turno: str

@dataclass
class Medico(Funcionario):
    crm: str
    especialidade: str
