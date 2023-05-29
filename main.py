import os
from Funcionario import Enfermeira, TecnicaEnfermagem, Medico
from cadastro import cadastrar_funcionario
from lista import atualizar_funcionario,buscar_funcionario,excluir_funcionario,listar_funcionarios
from menu import exibir_menu,limpar_tela

def executar_opcao(opcao, funcionarios):
    match opcao:
        case "1":
            medico = cadastrar_funcionario()
            funcionarios.append(medico)
            print("Funcionario cadastrado com sucesso!")
                     
        case "2":
            listar_funcionarios(funcionarios)
            
        case "3":
            cpf = input("Digite o CPF do funcionário a ser buscado: ")
            funcionario = buscar_funcionario(funcionarios, cpf)
            if funcionario:
                if isinstance(funcionario, Enfermeira):
                    print(f"Enfermeira encontrada: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
                elif isinstance(funcionario, TecnicaEnfermagem):
                    print(f"Técnica de Enfermagem encontrada: {funcionario.nome} - Turno: {funcionario.turno}")
                elif isinstance(funcionario, Medico):
                    print(f"Médico encontrada: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
            else:
                print("Funcionário não encontrado!")
                
        case "4":
            cpf = input("Digite o CPF do funcionário a ser atualizado: ")
            funcionario = buscar_funcionario(funcionarios, cpf)
            if funcionario:
                atualizar_funcionario(funcionario)
                print("Funcionário atualizado com sucesso!")
            else:
                print("Funcionário não encontrado!")
                
        case "5":
            cpf = input("Digite o CPF do funcionário a ser excluído: ")
            funcionario = buscar_funcionario(funcionarios, cpf)
            if funcionario:
                excluir_funcionario(funcionarios, funcionario)
                print("Funcionário excluído com sucesso!")
            else:
                print("Funcionário não encontrado!")
                
        case "6":
            print("Saindo...")
            return False
        case _:
            print("Opção inválida!")

    return True

def main():
    funcionarios = []
    executando = True

    while executando:
        limpar_tela()
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        limpar_tela()
        executando = executar_opcao(opcao, funcionarios)
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    match main():
        case True:
            main()
        case False:
            print("Encerrando programa...")