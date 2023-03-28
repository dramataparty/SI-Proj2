#Escrever aqui o ficheiro .py a entregar em conjunto com a submissao no questionario
from searchPlus import *
from p2_aux import *


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
    
def mod_gen(pacman, obstaculos):
    obcopy =obstaculos.copy()
    for i in obstaculos:
        if manhatan(pacman,i) > 2:
            obcopy.remove(i)
    return obcopy       


def best_first_graph_search2(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return Node, explored

def planear():
    p = pacproblem
    astar_search(p())
    
    
def planear_online(pacman,pastilha,obstaculos):
    heurs = set()
    expanded = []
    heurs = {}
    print("MUNDO")
    str(display(pacman,pastilha,obstaculos,path=[]))
    print("MODELO")
    obcopy = mod_gen(pacman, obstaculos)
    modelo = str(display(pacman,pastilha,obcopy,path=[]))
    print(modelo)
    
    #funcao shenanigans
    nits = 0
    totexp = 0
    encountrou = bool(pacman=self.goal)
    while pacman != pastilha: 
        path=[]
        path.append(pacman)
        pac2 = pacproblem(pacman,pastilha,obcopy,expanded,...)
        """if bateu:
            break"""
        exp = 0
        
        nits += 1
        print("ITERAÇÃO: " + str(nits))
        print(modelo)
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