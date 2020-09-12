# Cria titulo para menu, para programas são executado dentro do terminal

def box(txt):
    size = len(txt)
    print('\33c')
    print('-'*(len(txt)+4))
    print(f"\33[1;33m{'|':<} { txt :^} {'|':>}\33[m")
    print('-'*(len(txt)+4))

def list_menu(lit):
    for c in range(len(lit)):
        print(f"[ {c} ] {lit[c]}")

def list_al():  
    dados = [{'Nome': 'Eduardo', 'Idade': 22 , 'Id': 562154},{'Nome': 'Carlos', 'Idade':22, 'Id': 521364}]
    print('='*29)
    print(f"| NOME |...| IDADE |...| ID |")
    print('='*29)
    for c in range(len(dados)):
        print(f"{dados[c]['Nome']}   {dados[c]['Idade']}    {dados[c]['Id']}")


list_al()