from engine.graph import TapizGraph
from engine.root import Root

class Executor:

    def __init__(self):
        self.graph = TapizGraph()
        self.root = Root()

    def cargar_local(self, ideas):
        for idea in ideas:
            self.graph.agregar_idea(
                idea["id"],
                idea["refs"]
            )

    def integrar_externo(self, repos):
        candidatos = self.root.buscar_optimo(repos)

        for repo in candidatos[:3]:
            hash_repo = repo["id"]

            self.graph.agregar_idea(
                hash_repo,
                repo.get("refs", [])
            )

    def run(self):
        return self.graph.ejecutar()
