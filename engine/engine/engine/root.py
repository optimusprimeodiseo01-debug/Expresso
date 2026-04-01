class Root:

    def score(self, repo):
        forks = repo.get("forks", 1)
        refs = len(repo.get("refs", []))
        size = repo.get("size", 1)

        return (forks * refs) / (size + 1)

    def buscar_optimo(self, repos):
        return sorted(repos, key=self.score, reverse=True)
