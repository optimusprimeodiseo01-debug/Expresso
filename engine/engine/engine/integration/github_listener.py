import hashlib

class GitHubListener:

    def hash_issue(self, text):
        return hashlib.sha256(text.encode()).hexdigest()

    def extraer_refs(self, text):
        refs = []
        for line in text.split("\n"):
            if line.startswith("ref:"):
                refs.append(line.split("ref:")[1].strip())
        return refs

    def procesar_issue(self, text):
        return {
            "id": self.hash_issue(text),
            "refs": self.extraer_refs(text)
        }
