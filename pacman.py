#Escrever aqui o ficheiro .py a entregar em conjunto com a submissao no questionario
from searchPlus import *

def line(x, y, dx, dy, length):
    """Uma linha de células de comprimento 'length' começando em (x, y) na direcção (dx, dy)."""
    return {(x + i * dx, y + i * dy) for i in range(length)}

def quadro(x, y, length):
    """Uma moldura quadrada de células de comprimento 'length' começando no topo esquerdo (x, y)."""
    return line(x,y,0,1,length) | line(x+length-1,y,0,1,length) | line(x,y,1,0,length) | line(x,y+length-1,1,0,length)

def manhatan(p,q):
    (x1,y1) = p
    (x2,y2) = q
    return abs(x1-x2) + abs(y1-y2)


def display(pacman,pastilha,obstaculos,path=[]):
    """ print the state please"""
    pacmanX,pacmanY=pacman
    osXs={x for (x,_) in obstaculos | {pastilha, pacman}}
    minX=min(osXs)
    maxX=max(osXs)
    osYs={y for (_,y) in obstaculos | {pastilha, pacman}}
    minY=min(osYs)
    maxY=max(osYs)
    output=""
    for j in range(minY,maxY+1):
        for i in range(minX,maxX+1):
            if pacman ==(i,j):
                ch = '@'
            elif pastilha==(i,j):
                ch = "*"
            elif (i,j) in obstaculos:
                ch = "#"
            elif (i,j) in path:
                ch = '+'
            else:
                ch = "."
            output += ch + " "
        output += "\n"
    print(output)
    
    
    
    def astar_search(problem, h=None):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))
   
def planear_online(pacman,pastilha,obstaculos):
    print("MUNDO")
    display(pacman,pastilha,obstaculos,path=[])
    print("MODELO")
    #funcao shenanigans
    
    print()
    print()
    
    pass
def planear_adapt_online(pacman,pastilha,obstaculos):
    pass
    

pacman=(1,1)
pastilha=(1,6)
l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10)
obstaculos=fronteira | l | c
print(fronteira)
display(pacman,pastilha,obstaculos,path=[])
