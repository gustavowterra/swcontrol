from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('email_teste/', views.teste_email, name='email_teste'),
    path('colaborador/', views.form_Colaborador, name='form_vend'),
    path('dologin/', views.dologin, name='dologin'),
    path('logout/', views.logout_view, name='logout'),
    path('painel/', views.painel, name='painel'),
    ### CLIENTES ###
    path('cliente/', views.form_Clientes2, name='cadastrar-cliente'),
    path('cadastrar_cliente/', views.form_Clientes, name='cadastrar-cliente-pedido'),
    path('editar_cliente/<str:documento>', views.editar_clientes, name='editar-cliente-pedido'),
    path('consulta_cliente/', views.consulta_clientes, name='consulta_clientes'),
    path('cadastra_revenda/', views.cadastra_revenda, name='cadastra_revenda'),
    path('get-cliente/', views.get_clientes, name='get_clientes'),
    path('cliente-faturamento/', views.cliente_faturamento, name='cliente-faturamento'),
    path('download-relatorio-clientes/', views.report_clientes_xls, name='orcamentos-report'),
    path('painel_crm/', views.resumo_origens_clientes, name='resumo_origens_clientes'),

    ### FORNECEDOR ###
    path('cadastrar_fornecedor/', views.form_fornecedor, name='cadastrar-fornecedor'),
   ### PEDIDOS ###
    path('pedido/', views.pedido_create, name='painel_pedido'),
    path('editarpedido/<int:numero_pedido>/', views.editar_pedidos, name='editar_pedido'),
    path('editarpedidob/<int:numero_pedido>/', views.editar_pedidos_b, name='editar_pedidob'),
    path('editaritensnf/<int:numero_pedido>/', views.itens_edit_nfe, name='editaritensnf'),
    path('delete_pedido/', views.delete_pedido, name='delete_pedido'),
    path('get-comissao/', views.get_comissao, name='get-comissao'),
    path('get-price/', views.get_price, name='get-price'),
    path('pedido_gerente/', views.pedido_create_super, name='painel_pedido-gerente'),
    path('get-pedidos/', views.get_pedidos, name='get_pedidos'),
    path('save_itens/', views.item_save, name='item_save'),
    path('saveitenspedido/', views.saveitenspedido, name='saveitenspedido'),
    path('edita-itens/', views.editaitenspedido, name='edita-itens'),
    path('pedido_save/', views.pedido_save, name='pedido_save'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('meuspedidos/', views.meuspedidos, name='meus_pedidos'),
    path('painelpedidos/', views.meuspedidos_new, name='painel_pedidos'),
    path('consultarpedido/<int:numero_pedido>/', views.consultar_pedidos, name='consultar_pedido'),
    path('gerarecibo/<int:numero_pedido>/', views.gerar_recibo, name='gerar_pedido'),

    path('painelvendas/', views.painel_vendas, name='painel-vendas'),
    path('cadastrar_layout/', views.layout_pedido, name='layout_pedido'),

    #### FINANCEIRO #######
    path('contas_receber/', views.contas_receber, name='contas-receber'),
    path('editar_conta/<int:numero_pedido>/', views.editar_conta, name='editar-contas-receber'),
    path('contas_pagar/', views.contas_pagar, name='contas-pagar'),
    path('cadastrar_contas_pagar/', views.create_contas_pagar, name='cadastrar-contas-pagar'),
    path('editar_conta_pagar/<int:id>/', views.editar_conta_pagar, name='editar-contas-pagar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registra_entrega/<int:numero_pedido>', views.registrar_entrega, name='registra-entrega'),
    path('rejeita_entrega/<int:numero_pedido>', views.rejeitar_entrega, name='rejeita-entrega'),
    path('registra_coleta/<int:numero_pedido>', views.registrar_coleta, name='registra-coleta'),
    path('get_lista_comissao/', views.get_lista_comissao, name='get_lista_comissao'),
    path('comissoes/', views.comissao, name='comissoes'),
    path('busca_comissao/<str:vendedor>/<str:mes>/', views.busca_comissao, name='busca_comissao'),
    path('consultar_cep/', views.consultar_cep, name='consultar_cep'),
    path('condicoes_pagamento/', views.condicoes_pagamento, name='condicoes_pagamento'),



    ######## PRODUÇÃO ############
    path('producao/', views.producao, name='producao'),
    path('producao_total/', views.producao_total, name='producao_total'),
    path('filtrar_producao/', views.filtrar_producao, name='filtrar_producao'),
    path('filtrar_expedicao/', views.filtrar_expedicao, name='filtrar_expedicao'),
    path('producao_7/', views.producao_7, name='producao_7'),
    path('producao_3/', views.producao_3, name='producao_3'),
    path('producao_atrasados/', views.producao_atrasados, name='producao_atrasados'),
    path('expedicao/', views.painel_expedicao, name='expedicao'),
    path('expedicao_total/', views.expedicao_total, name='expedicao_total'),
    path('expedicao_financeiro/', views.expedicao_financeiro, name='expedicao_financeiro'),
    path('expedicao_liberados/', views.expedicao_liberados, name='expedicao_liberados'),

    path('comissoes/get_resumo_comissao_mes/', views.get_resumo_comissao_mes, name='resumo-comissao-mes'),
    path('emitir-nota/', views.emitir_nota, name='emitir-nf'),
    path('cancelar-nota/', views.cancelar_nota, name='cancelar-nf'),
    path('ajusta_comissao/', views.ajusta_comissao, name='ajusta_comissao'),
    path('registra_pagamento/', views.registra_pagamento, name='registra_pagamento'),
    path('emitir-boleto/', views.gerar_boleto, name='emitir-boleto'),
    path('delete-boleto/', views.delete_boleto, name='delete-boleto'),
    path('webhook/', views.webhook_view, name='webhook'),
    ######### LOGISTICA ######################
    path('expedicao_rota/', views.expedicao_rota, name='expedicao_rota'),
    path('envia_para_entrega/', views.select_regiao_entrega, name='envia-entrega'),
    path('regiao1/', views.regiao_1, name='regiao1'),
    path('regiao2/', views.regiao_2, name='regiao2'),
    path('regiao3/', views.regiao_3, name='regiao3'),
    path('regiao4/', views.regiao_4, name='regiao4'),
    path('regiao5/', views.regiao_5, name='regiao5'),
    path('regiao6/', views.regiao_6, name='regiao6'),
    path('regiao7/', views.regiao_7, name='regiao7'),
    path('regiao8/', views.regiao_8, name='regiao8'),
    path('reg_transportadora/', views.regiao_transportadora, name='regiao-transportadora'),
    path('reg_retirada/', views.expedicao_retirada, name='expedicao-retirada'),
    path('mensagem_sucesso_layout/', views.mensagem_sucesso_layout, name='mensagem_sucesso_layout'),


    path('entrega/', views.entregas, name='entregas'),

    path('cadastrar-transportadora/', views.transportadora, name='cadastrar-transportadora'),
    path('atualiza-status/', views.atualiza_status, name='atualiza-status'),
    path('edita-status/', views.edita_status, name='edita-status'),
    path('expedicao_frete/', views.expedicao_frete, name='expedicao_frete'),
    path('geradocpedido/<int:numero_pedido>/', views.gerar_docpedido, name='gerardocpedido'),
    path('pedidoaberto/', views.pedido_create_aberto, name='pedidoaberto'),
    path('save-opened/', views.save_aberto_itens, name='save-opened'),
    path('emitir-nota-aberta/', views.nota_aberta, name='nota-aberta'),
    path('download-comissao-excel/', views.report_comissoes_xls, name='comissao-excel'),
    path('download-comissao-excel-mensal/', views.report_comissoes_mensal_xls, name='comissao-excel-mensal'),
    path('download-relatorio-contasreceber/', views.report_contas_receber_xls, name='contas-receber-report'),
    path('download-relatorio-contaspagar/', views.report_contas_pagar_xls, name='contas-pagar-report'),
    path('download-relatorio-pedidos/', views.report_pedidos_xls, name='pedidos-report'),
    path('painel-boletos/<str:empresa>/', views.painel_boletos, name='painel-boletos'),
    path('boletos_total/<str:empresa>/<str:status>/', views.boletos_total, name='boletos-total'),
    path('filtrar_boletos/', views.filtrar_boletos, name='filtrar-boletos'),
    path('sincronizar_notas/', views.sincroniza_notas, name='sincronizar_notas'),
    path('sincroniza_pedido/<int:numero_pedido>/', views.sincroniza_nota_unica, name='sincroniza_nota_unica'),
    path('painel-notas/<str:empresa>/', views.painel_notas, name='painel-notas'),
    path('notas_total/<str:empresa>/<str:periodo>/', views.notas_total, name='notas-total'),
    path('flag-impressao/', views.flag_impressao, name='flag-impressao'),
    path('confirma_pedido/', views.confirma_pedido, name='confirma_pedido'),
    path('unificar_contas/<str:documento>/', views.cobranca_unificada, name='unificar_contas'),
    path('unificar_cobrancas/', views.unificar_cobranca, name='unificar_cobranca'),
    path('registra_recebimento/', views.registra_recebimento, name='registra_recebimento'),
    path('delete_cliente/', views.delete_cliente, name='delete_cliente'),
    path('consulta_colaboradores/', views.consulta_colaboradores, name='consulta_colaboradores'),

    path('editar_colaborador/<int:id>/', views.editar_colaborador, name='editar-colaborador'),
    path('upload_foto_vendedor/', views.upload_foto_vendedor, name='upload_foto_vendedor'),

    ########## ORÇAMENTOS ###############################
    path('orcamento/', views.novo_orcamento, name='orcamento'),
    path('painel_orcamento/', views.painel_orcamento, name='painel_orcamento'),
    path('template_fornecedor/', views.template_fornecedor, name='template_fornecedor'),
    path('template_orcamento/<int:numero_orcamento>/', views.gerar_orcamento, name='gerar_orcamento'),
    path('template_orcamento_tem/<int:numero_orcamento>/', views.gerar_orcamento_tem, name='gerar_orcamento_tem'),
    path('adiciona_comentario/', views.orcamento_comentario, name='add_comentario'),
    path('atualiza-status-orcamento/', views.atualiza_status_orcamento, name='atualiza-status-orcamento'),
    path('get_observacoes/<int:orcamento_id>/', views.get_observacoes, name='get_observacoes'),
    path('delete_orcamento/', views.delete_orcamento, name='delete_orcamento'),
    path('edita_orcamento/<int:orcamento_id>/', views.edita_orcamento, name='edita_orcamento'),
    path('atualiza-valor-final/', views.atualiza_valor_final, name='atualiza_valor_final'),
    path('orcamento_carimbo/', views.orcamento_carimbo, name='orcamento_carimbo'),

    path('download-relatorio-orcamentos/', views.report_orcamentos_xls, name='orcamentos-report'),

    ############ GUIAS DE REPARO ################################
    path('solicita-reparo/', views.solicita_reparo, name='solicita_reparo'),
    path('nova_guia_reparo/<int:numero_pedido>/', views.nova_guia_reparo, name='nova_guia_reparo'),
    path('guia_reparo/<int:numero_pedido>/', views.gerar_guia_reparo, name='guia_reparo'),
    path('guia_reparo_documento/<int:numero_pedido>/', views.documento_guia_reparo, name='guia_reparo_documento'),
    path('painel_guias/', views.painel_guias, name='guia_reparo'),
    path('delete_guia/', views.delete_guia, name='delete_guia'),


    ############ WEBHOOKS NOTAS FISCAIS ###########################
    path('wnotasgrf/', views.webhook_notas_grf, name='wnotasgrf'),
    path('wnotastem/', views.webhook_notas_tem, name='wnotastem'),


    ############ RELATORIOS ####################
    path('relatorio_log/', views.relatorio_log, name='relatorio_log'),
    #path('indicadores/', views.indicadores, name='indicadores'),


]

