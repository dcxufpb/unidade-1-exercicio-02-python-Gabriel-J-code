nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def imprime_dados_loja():    		
	nota = nome_loja+"\n"
	nota+="%s, %d %s\n" % (logradouro, numero, complemento)
	nota += "%s - %s - %s\n" % (bairro, municipio, estado)
	nota += "CEP:%s Tel %s\n" % (cep, telefone)
	nota += observacao+"\n"
	nota += "CNPJ: %s\n" % cnpj
	nota += "IE: %s \n"% inscricao_estadual
	return nota