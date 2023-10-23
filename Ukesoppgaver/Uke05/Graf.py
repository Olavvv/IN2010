
class Node:
    def __init__(self, data):
        self.data = data        #Nodens verdi
        self.besokt = False     #Er den besøkt? NB: dette kan brukes istedenfor en besøkt-liste!
        self.inDeg = 0          #Inngrad
        self.naboer = []        #Sine naboer (kanter)


    def __str__(self):
        penStr = str(self.data) + ": ["
        if (len(self.naboer) != 0):
            for kant in self.naboer:
                penStr += str(kant.data) + ", "
            penStr = penStr[:len(penStr) - 2]  #fjerner trailing komma
        return penStr + "]"



class Graf:
    def __init__(self, rettet):
        self.graf = {}          #Representert med en dictionary
        self.rettet = rettet    #Er grafen rettet?
    

    # Legg til en kant i grafen
    def leggTilKant(self, u, v) -> None:
        uNode = self.hentNode(u)
        vNode = self.hentNode(v)

        if (self.rettet):
            uNode.naboer.append(vNode)
            vNode.inDeg += 1
        else:
            uNode.naboer.append(vNode)
            vNode.naboer.append(uNode)

    
    # Henter eksisterende node fra grafen eller lager en ny
    def hentNode(self, data) -> Node:
        if (data not in self.graf):
            self.graf[data] = Node(data)
        return self.graf[data]



    # Oppdater alle noder til ubesøkt
    def settNoderUbesokt(self):
        for node in self.graf.values():
            node.besokt = False




    def __str__(self):
        penStr = ""
        for v in self.graf:
            penStr += str(self.graf[v]) + "\n"
        return penStr


# ----------------------------------------------------------------------------
#
#       Fyll inn her:
#           Gjør DFS og BFS enten iterativt eller rekursivt (eller begge !)


    # Dybde-først søk
    def DFS(self, data):
        stack = self.graf.values()[0] # Legger til startnoden i stacken.

        while len(stack) != 0:
            u = stack.pop()
            if not u.besokt:
                if (data == u.data):
                    return u
                for nabo in u.naboer:
                    stack.append(nabo)

        self.settNoderUbesokt()
        return None #Returnerer None om dataen vi soeker etter ikke er i grafen.
                



    # Bredde-først søk
    def BFS(self, data):
        queue = self.graf.values()[0] # Legger til startnoden i stacken.

        while len(queue) != 0:
            u = queue.pop(0)
            if not u.besokt:
                if (data == u.data):
                    return u
                for nabo in u.naboer:
                    queue.append(nabo)

        self.settNoderUbesokt()
        return None #Returnerer None om dataen vi soeker etter ikke er i grafen.
        


    # Topologisk sortering
    def topologiskSortering(self):
        stack = []
        output = {}
        for node in  self.graf:
            if node.inDeg == 0:
                stack.append(node)
        while len(stack) != 0:
            u = stack.pop()
            output




#
# ----------------------------------------------------------------------------


def main():
    # Lag en urettet graf

    graf = Graf(False)
    graf.leggTilKant("A", "D")
    graf.leggTilKant("E", "F")
    graf.leggTilKant("D", "E")
    graf.leggTilKant("F", "G")
    graf.leggTilKant("A", "B")
    graf.leggTilKant("A", "C")
    graf.leggTilKant("B", "C")
    graf.leggTilKant("C", "D")
    graf.leggTilKant("C", "F")

    graf.leggTilKant("X", "Y")
    graf.leggTilKant("X", "Z")
    graf.leggTilKant("Y", "Z")
    print(graf)


    print("\n---( Kaller på DFS)---")
    graf.DFS("A")


    graf.settNoderUbesokt()


    print("\n---( Kaller på BFS)---")
    graf.BFS("A")


    morgen = Graf(True)
    morgen.leggTilKant("Dusj", "Undertøy")
    morgen.leggTilKant("Dusj", "Sokker")
    morgen.leggTilKant("Dusj", "Bukse")
    morgen.leggTilKant("Dusj", "T-skjorte")
    morgen.leggTilKant("Undertøy", "Bukse")
    morgen.leggTilKant("Undertøy", "Bukse")
    morgen.leggTilKant("Sokker", "Sko")
    morgen.leggTilKant("Bukse", "Jakke")
    morgen.leggTilKant("Bukse", "Sko")
    morgen.leggTilKant("T-skjorte", "Jakke")
    morgen.leggTilKant("Jakke", "Dra")
    morgen.leggTilKant("Bukse", "Dra")
    morgen.leggTilKant("Sko", "Dra")
    morgen.leggTilKant("Frokost", "Pusse tenner")
    morgen.leggTilKant("Frokost", "Pusse tenner")
    morgen.leggTilKant("Frokost", "Dra")
    morgen.leggTilKant("Pusse tenner", "Dra")


    # Disse to linjene lager sykler
    #morgen.leggTilKant("Sko", "Sokker")
    #morgen.leggTilKant("Dra", "Dusj")


    print("\n---( Kaller på TopologiskSortering )---")
    morgen.topologiskSortering()
    

if __name__=="__main__":
    main()
