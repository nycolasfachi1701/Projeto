#RA: 1134317 - Nycolas Musskopf Fachi

import random

FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'Adidas Apple BMW Coca-Cola Disney Ford Google Honda Ikea Intel KFC Lego Mercedes-Benz Microsoft Nike Pepsi Samsung Toyota Twitter Volkswagen Walmart Yahoo Zara Audi Chevrolet'.split()

def main():
    
    global FORCAIMG
 
    print('F O R C A')
    letrasErradas = '' 
    letrasAcertadas = '' 
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True
 
    while jogando: 
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta) 
 
        palpite = recebePalpite(letrasErradas + letrasAcertadas) 
 
        if palpite in palavraSecreta: 
            letrasAcertadas += palpite 
 
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas): 
                print("Parabens! A palavra secreta e "+palavraSecreta+'! Voce ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite 
 
            if len(letrasErradas) == len(FORCAIMG) - 1: 
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
 
                print("Voce exagerou o seu limite de palpites!")
                print("Depois de "+str(len(letrasErradas))+' letras erradas e'+str(len(letrasAcertadas)), end = ' ')
                print('palpites corretos, a palavra era '+palavraSecreta+'.')
 
                jogando = False
 
        if not jogando: 
            if JogarNovamente(): 
                letrasErradas = '' 
                letrasAcertadas = '' 
                jogando = True
                palavraSecreta = geraPalavraAleatoria().upper() 
                
def geraPalavraAleatoria():
   
    global palavras
    return random.choice(palavras)

def imprimeComEspacos(palavra):
    
    for letra in palavra:
        print(letra, end = ' ')
 
    print()
 

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
   
    global FORCAIMG  
    print(FORCAIMG[len(letrasErradas)]+'\n')  
 
    print("Letras Erradas:", end = ' ') 
    imprimeComEspacos(letrasErradas) 

    vazio = '_'*len(palavraSecreta) 
    for i in range(len(palavraSecreta)): 
        if palavraSecreta[i] in letrasAcertadas: 
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:] 
 
    imprimeComEspacos(vazio) 

def recebePalpite(palpiteFeitos):
    
    
    while True: 
        palpite = input('Adivinhe alguma letra. \n').upper() 
        
        if len(palpite) != 1: 
            print('Coloque uma unica letra')
        elif palpite in palpiteFeitos: 
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z': 
            print('Escolha Somente uma letra!')
        else:
            return palpite  

def JogarNovamente():
   
    return input("Voce quer jogar novamente? (sim ou nao)\n").upper().startswith('S')  
def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
   
    
    ganhou = True
    for letra in palavraSecreta: 
        if letra not in letrasAcertadas: 
            ganhou = False 
            break 
 
    return ganhou 
 
main()