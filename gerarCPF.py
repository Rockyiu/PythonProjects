#import re
#import sys



print('Gerar o primeiro e segundo digito de um CPF')
#entrada = input('CPF':)
cpf_enviado_usuario =  '86944116014' 
#cpf_enviado_usuario = re.sub(r'^[0-9], '', entrada)
#\.replace('.', '') \.replace('-','')
cpf_gerado_pelo_calculo = 0

#entrada_e_sequencial = entrada == entrada[0] *len(entrada)
# if entrada_e_sequencial:
    #print('Voce enviou dados sequenciais.')
    #sys.exit()


nove_digitos = cpf_enviado_usuario[:9]
dez_digitos = 0
contador_regressivo_1 = 10
contador_regressivo_2 = 11
resultado_1 = 0
resultado_2 = 0
primeiro_digito = 0
segundo_digito = 0

for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
primeiro_digito = (resultado_1 * 10) % 11  
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito) 

dez_digitos = nove_digitos + str(primeiro_digito)
print(dez_digitos)

for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
segundo_digito = (resultado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(segundo_digito)

cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')




