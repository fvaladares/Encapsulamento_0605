from br.com.fabricio.classes.NotaFiscal import NotaFiscal

if __name__ == '__main__':
    print('.:| Cadastro de nota fiscal |:.')
    cod = input('Código NF: ')
    comprador = input('Comprador: ')
    qtd_itens = input('Quantidade de itens: ')
    valor_unit = input('Valor unitário: ')

    nf = NotaFiscal(cod, comprador, qtd_itens, valor_unit)

    print('Antes da modificação:')
    print(nf.imprimir_nota())
    nf.codigo = 2021
    # print('Código: ' + str(nf.codigo))
    print('Código: {}'.format(nf.codigo))
