def tratar_mes(mes):
    meses_extenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    mes_tratado = ''

    for pos, var in enumerate(meses_extenso):
        if pos == int(mes)-1:
            mes_tratado = var
            return mes_tratado