from Funcionario import Enfermeira, Medico, TecnicaEnfermagem

def cadastrar_funcionario():
    tipo_funcionario = input("Digite o tipo de funcionário (médico, enfermeira ou técnica de enfermagem): ")
    if tipo_funcionario == "médico":
        nome = input("Digite o nome do médico: ")
        cpf= input("Digite o CPF do médico: ")
        salario = float(input("Digite o salário do médico: "))
        crm = input("Digite o CRM do médico: ")
        especialidade = input("Defina especialidade(Ortopedista, Pediatra, Clinico Geral)")
        medico = Medico(nome, cpf, salario, crm, especialidade)
        return medico
    
    elif tipo_funcionario == "enfermeira":
        nome = input("Digite o nome da enfermeira: ")
        cpf = input("Digite o CPF da enfermeira: ")
        salario = float(input("Digite o salário da enfermeira: "))
        especialidade = input("Digite a especialidade da enfermeira: ")
        enfermeira = Enfermeira(nome, cpf, salario, especialidade)
        return enfermeira
    
    elif tipo_funcionario == "técnica de enfermagem":
        nome = input("Digite o nome da técnica de enfermagem: ")
        cpf = input("Digite o CPF da técnica de enfermagem: ")
        salario = float(input("Digite o salário da técnica de enfermagem: "))
        turno = input("Digite o turno de trabalho da técnica de enfermagem: ")
        tecnica_enfermagem = TecnicaEnfermagem(nome, cpf, salario, turno)
        return tecnica_enfermagem
    
    else:
        print("Tipo de funcionário inválido.")
        return None