from email.policy import default

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Produtos (models.Model):
    descricao = models.CharField(max_length=120)
    preco_base_comissao1 = models.FloatField()
    preco_base_comissao2 = models.FloatField()
    preco_base_comissao3 = models.FloatField()
    preco_base_comissao4 = models.FloatField()
    preco_base_comissao5 = models.FloatField()
    percentual_comissao1 = models.IntegerField()
    percentual_comissao2 = models.IntegerField()
    percentual_comissao3_interno = models.IntegerField()
    percentual_comissao4_interno = models.IntegerField()
    percentual_comissao5_interno = models.IntegerField()
    percentual_comissao3_externo = models.IntegerField()
    percentual_comissao4_externo = models.IntegerField()
    percentual_comissao5_externo = models.IntegerField()
    tipo_medida = models.CharField(max_length=255, default='m2')
    prazo_fabricacao = models.IntegerField(default=15)
    ncm=models.IntegerField(default=84284000)
    codigo = models.IntegerField(default=None, null=True)
    medida_padrao = models.CharField(max_length=3, default='NAO', null=True)
    tamanho_padrao = models.CharField (max_length=255, default='1', null=True)
    produto_adicional = models.CharField(max_length=3, default='NAO', null=True)
    flag_conferir = models.IntegerField(default=0)
    modelo = models.CharField(max_length=255, default=None, null=True)


    def __str__(self):
        return "{}".format(self.descricao)
class Tipo_Pedido (models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.descricao)

class Produtos_Revenda (models.Model):
    descricao = models.CharField(max_length=120)
    preco_base_1 = models.FloatField()
    preco_base_2 = models.FloatField()
    preco_base_3 = models.FloatField()
    preco_base_4 = models.FloatField(default=None)
    tipo_medida = models.CharField(max_length=255, default='m2')
    prazo_fabricacao = models.IntegerField(default=15)
    ncm = models.IntegerField(default=84284000)
    codigo = models.IntegerField(default=None, null=True)
    medida_padrao = models.CharField(max_length=3, default='NAO', null=True)
    tamanho_padrao = models.CharField(max_length=255, default='1', null=True)
    comissao = models.IntegerField(default=1)
    flag_conferir = models.IntegerField(default=0)
    modelo = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return "{}".format(self.descricao)



class TipoDocumento (models.Model):
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return"{}".format(self.descricao)

class TipoPgto (models.Model):
    NAO = 'NÃO'
    SIM = 'SIM'
    ACEITA_PARCELA = (
        (NAO, 'NÃO'),
        (SIM, 'SIM')
    )

    descricao = models.CharField(max_length=50)
    nome_banco = models.CharField(max_length=50, null=True)
    ag_banco = models.CharField(max_length=50, null=True)
    cc_banco = models.CharField(max_length=50, null=True)
    aceita_parcela = models.CharField(choices=ACEITA_PARCELA, max_length=3, default='NÃO')
    numero_parcelas = models.IntegerField(default=1)
    prazo_dias = models.CharField(max_length=20, default=30)

    def __str__(self):
        return"{}".format(self.descricao)


class Estado (models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)
    def __str__(self):
        return"{}".format(self.nome)

class Cidade (models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return"{}".format(self.nome)

class Bairro(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    zona = models.CharField(max_length=255, default=None, null=True)
    regiao = models.CharField(max_length=255, default='', null=True)

    def __str__(self):
        return "{}".format(self.nome)


class Empresas(models.Model):
    nome = models.CharField(max_length=100)
    razaosocial = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)
    inscricao_estadual = models.IntegerField(default=None, null=True)
    cidade = models.ForeignKey(Cidade,on_delete=models.SET_NULL, null=True)
    bairro = models.ForeignKey(Bairro,on_delete=models.SET_NULL, null=True)
    uf = models.ForeignKey(Estado,on_delete=models.SET_NULL, null=True)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=11, default='24342702')
    numero = models.IntegerField(default=11)
    endereco_numero = models.CharField(default=11, max_length=10)
    complemento = models.CharField(max_length=100, default=None, null=True)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    ultimo_pedido_ref = models.BigIntegerField(default=0)
    token_nota = models.CharField(max_length=255)
    url_nota = models.CharField(max_length=255)
    flag_pagamento = models.IntegerField(default=0)
    aws_chave = models.CharField(max_length=255, null=True, default=None)
    aws_id = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return"{}".format(self.nome)
class Status_Colaborador (models.Model):

    descricao = models.CharField(max_length=255)

    def __str__(self):
        return"{}".format(self.descricao)


class Motivos_Desligamento(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return"{}".format(self.descricao)


class Colaborador(models.Model):
    GERENTE = 'Gerente'
    ADMINISTRADOR = 'Administrador'
    VENDEDOR_INTERNO = 'Vendedor Interno'
    VENDEDOR_EXTERNO = 'Vendedor Externo'
    PRODUCAO = 'Producao'
    AUXILIAR = 'Auxiliar'
    LOGISTICA = 'Logistica'
    EXPEDICAO = 'Expedicao'
    FINANCEIRO = 'Financeiro'
    RECEPCIONISTA = 'Recepcionista'

    FUNCAO_CHOICES = (
        (GERENTE, 'Gerente'),
        (ADMINISTRADOR, 'Administrador'),
        (VENDEDOR_INTERNO, 'Vendedor Interno'),
        (VENDEDOR_EXTERNO, 'Vendedor Externo'),
        (PRODUCAO, 'Produção'),
        (AUXILIAR, 'Auxiliar'),
        (LOGISTICA, 'Logística'),
        (EXPEDICAO, 'Expedicao'),
        (FINANCEIRO, 'Financeiro'),
        (RECEPCIONISTA, 'Recepcionista'),
    )

    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_admissao = models.DateField(default=None, null=True)
    data_desligamento = models.DateField(default=None, null= True)
    status = models.ForeignKey (Status_Colaborador, on_delete=models.CASCADE, default=None, null=True)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    telefone_comercial = models.CharField(max_length=15, default=None, null=True)
    funcao = models.CharField(max_length=30, choices=FUNCAO_CHOICES, default=" ")
    endereco = models.CharField(max_length=255)
    numero_endereco = models.CharField(max_length=5, default=None, null=True)
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    empresa = models.ForeignKey(Empresas,on_delete=models.SET_NULL, null=True)
    motivo_desligamento = models.ForeignKey(Motivos_Desligamento, on_delete=models.SET_NULL, null=True, default=None)
    caminho_foto = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return self.nome

class Tipo_Indicacao(models.Model):
    descricao = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return self.descricao


class Leads (models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    documento = models.CharField(max_length=255, null=True, default=None)
    email = models.CharField(max_length=255, null=True, default=None)


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    documento = models.CharField(max_length=50)
    inscricao_estadual = models.CharField(max_length=10, default=None, null=True)
    dt_abertura=models.DateField(null=True, default=None)
    nome_contato = models.CharField(max_length=50, default=None, null=True)
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15)
    CEP = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    numero_endereco=models.IntegerField()
    complemento=models.CharField(max_length=100, null=True)
    ponto_referencia = models.CharField(max_length=100, default=None, null=True)
    total_pedidos = models.IntegerField(default=None, null=True)
    ultimopedido = models.IntegerField(default=None, null=True)
    id_clientecob = models.CharField(max_length=100, default=None, null=True)
    score = models.FloatField(default=5.0)
    tipo_cliente = models.ForeignKey (Tipo_Pedido, models.SET_NULL, null=True, default=1)
    pagamento_boleto = models.CharField(max_length=3, default='NAO')
    tipo_entrada = models.ForeignKey(Tipo_Indicacao, on_delete=models.SET_NULL, null=True, default=None)
    flag=models.IntegerField(default=0)
    data_cadastro = models.DateField(null=True, default=None)

    def __str__(self):
        return self.nome
class Bancos(models.Model):
    nome = models.CharField(max_length=100)
    agencia = models.CharField(max_length=10)
    numero_conta = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresas, models.SET_NULL, null=True)

    def __str__(self):
        return self.nome





class Inadimplencia (models.Model):

    data = models.CharField(max_length=12, null=True)
    flag = models.IntegerField(null=True, default=None)

    def __str__(self):
        return "{}".format(self.data)


class Temp_Contas_Receber (models.Model):
    ABERTO = 'Aberto'
    A_Vencer = 'A Vencer'
    Vencida = 'Vencida'
    Pago = 'Pago'
    PENDENTE_FATURAMENTO = 'Pendente Faturamento'


    STATUS_CONTA = (
        (ABERTO, 'Aberto'),
        (PENDENTE_FATURAMENTO, 'Pendente Faturamento'),
        (A_Vencer, 'A Vencer'),
        (Vencida, 'Vencida'),
        (Pago, 'Pago'),

    )
    pedido = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=100)
    data_vencimento = models.DateField(null=True, default=None)
    data_pagamento = models.DateField(null=True, default=None)
    tipo_pgto = models.CharField(max_length=50, default="PIX")
    numero_parcela = models.IntegerField()
    total_parcelas = models.IntegerField()
    valor = models.FloatField()
    status_conta = models.CharField(max_length=50, choices=STATUS_CONTA, default="Aberto")
    momento_pagamento = models.CharField(max_length=100, default=None, null=True)
    caminho_boleto = models.CharField(max_length=100, default=None, null=True)
    id_cobranca = models.CharField(max_length=100, default=None, null=True)
    status_cobranca = models.CharField (max_length=100, default=None, null=True)
    flag_uni = models.IntegerField(null=True, default=0)

    def __str__(self):
        return "{}".format(self.descricao)

class Tipo_Fornecedor (models.Model):

    descricao = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return "{}".format(self.descricao)

class Fornecedor (models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, null=True)
    documento = models.CharField(max_length=50, unique=True)
    nome_contato = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    tipo_fornecedor = models.ForeignKey(Tipo_Fornecedor, on_delete=models.SET_NULL, null=True)
    cep = models.CharField(max_length=255, null=True, default=None)
    bairro = models.CharField(max_length=255, null=True, default=None)
    cidade = models.CharField(max_length=255, null=True, default=None)
    uf = models.CharField(max_length=255, null=True, default=None)
    logradouro = models.CharField(max_length=255, null=True, default=None)
    numero = models.CharField(max_length=255, null=True, default=None)
    complemento = models.CharField(max_length=255, null=True, default=None)



    def __str__(self):
        return "{}".format(self.nome)

class Contas_Pagar (models.Model):
    ABERTO = 'Aberto'
    A_Vencer = 'A Vencer'
    Vencida = 'Vencida'
    Pago = 'Pago'
    Aguardando = 'Aguardando'

    STATUS_CONTA = (
        (ABERTO, 'Aberto'),
        (A_Vencer, 'A Vencer'),
        (Vencida, 'Vencida'),
        (Pago, 'Pago'),
        (Aguardando, 'Aguardando')

    )
    pedido = models.IntegerField(null=True, default=None)
    descricao = models.CharField(max_length=100)
    data_vencimento = models.DateField(null=True)
    data_pagamento = models.DateField(null=True, default=None)
    tipo_pgto = models.ForeignKey(TipoPgto, on_delete=models.SET_NULL, null=True)
    numero_parcela = models.IntegerField(default='1')
    total_parcelas = models.IntegerField(default='1')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    valor = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS_CONTA, default="Aberto")
    outras_informacoes = models.CharField(max_length=255, null=True)
    documento_caminho = models.CharField(max_length=255, null= True)
    comprovante_caminho = models.CharField(max_length=255, null=True, default=None)
    notafiscal = models.CharField(max_length=255, null=True, default=None)
    notafiscal_caminho = models.CharField(max_length=255, null=True, default=None)
    empresa = models.ForeignKey(Empresas, on_delete=models.SET_NULL, default=None, null=True)
    banco = models.ForeignKey(Bancos, on_delete=models.SET_NULL, default=None, null=True)


    def __str__(self):
        return "{}".format(self.descricao)



class Revenda (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, default="")
    nivel = models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.cliente)

class Condicoes_Pagamentos (models.Model):
    descricao = models.CharField(max_length=255)
    quantidades_parcelas = models.IntegerField(null=True, default=None)


    def __str__(self):
        return "{}".format(self.descricao)


class Pedidos (models.Model):
    ABERTO = 'Aberto'
    Confirma_Valores = 'Confirma os Valores'
    Duplicado = 'duplicado'
    PRODUÇÃO = 'Producao'
    PENDENTE_FINANCEIRO = 'Pendente Financeiro'
    LIBERADO_ENTREGA = 'Liberado para Entrega'
    LIBERADO_COLETA = 'Liberado Coleta'
    LIBERADO_RETIRADA = 'Liberado Retirada Cliente'
    EM_ENTREGA = 'Em Rota de Entrega'
    FINANCEIRO = 'Financeiro'
    FINALIZADO = 'Finalizado'
    ENTREGUE = 'Entregue'
    FATURAMENTO = 'Faturamento'
    PENDENTE_LOGISTICA = 'Pendente Logistica'
    EXPEDICAO = 'Expedicao'
    NFE_ANTECIPADA = 'Nfe Antecipada'
    CONFERIR_ITEM = 'Conferir Item'



    STATUS_CHOICES = (
        (ABERTO, 'Aberto'),
        (Confirma_Valores, 'Confirma os Valores'),
        (Duplicado, 'duplicado'),
        (PRODUÇÃO, 'Producao'),
        (PENDENTE_FINANCEIRO, 'Pendente Financeiro'),
        (LIBERADO_ENTREGA, 'LIBERADO_ENTREGA'),
        (EM_ENTREGA, 'EM_ENTREGA'),
        (FINALIZADO, 'FINALIZADO'),
        (ENTREGUE, 'Entregue'),
        (FINANCEIRO, 'Financeiro'),
        (FATURAMENTO, 'Faturamento'),
        (PENDENTE_LOGISTICA, 'Pendente Logistica'),
        (EXPEDICAO, 'Expedicao'),
        (NFE_ANTECIPADA, 'Nfe Antecipada'),
        (LIBERADO_COLETA, 'Liberado Coleta'),
        (LIBERADO_RETIRADA, 'Liberado Retirada Cliente'),
        (CONFERIR_ITEM, 'Conferir Item')

    )
    numero = models.IntegerField()
    datapedido = models.DateField()
    prazo_entrega = models.DateField()
    data_entrega_efetiva = models.DateTimeField(null=True, default=None)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Aberto")
    valorTotal = models.FloatField()
    valorTotalParcial = models.FloatField()
    frete_valor = models.FloatField(null=True, default=0.00)
    frete_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    descontototal = models.FloatField()
    pgtotipo = models.ManyToManyField(TipoPgto, related_name='tipos_pagamento')
    Vendedor = models.CharField(max_length=200, default=" ")
    vendedor_comissao =models.FloatField()
    vendedor_comissaov = models.FloatField(null=True)
    Vendedor2 = models.CharField(max_length=200, default=" ", null=True)
    vendedor2_comissao = models.FloatField(null=True)
    vendedor2_comissaov = models.FloatField(null=True)
    itemPedido = models.ManyToManyField(Produtos, related_name='itens_pedido')
    cliente_pedido=models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    cep_entrega=models.CharField(max_length=10)
    uf_entrega=models.CharField(max_length=2)
    cidade_entrega=models.CharField(max_length=100)
    bairro_entrega=models.CharField(max_length=100)
    zona_entrega = models.CharField(max_length=100, default=None, null=True)
    endereco_entrega=models.CharField(max_length=100)
    numero_end_entrega=models.IntegerField()
    complemento=models.CharField(max_length=100, null=True)
    ponto_referencia_entrega = models.CharField(max_length=100, default=None, null=True)
    observacao=models.CharField(max_length=500, null=True)
    empresa_pedido = models.ForeignKey(Empresas, on_delete=models.SET_NULL, null=True, default='')
    data_fim_producao = models.DateField(null=True, default=None)
    caminho_layout = models.CharField(max_length=300, null=True, default=None)
    pagamento_entrega = models.FloatField(null=True, default=0.00)
    pagamento_antecipado = models.FloatField(null=True, default=0.00)
    datapg_antecipado = models.DateField(null=True, default=None)
    bancopg_antecipado = models.CharField(max_length=100, null=True, default='')
    pagamento_faturado =  models.FloatField(null=True, default=0.00)
    caminho_nfe = models.CharField(max_length=200, default=None, null=True)
    flag_nfe = models.IntegerField(default=0)
    caminho_xml = models.CharField(max_length=200, default=None, null=True)
    numero_nfe = models.IntegerField(default=None, null=True)
    referencia_nfe = models.CharField (max_length=100, default=None, null=True)
    dataEmissao_nfe = models.DateField(default=None, null=True)
    informacoes_adicionais = models.CharField (max_length=1000, default=None, null=True)
    operacao_nota = models.IntegerField (default=1, null=True)
    frete_peso = models.FloatField(default=0.00, null=True)
    frete_flag = models.IntegerField(default=0)
    frete_volume = models.IntegerField(default=0, null=True)
    justificativa_comissao = models.CharField(max_length=1000, default=None, null=True)
    tipo_pedido = models.ForeignKey(Tipo_Pedido, on_delete=models.SET_NULL, null=True, default=1)
    informacoes_pagamento = models.CharField (max_length=1000, default=None, null=True)
    retirada_flag = models.IntegerField(default=0)
    fundo = models.CharField(max_length=255, default="", null=True)
    borda = models.CharField(max_length=255, default="", null=True)
    letra = models.CharField(max_length=255, default="", null=True)
    valor_acerto = models.FloatField(default=0.00, null=True)
    valor_repasse = models.FloatField(default=0.00, null=True)
    valor_nota = models.FloatField(default=0.00, null=True)
    logomarca = models.CharField(max_length=255, default="", null=True)
    tipo_entrega = models.CharField(max_length=255, default=" ", null=True)
    flag_aberto = models.IntegerField(default=0)
    bonificado = models.ForeignKey (Fornecedor, related_name='bonificados_pedido', on_delete=models.SET_NULL, null=True, default="")
    flag_nfe_antecipada = models.IntegerField(default=0)
    flag_impressao = models.IntegerField(default=1, null=True)
    flag_entrega_rejeitada = models.IntegerField(default=0, null=True)
    observacao_entrega_rejeitada = models.CharField(max_length=255, default=" ", null=True)
    comprador_nome = models.CharField (max_length=255, default='', null=True)
    comprador_email = models.CharField (max_length=255, default='', null=True)
    comprador_telefone = models.CharField (max_length=255, default='', null=True)
    flag_notificacao = models.IntegerField(default=1)
    flag_reparo = models.IntegerField(default=0)
    condicao_pagamento = models.ForeignKey(Condicoes_Pagamentos, on_delete=models.SET_NULL, null=True, default=None)


    def __str__(self):
        return"{}".format(self.numero)

class Itens_Pedido(models.Model):
    nome = models.CharField(max_length=100)
    pedido = models.IntegerField()
    quantidade = models.IntegerField()
    medida = models.CharField(max_length=100, default='0', null=True)
    medida_final = models.FloatField(default=1)
    largura = models.FloatField(default=0.00,null=True)
    comprimento = models.FloatField(default=0.00,null=True)
    preco = models.FloatField()
    desconto = models.FloatField(null=True, default='0.00')
    total_item = models.FloatField()
    valor_base = models.FloatField(default=1)
    produto = models.ForeignKey(Produtos, related_name='produto_item', on_delete=models.SET_NULL, null=True)
    produto_revenda = models.ForeignKey(Produtos_Revenda, related_name='produto_revenda_item', on_delete=models.SET_NULL, null=True)
    observacao_item = models.CharField(max_length=200, default=None, null=True)
    tipo = models.CharField(max_length=255, null=True, default='PADRAO')
    nome_nf = models.CharField(max_length=100, default='', null=True)
    preco_nf = models.FloatField(default=0, null=True)
    quantidade_nf = models.IntegerField(default=0, null=True)
    total_item_nf = models.FloatField(default=0, null=True)
    flag_editado = models.IntegerField(default=0)
    adicional = models.FloatField(default=0.00, null=True)
    frete_embutido = models.FloatField(default=0.00, null=True)
    pedido_itens = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return "{}".format(self.nome)

class Contas_Receber (models.Model):
    ABERTO = 'Aberto'
    A_Vencer = 'A Vencer'
    Vencida = 'Vencida'
    Pago = 'Pago'
    PENDENTE_FATURAMENTO = 'Pendente Faturamento'


    STATUS_CONTA = (
        (ABERTO, 'Aberto'),
        (PENDENTE_FATURAMENTO, 'Pendente Faturamento'),
        (A_Vencer, 'A Vencer'),
        (Vencida, 'Vencida'),
        (Pago, 'Pago'),

    )
    pedido = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=100)
    data_vencimento = models.DateField(null=True, default=None)
    data_pagamento = models.DateField(null=True, default=None)
    tipo_pgto = models.CharField(max_length=50, default="PIX")
    numero_parcela = models.IntegerField()
    total_parcelas = models.IntegerField()
    valor = models.FloatField()
    status_conta = models.CharField(max_length=50, choices=STATUS_CONTA, default="Aberto")
    momento_pagamento = models.CharField(max_length=100, default=None, null=True)
    caminho_boleto = models.CharField(max_length=100, default=None, null=True)
    id_cobranca = models.CharField(max_length=100, default=None, null=True)
    status_cobranca = models.CharField (max_length=100, default=None, null=True)
    pedido_conta = models.ForeignKey (Pedidos, on_delete=models.SET_NULL, default=None, null=True)
    banco = models.ForeignKey(Bancos, on_delete=models.SET_NULL, default=None, null=True)
    flag_uni = models.IntegerField(null=True, default=0)




    def __str__(self):
        return "{}".format(self.descricao)

class Registra (models.Model):
    numero_registro = models.IntegerField(unique=True)
    pedido = models.ForeignKey(Pedidos,on_delete=models.SET_NULL, null=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True)
    data_entrega = models.DateTimeField(default=None, null=True)
    data_rejeicao = models.DateTimeField(default=None, null=True)
    nome_recebedor = models.CharField(max_length=255, null=True)
    observacao_rejeicao = models.CharField(max_length=255, null=True, default=None)
    documento_recebedor = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.numero_registro)

class Producao(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    item_nome = models.ForeignKey(Itens_Pedido, on_delete=models.SET_NULL, null=True)
    hora_conclusao = models.DateTimeField(null=True, default=None)


def upload_layout(instance, filename):
    # Define o caminho e o nome do arquivo de upload
    return f'layouts/{instance.numero_pedido.numero}/{filename}'

class Layout(models.Model):
    numero_pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    arquivo_path = models.FileField(upload_to=upload_layout)
    arquivo_nome = models.CharField(max_length=255, default=None)

    def save(self, *args, **kwargs):
        # Se um arquivo já existe, exclua-o antes de salvar o novo arquivo
        if self.pk:
            old_layout = Layout.objects.get(pk=self.pk)
            if old_layout.arquivo != self.arquivo:
                old_layout.arquivo.delete()

        super(Layout, self).save(*args, **kwargs)

    def __str__(self):
        return f"Layout {self.pk} - Pedido {self.numero_pedido.numero}"

class Numero_Pedidos (models.Model):
    numero_disponivel = models.BigIntegerField()
    ultimo_numero_salvo = models.BigIntegerField()
    ultimo_numero_enviado = models.BigIntegerField()
    empresa = models.ForeignKey(Empresas, on_delete=models.SET_NULL, null=True, default="")




class Temp_Pedidos (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, default=None)
    pedido = models.BigIntegerField(null=True, default=None)
    tipo_pedido = models.ForeignKey(Tipo_Pedido, on_delete=models.SET_NULL, null=True, default=None)
    empresa = models.ForeignKey(Empresas, on_delete=models.SET_NULL, null=True, default=None)
    vendedor1 = models.ForeignKey(Colaborador, related_name='pedido_vendedor1', on_delete=models.SET_NULL, null=True, default=None)
    vendedor2 = models.ForeignKey(Colaborador, related_name='pedido_vendedor2', on_delete=models.SET_NULL, null=True, default=None)
    comissao1 = models.FloatField(default=0.00, null=True)
    comissao2 = models.FloatField(default=0.00, null=True)
    total_parcial = models.FloatField(default=0.00, null=True)

    def __str__(self):
        return f"Layout {self.pk} - Pedido {self.pedido}"



class Rota (models.Model):
    pedido = models.ForeignKey(Pedidos,on_delete=models.SET_NULL, null=True)
    regiao = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.regiao)

class Status_Reparo (models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.descricao)

class Guia_Reparo (models.Model):
    codigo = models.BigIntegerField()
    status = models.ForeignKey(Status_Reparo, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    observacao = models.TextField( null=True, default=None)
    data_criacao = models.DateField()
    data_alteracao = models.DateField()
    data_coleta = models.DateTimeField(null=True, default=None)
    usuario_coleta = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True)
    data_entrega = models.DateTimeField(null=True, default=None)
    usuario_entrega = models.ForeignKey(Colaborador, related_name='usuario_entrega', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.codigo)

class Reparos (models.Model):
    guia = models.ForeignKey(Guia_Reparo,on_delete=models.PROTECT, null=True, default=None)
    pedido = models.ForeignKey (Pedidos,on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey (Itens_Pedido, on_delete=models.SET_NULL, null=True)
    observacao = models.CharField(max_length=255)
    data_coleta = models.DateTimeField(null=True,default=None)
    usuario_coleta = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.pedido.numero)




class atendimento (models.Model):
    telefone = models.CharField(max_length=13)
    data = models.DateField()
    tempo = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, default='Aberto')
    ultima_opcao = models.IntegerField(null=True)

class Cob_Unificada (models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    conta = models.ForeignKey(Contas_Receber, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)


class RegistrosLog (models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    data = models.DateTimeField()
    operacao = models.CharField(max_length=300, null=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    conta = models.ForeignKey (Contas_Receber, on_delete=models.PROTECT, null=True )


class TipoMedida(models.Model):
    descricao = models.CharField(max_length=10)

    def __str__(self):
        return "{}".format(self.descricao)


class StatusOr (models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return "{}".format(self.descricao)

class OpcoesFornecedor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nome)
class TemplateFornecedor(models.Model):

    descricao = models.CharField(max_length=255, null=True, default=None)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT, null=True, default=None)
    caminho_imagem = models.CharField(max_length=255, null=True, default=None)
    fornecedor = models.ForeignKey(OpcoesFornecedor, on_delete=models.PROTECT, null=True, default=None)
    def __str__(self):
        return "{}".format(self.descricao)





class Orcamentos(models.Model):

    vendedor = models.ForeignKey (Colaborador, on_delete=models.PROTECT)
    codigo = models.BigIntegerField()
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    datacriacao = models.DateField()
    dataexpiracao = models.DateField(null=True, default=None)
    data_ultima_atualizacao = models.DateField(null=True, default=None)
    validade = models.IntegerField()
    status = models.ForeignKey(StatusOr, on_delete=models.PROTECT)
    valor_total = models.FloatField(default=0.00)
    valor_com_desconto = models.FloatField(default=0.00)
    texto_garantia = models.CharField(max_length=255, default=None, null=True)
    caminho1 = models.CharField(max_length=255, null=True, default=None)
    forma_pagamento = models.CharField(max_length=255, null=True, default=None)
    cliente_lead = models.ForeignKey(Leads, on_delete=models.PROTECT, null=True, default=None)
    endereco_entrega = models.CharField (max_length=255, null=True, default= None)
    bairro_entrega = models.CharField(max_length=255, null=True, default=None)
    cidade_entrega = models.CharField(max_length=255, null=True, default=None)
    estado_entrega = models.CharField(max_length=255, null=True, default=None)

    flag_carimbo = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "{}".format(self.codigo)


class ItensOrcamento (models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    comprimento = models.FloatField()
    largura = models.FloatField()
    tipo_medida = models.ForeignKey(TipoMedida, on_delete=models.PROTECT)
    orcamento = models.ForeignKey(Orcamentos, on_delete=models.PROTECT, null=True, default=None)
    valor_item = models.FloatField()
    valor_total_item = models.FloatField(null=True, default=0.00)
    codigo_orcamento = models.BigIntegerField()

    def __str__(self):
        return "{}".format(self.descricao)


class Orcamento_Comentarios (models.Model):
    texto = models.TextField()
    orcamento = models.ForeignKey(Orcamentos, on_delete=models.PROTECT, null=True, default=None)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT, null=True, default=None)
    data = models.DateField(null=True, default=None)


class Orcamentos_Templates(models.Model):
    orcamento = models.ForeignKey (Orcamentos, on_delete=models.SET_NULL, null=True)
    template = models.ForeignKey (TemplateFornecedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.orcamento)
