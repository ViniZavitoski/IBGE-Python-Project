class Variavel:

    def __init__(self, posicao_inicial, tamanho, codigo, descricao):
        self.posicao_inicial = posicao_inicial
        self.tamanho = tamanho
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = []

    def add_categoria(self, categoria):
        # categoria = dict {'categoria_tipo': tipo, 'categoria_descricao_tipo': descricao}
        self.categoria.append(categoria)

    def __str__(self):
        return self.codigo + " - " + self.descricao
