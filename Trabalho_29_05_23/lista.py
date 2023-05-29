from Funcionario import TecnicaEnfermagem,Enfermeira, Medico

def listar_funcionarios(funcionarios):
    print("==== Lista de Funcionários ====")
    for funcionario in funcionarios:
        if isinstance(funcionario, Enfermeira):
            print(f"Enfermeira: {funcionario.nome} - Especialidade: {funcionario.especialidade} - CPF: {funcionario.cpf}")
        elif isinstance(funcionario, TecnicaEnfermagem):
            print(f"Técnica de Enfermagem: {funcionario.nome} - Turno: {funcionario.turno} - CPF: {funcionario.cpf}")
        elif isinstance(funcionario, Medico):
            print(f"Médico: {funcionario.nome} - Especialidade: {funcionario.especialidade} - CPF: {funcionario.cpf}")
    print("================================")

def buscar_funcionario(funcionarios, cpf):
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            return funcionario
    return None


def atualizar_funcionario(funcionario):
    if isinstance(funcionario, Enfermeira):
        especialidade = input("Digite a nova especialidade da enfermeira: ")
        funcionario.especialidade = especialidade
    elif isinstance(funcionario, TecnicaEnfermagem):
        turno = input("Digite o novo turno de trabalho da técnica de enfermagem: ")
        funcionario.turno = turno
    elif isinstance(funcionario, Medico):
        especialidade = input("Digite a nova especialidade do médico: ")
        funcionario.especialidade = especialidade


def excluir_funcionario(funcionarios, funcionario):
    funcionarios.remove(funcionario)