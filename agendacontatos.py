file_handle = open ('agenda.txt', 'w')
agenda = []     

def i_nome():    
     return(input("Nome: "))


def i_telefone():
     return(input("Telefone: "))


def i_email():   
     return(input("Email: "))


def listar_dados(nome, telefone, email):   
     print("Nome: %s\nTelefone: %s\nEmail: %s" % (nome, telefone, email))


def pesquisa(nome):           
     name = nome.lower()     
     for d, e in enumerate(agenda):
         if (e[0].lower() == name):  
               return d            
     return None                   

def novo():                   
     global agenda            
     nome = i_nome()          
     telefone = i_telefone()
     email = i_email()        
     agenda.append([nome, telefone, email])

def apagar():    
     global agenda
     nome = i_nome()
     p = pesquisa(nome)
     if (p != None):     
         del agenda[p] 
     else:
         print("Nome não encontrado.")


def editar():                      
     p = pesquisa(i_nome())        
     if (p != None):    
         nome = agenda[p][0]       
         telefone = agenda[p][1]   
         email = agenda [p][2]
         
         print("\n **** Encontrado **** \n")
         
         listar_dados(nome, telefone, email) 
         nome = i_nome()         
         telefone = i_telefone() 
         email = i_email()       
         agenda[p] = [nome, telefone, email] 
     else:
         print("Nome não encontrado!")



def listar():
    
     print("\n*************************** \n \tAgenda\n\n***************************")

     file_handle = open ('agenda.txt', 'a')
     file_handle.write(str(agenda))
     
     for coisa in agenda:
          file_handle = open ('agenda.txt', 'r')
          file_handle.readlines()
          print(listar_dados(coisa[0], coisa[1], coisa[2]) , '\n')
     return ' '
     print("***************************\n")
     

file_handle.close()

def pesquisar():                   
     p = pesquisa(i_nome())        
     if (p != None):                 
         nome = agenda[p][0]       
         telefone = agenda[p][1]   
         email = agenda[p][2]      
         print("\n **** Encontrado **** \n")      
         listar_dados(nome, telefone, email)  
     else:
          print("Nome não encontrado!")      

def validar(pergunta, inicio, fim):          
     while True:                            
         try:                               
               valor = int(input(pergunta)) 
               if (inicio <= valor <= fim):   
                   return(valor)            
                                     
         except ValueError:                 
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():                   
     print("""
   1 - Novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Todos os Contatos
   5 - Apagar um contato
   6 - Sair
""")
   
     return validar("Escolha uma opção: ",1,6) 


while (True):                             
     opção = menu()
     if (opção == 6):                      
         break
     elif (opção == 1):
         novo()
     elif (opção == 2):
         editar()
     elif (opção == 3):
         pesquisar()
     elif (opção == 4):
         listar()
     elif (opção == 5):
         apagar()

         
#desenvolvido por Adrielle Alves & Adnaelle Alves
#Trabalho de FuP
#                   #MeDáUm10
#                   #EmNomeDeJesus
#                   #É_Serio
