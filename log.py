from socket import PACKET_MULTICAST
import emitir_boleto


with open('hoje.txt','w') as arquivo: 
    for valor in placa: 
        arquivo.write(str(valor))