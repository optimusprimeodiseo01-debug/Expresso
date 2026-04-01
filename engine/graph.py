import networkx as nx
from engine.brain import Brain

class TapizGraph:

    def __init__(self):
        self.grafo = nx.DiGraph()
        self.brain = Brain()

    def agregar_idea(self, idea_id, referencias):
        if len(referencias) == 0:
            raise Exception("idea invalida: requiere copia")

        self.grafo.add_node(idea_id)

        for ref in referencias:
            self.grafo.add_edge(ref, idea_id)

        if not nx.is_directed_acyclic_graph(self.grafo):
            raise Exception("violacion DAG")

    def eficiencia(self, idea):
        refs = list(self.grafo.predecessors(idea))
        profundidad = self._profundidad(idea)

        if profundidad == 0:
            return 0

        energia = self.brain.energia(refs)
        return energia / profundidad

    def _profundidad(self, nodo):
        preds = list(self.grafo.predecessors(nodo))
        if not preds:
            return 1
        return 1 + max(self._profundidad(p) for p in preds)

    def priorizar(self):
        scores = {
            n: self.eficiencia(n)
            for n in self.grafo.nodes
        }
        return sorted(scores, key=scores.get, reverse=True)

    def ejecutar(self):
        orden = list(nx.topological_sort(self.grafo))

        resultado = []
        for nodo in orden:
            resultado.append({
                "idea": nodo,
                "eficiencia": self.eficiencia(nodo)
            })

        return resultado
