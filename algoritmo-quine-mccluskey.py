def agrupar(mintermos, bits):                                      #funcao pra agrupar os mintermos em quantidades de 1s

    grupos = {};                                                   #dicionario em que ficarão os mintermos agrupados por quantidade de 1s
    for i in range(bits+1):
        grupos[i] = [];

    for i in mintermos:
        bin = format(i, 'b').zfill(bits);                          #transformando os mintermos em binário e preenchendo com zero 

        ones = bin.count('1');
        
        grupos[ones].append(bin);                                  #agrupa os grupos em suas respectivas posições no dicionario (posição 0, grupo de zero 1s...)

    return grupos;

def comparar(mintermo1, mintermo2):                                #funçao que verifica se os mintermos que diferem por 1bit sao combinaveis (se forem, combina)
    diferente = 0;
    posicao = -1;
    for i in range(len(mintermo1)): 
        if (mintermo1[i] != mintermo2[i]):                         #rastrea que houve diferença e armazena a posiçao de onde difere
            diferente += 1;
            posicao = i;
        
    if diferente != 1:                                             #só tem que diferir uma vez, se diferir mais, não é combinavel
        return None;

    else:
        minCombinado = '';                                                      
        for i in range(len(mintermo1)):                            #se a posicao do mintermo for a que os bits diferem, coloca - no lugar. se nao for, só repete o bit
            if i == posicao:
                minCombinado += '-';
            else:
                minCombinado += mintermo1[i];
        
        return minCombinado;                                     #retorna o mintermo ja combinado, com - onde os bits diferiram

def combinar(grupos):                                           #primeira rodada em que combinamos os termos 
    novos_mintermos = {};                                       #onde guardaremos os novos mintermos agrupados
    mintermos_usados = set();                                   #guardando os mintermos q ja foram usados                
    for i in range(len(grupos)-1):                                 #vamos comparar os mintermos do grupo i com os mintermos do grupo i+1 (zero 1 com um 1, um 1 com dois 1s, dois 1s com três 1s...), pois estão em ordem e diferem de apenas 1 bit     
        for mintermo1 in grupos[i]:
            for mintermo2 in grupos[i+1]:
                resultado = comparar(mintermo1, mintermo2);             
                if resultado != None:                               #se o resultado for um mintermo combinado, a gente marca que os mintermos que geraram ele já foram usados
                    mintermos_usados.add(mintermo1);
                    mintermos_usados.add(mintermo2);
                
                    ones = resultado.count('1');                    #aqui agrupamos os novos mintermos combinados em outro dicionario, em ordem de 1s novamente para os vizinhos i e i+1 diferirem de apenas 1 bit, em ordem.
                    if ones not in novos_mintermos:
                        novos_mintermos[ones] = [];
                    if resultado not in novos_mintermos[ones]:
                        novos_mintermos[ones].append(resultado);
                    
    implicantes_primos = [];                                            
    for i in grupos:                                                 #aqui percorremos o grupo original e guardamos os mintermos que não foram combinados (implicantes primos)
        for mintermo in grupos[i]:
            if mintermo not in mintermos_usados:
                implicantes_primos.append(mintermo);

    return novos_mintermos, implicantes_primos;                      #retorna os novos mintermos para serem comparados novamente e a lista dos implicantes primos


def algoritmo_quine_mccluesky(mintermos, bits):                       #aqui implementamos, finalmente, o algoritmo em si, que chama todas as funções que foram implementadas aqui
    grupos = agrupar(mintermos, bits);                                #formamos os grupos com os mintermos iniciais
    implicantes_finais = []                                            #lista final onde todos os implicantes primos ficarão armazenados para usarmos na tabela final

    while True:                                                       #loop que fica combinando os mintermos até não ser possível fazer mais combinações
        novos_grupos, implicantes_primos = combinar(grupos);

        implicantes_finais += implicantes_primos;                      #vai guardando todos os implicantes primos das combinações em uma lista

        if not novos_grupos:
            break;

        grupos = novos_grupos;                                          #vai guardando os novos grupos combinados e chama esses novos grupos quando o laço repetir

    tabela = tabela_de_cobertura(implicantes_finais, mintermos)         #tabela que associa todos os implicantes primos finais com os mintermos com que se encaixam
    essenciais = primos_essenciais(tabela)                              #implicantes primos essenciais                    
    
    resultado_final = list(essenciais)
    mintermos_cobertos = set()

    for e in essenciais:                                                  #percorre os essenciais e ve quais mintermos sao cobertos por eles
        for m in mintermos:
            mBin = format(m, 'b').zfill(bits)
            cobre = True
            for i in range(len(e)):
                if e[i] != '-' and e[i] != mBin[i]:
                    cobre = False
                    break
            if cobre:
                mintermos_cobertos.add(m)   

    for m in mintermos:                                                    #verifica quais mintermos não sao cobertos pelos implicantes essenciais. se não for, pega o primeiro implicante associado ao mintermo sem implicante essencial e coloca no resultado final
        if m not in mintermos_cobertos:
            implicante_escolhido = tabela[m][0]
            if implicante_escolhido not in resultado_final:
                resultado_final.append(implicante_escolhido)
            
            mintermos_cobertos.add(m) 

        return resultado_final                                              #retorna todos os implicantes que cobrem os mintermos originais (de forma mínima, obviamente)

def tabela_de_cobertura(implicantes_finais, mintermos):
    tabela = {};                                                        #dicionario em que serão armazenados os implicamentes primos relacionados aos mintermos que se encaixam com ele
    for min in mintermos:
        tabela[min] = [];                                               
        
    for implicante in implicantes_finais:                                   #aqui, pega cada mintermo, passa pra binário e compara os bits com os bits de cada implicante. Se o implicante se encaixa com o mintermo (ex: --1 com 011 / -0- 101), vai ser guardado no dicionario associado ao mintermo (011: --1 / 101: -0-)
        for m in mintermos:
            minBin = format(m, 'b').zfill(len(implicante));
            cobre = True;
                
            for i in range(len(implicante)):
                if implicante[i] != '-' and implicante[i] != minBin[i]:
                    cobre = False;
                    break;

            if cobre:
                tabela[m].append(implicante);

    return tabela;                                                           #retorna o dicionario com os implicantes primos associados a cada mintermo com que se encaixam
                
def primos_essenciais(tabela):
    essenciais = set();
    for lista in tabela.values():
        if len(lista) == 1:
            essenciais.add(lista[0]);
    
    return essenciais;