#Escrever aqui o ficheiro .py a entregar em conjunto com a submissao no questionario
from searchPlus import *
from p2_aux import *


    
def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))

def planear_online(pacman,pastilha,obstaculos):
    print("MUNDO")
    pworld = str(display(pacman,pastilha,obstaculos,path=[]))
    rworld = pworld.split()
    print(pworld)
    print("MODELO")
    modelo = quadro[:pastilha[1]][:pastilha[0]]
    print(modelo)
    #funcao shenanigans
    nits = 0
    print("ITERAÇÃO: " + str(nits))
    print("_path__")
    exp = 0 
    print("Expandidos " + str(exp))
    print("FIM: total de expandidos: "+ str(exp))
    
    
    pass
def planear_adapt_online(pacman,pastilha,obstaculos):
    print("MUNDO")
    display(pacman,pastilha,obstaculos,path=[])
    print("MODELO")
    #funcao shenanigans
    nits = 0
    print("ITERAÇÃO: " + nits)
    print(_path__)
    exp = 0 
    print("Expandidos " + exp)
    print("FIM: total de expandidos: "+ exp)
    heur = []
    print("Novas heurísticas: " + heur)
    pass
    

pacman=(1,1)
pastilha=(1,6)
l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10)
obstaculos=fronteira | l | c
print(fronteira)
planear_online(pacman,pastilha,obstaculos)