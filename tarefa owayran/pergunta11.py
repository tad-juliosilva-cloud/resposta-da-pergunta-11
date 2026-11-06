class TabelaHash:
    def _init_(self, tamanho=7):
        self.tabela = [[] for _ in range(tamanho)]

    def funcao_hash(self, chave):
        return chave % 7

    def inserir(self, ra, nome):
        self.tabela[self.funcao_hash(ra)].append((ra, nome))

    def buscar(self, ra):
        pos = self.funcao_hash(ra)
        for item in self.tabela[pos]:
            if item[0] == ra:
                return f"Encontrado na posição {pos}"
        return "Não encontrado"

    def exibir(self):
        for i, lista in enumerate(self.tabela):
            if lista:
                print(f"[{i}] " + " -> ".join(f"{ra}-{nome}" for ra, nome in lista))