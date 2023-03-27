#Escrever aqui o ficheiro .py a entregar em conjunto com a submissao no questionario
from searchPlus import *
from p2_aux import *

def astar_search2(problem, h=None):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        #h = memoize(h or problem.h, 'h')
        f = lambda n: n.path_cost + h(n)
        return best_first_graph_search(problem, lambda n: n.path_cost + h(n))

class pacproblem(Problem):

    def __init__(self, initial, goal, obstacles):
        self.initial=initial
        self.goal=goal 
        self.obstacles=set(obstacles) - {initial, goal}

    directions = {"N":(0, -1), "W":(-1, 0), "E":(1,  0),"S":(0, +1)}  
    
    costs = {"N":1, "W":1, "E":1,"S":1}
                  
    def result(self, state, action): 
        "Tanto as acções como os estados são representados por pares (x,y)."
        (x,y) = state
        (dx,dy) = self.directions[action]
        return (x+dx,y+dy) 
    
    def actions(self, state):
        """Podes move-te para uma célula em qualquer das direcções para uma casa 
           que não seja obstáculo."""
        x, y = state
        return [act for act in self.directions.keys() if (x+self.directions[act][0],y+self.directions[act][1]) not in self.obstacles]
    
    def path_cost(self,c,state,action,new):
        return c+self.costs[action]
    

    
def planear_online(pacman,pastilha,obstaculos):
    heurs = set()
    expanded = []
    print("MUNDO")
    pworld = str(display(pacman,pastilha,obstaculos,path=[]))
    print("MODELO")
    obcopy =obstaculos.copy()
    for i in obstaculos:
        if manhatan(pacman,i) > 2:
            obcopy.remove(i)    
    modelo = str(display(pacman,pastilha,obcopy,path=[]))
    print(modelo)
    #funcao shenanigans
    nits = 0
    totexp = 0
    '''while pacman != pastilha: 
        path=[]
        path.append(pacman)
        pac2 = pacproblem(pacman,pastilha,obcopy,expanded,sol)
        exp = 0
        astar_search2(pacproblem(pac2,pac2.manhatan_goal))
        nits += 1
        print("ITERAÇÃO: " + str(nits))
        print(str(display(pacman,pastilha,obcopy,path)))
        Node.expand(pacproblem)
        print(expanded)
            
        print("Expandidos " + str(exp))
        totexp += exp
    print("FIM: total de expandidos: "+ str(totexp))'''
    pass

def planear_adapt_online(pacman,pastilha,obstaculos):
    print("MUNDO")
    display(pacman,pastilha,obstaculos,path=[])
    print("MODELO")
    #funcao shenanigans
    nits = 0
    print("ITERAÇÃO: " + nits)
    print()
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
obstaculos= fronteira | l | c
print(fronteira)
planear_online(pacman,pastilha,obstaculos)