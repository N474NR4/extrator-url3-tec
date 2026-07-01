endereco = "Rua Dr Orlando Araujo Costa 1931, casa, Parque São Basilio, Pitanga, Pr, 85202-000"

import re  
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][0123456789][0123456789][0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)