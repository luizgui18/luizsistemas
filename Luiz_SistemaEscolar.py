disciplinas = ["Algoritmos","Segurança","Desenv. Web"]
turma = [] 

def cadastra_aluno(matricula, nome, idade):
    turma.append(
        {
            "matricula":matricula,
            "nome":nome,
            "idade":idade,
            "notas":[[],[],[]] 
        }
    )

def encontra_aluno(matricula):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def inicializa_notas_aluno(matricula):
    aluno = encontra_aluno(matricula)
    for notas_disciplina in aluno["notas"]:
        for cont_notas in range(0,5):
            notas_disciplina.append(0)

def valida_nota(nota):
  
    if nota < 0 or nota > 10:
      
        return False
    return True

def cadastra_notas_aluno(matricula, cod_disciplina):
    aluno = encontra_aluno(matricula)
    for cont_notas in range(0,5):
        mensagem = "Informe a " + str(cont_notas + 1) + " nota: "
        nota = float(input(mensagem))
        while not valida_nota(nota): 
            print("Nota inválida!")
            mensagem = "Informe a " + str(cont_notas + 1) + " nota: " 
            nota = float(input(mensagem))
        aluno["notas"][cod_disciplina][cont_notas] = nota

def cadastra_notas_aluno(matricula, cod_disciplina):
    aluno = encontra_aluno(matricula)
    for cont_notas in range(0,5):
        mensagem = "Informe a " + str(cont_notas + 1) + " nota: "
        nota = float(input(mensagem))
        while not valida_nota(nota):
            print("Nota inválida!")
            mensagem = "Informe a " + str(cont_notas + 1) + " nota: "
            nota = float(input(mensagem))
        aluno["notas"][cod_disciplina][cont_notas] = nota

def gera_relatorio_desempenho(matricula):
  
    aluno = encontra_aluno(matricula)
    cont_disciplina = 0
    for notas_disciplina in aluno["notas"]:
        media = 0
        for nota in notas_disciplina:
            media += nota
        media /= len(notas_disciplina)
        print(disciplinas[cont_disciplina] + ": ", + media)
        cont_disciplina += 1

def consulta_informacoes_aluno(matricula):
   
    aluno = encontra_aluno(matricula)
    print("Nome: ", aluno["nome"])
    cont_disciplina = 0
    for notas_disciplina in aluno["notas"]:
        print(disciplinas[cont_disciplina] + ": ", notas_disciplina) 
        cont_disciplina += 1

opcao = 0

def menu():

    opcao = int(input("""                                                                                                      
    1 - Cadastrar novo aluno(a)                         
    2 - Incluir notas                                    
    3 - Gerar relatório de desempenho                    
    4 - Consultar informações 
    Escolha uma operação:  """))                     
    if(opcao == 1):
        matricula = int(input("""
    Informe a matrícula: """))
        nome = input("""
    Informe o nome: """)
        idade = int(input("""
    Informe a idade: """))  
        cadastra_aluno(matricula, nome, idade)
        inicializa_notas_aluno(matricula)
   
    elif(opcao == 2):

        matricula = int(input("""
    Informe a matrícula: """))
        cod_disciplina = int(input("""
    Informe o código da disciplina: """))
        cadastra_notas_aluno(matricula, cod_disciplina)
    elif(opcao == 3):
        matricula = int(input("""
    Informe a matrícula: """))
        gera_relatorio_desempenho(matricula)
    elif(opcao == 4):
        matricula = int(input("""
    Informe a matrícula: """))
        consulta_informacoes_aluno(matricula)
    else:
        print("Opção invalida, repita o processo")
menu()
repete = input("""
    Deseja realizar mais alguma operação? (s/n): """)
while repete == "s":
    menu() 
    repete = input("""
    Deseja realizar mais alguma operação? (s/n): """) 