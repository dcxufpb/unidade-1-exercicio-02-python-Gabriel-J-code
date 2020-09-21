import cupom

def test_exercicio1():
		cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
		cupom.logradouro = "Av. Projetada Leste"
		cupom.numero = 500
		cupom.complemento = "EUC F32/33/34"
		cupom.bairro = "Br. Sta Genebra"
		cupom.municipio = "Campinas"
		cupom.estado = "SP"
		cupom.cep = "13080-395"
		cupom.telefone = "(19) 3756-7408"
		cupom.observacao = "Loja 1317 (PDP)"
		cupom.cnpj = "42.591.651/0797-34"
		cupom.inscricao_estadual = "244.898.500.113"

		assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''


def test_exercicio2_tudo_vazio():
		cupom.nome_loja = ""
		cupom.logradouro = ""
		cupom.numero = 0
		cupom.complemento = ""
		cupom.bairro = ""
		cupom.municipio = ""
		cupom.estado = ""
		cupom.cep = ""
		cupom.telefone = ""
		cupom.observacao = ""
		cupom.cnpj = ""
		cupom.inscricao_estadual = ""

		assert cupom.imprime_dados_loja() == '''
, 0 
 -  - 
CEP: Tel 

CNPJ: 
IE: 
'''


def test_exercicio2_customizado():
		
		# Defina seus próprios valores para as variáveis a seguir
		cupom.nome_loja = "Tropical"
		cupom.logradouro = "Rua siqueira Campos"
		cupom.numero = 580
		cupom.complemento = ""
		cupom.bairro = "Centro"
		cupom.municipio = "Paulista"
		cupom.estado = "Pernambuco"
		cupom.cep = "53401-320"
		cupom.telefone = "(81) 3438-5714"
		cupom.observacao = ""
		cupom.cnpj = "37.886.772/0001-82"
		cupom.inscricao_estadual = "4232303-79"

		#E atualize o texto esperado abaixo
		assert cupom.imprime_dados_loja() == '''Tropical
Rua siqueira Campos, 580 
Centro - Paulista - Pernambuco
CEP:53401-320 Tel (81) 3438-5714

CNPJ: 37.886.772/0001-82
IE: 4232303-79
'''
