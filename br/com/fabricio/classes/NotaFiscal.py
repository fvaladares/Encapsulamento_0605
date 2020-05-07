class NotaFiscal:
    def __init__(self, codigo: str, comprador: str, qtd_itens: int, valor_item: float):
        self._codigo = codigo
        self._comprador = comprador
        self._qtd_itens = qtd_itens
        self._valor_item = valor_item

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    def get_valor_total(self):
        return float(self._qtd_itens) * float(self._valor_item)

    def imprimir_nota(self):
        # print()
        return str('Código NF: \t\t {}\n'
                   'Comprador: \t\t {}\n'
                   'Quantidade de itens: \t\t {}\n'
                   'Valor unitário: \t\t {}\n'
                   'Valor total: {}\n'.format(
            self._codigo, self._comprador,
            self._qtd_itens, self._valor_item,
            self.get_valor_total()
        ))
