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
    
def manhatan_goal(self,no) : 
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        return manhatan(no.state,self.goal)
    
def mod_gen(pacman, obstaculos):
    obcopy =obstaculos.copy()
    for i in obstaculos:
        if manhatan(pacman,i) > 2:
            obcopy.remove(i)
    return obcopy       

    
def planear_online(pacman,pastilha,obstaculos):
    heurs = set()
    expanded = []
    print("MUNDO")
    str(display(pacman,pastilha,obstaculos,path=[]))
    print("MODELO")
    print(mod_gen(pacman, obstaculos))
    modelo = str(display(pacman,pastilha,obcopy,path=[]))
    print(modelo)
    #funcao shenanigans
    nits = 0
    totexp = 0
    
    while pacman != pastilha: 
        path=[]
        path.append(pacman)
        pac2 = pacproblem(pacman,pastilha,obcopy,expanded,...)
        
        exp = 0
        astar_search2(pacproblem(pac2,pac2.h))
        nits += 1
        print("ITERAÇÃO: " + str(nits))
        print(mod_gen(pacman, obstaculos))
        Node.expand(pacproblem)
        print(len(expanded))
            
        print("Expandidos " + str(exp))
        totexp += exp
    print("FIM: total de expandidos: "+ str(totexp))
    pass

def planear_adapt_online(pacman,pastilha,obstaculos):
    """ As novas heuristicas deste modelo vão ser calculadas da seguinte forma:
        tamanho da solução (neste caso é 7) - o custo do nó (isto é a distancia que o pacman teve de andar até ao nó em questão)
        Sendo assim neste exemplo o mapa das heuristicas ficaria assim:
        # . . . 
        # . # .
        # 7 # . 7 - 0(não teve que andar nada visto que está na posição inicial)
        # 6 # . 7 - 1(path = 1 o pacman teve de andar 1 para chegar a esta casa)
        # 5 # . 7 - 2(path = 2)
        # 4 # . ....
        # 3 # . 7 - 3(path = 3)
        # @ # *
        # . . ."""
 
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