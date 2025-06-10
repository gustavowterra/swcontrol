
from django.core.mail import EmailMessage, get_connection
from django.core.mail.backends.smtp import EmailBackend

CONFIGURACOES_EMAIL = {
    'temtapetes': {
        'host': 'mail.temtapetes.com.br',
        'porta': 587,
        'usuario': 'cobranca@temtapetes.com.br',
        'senha': 'Cobranc@01',

    },
    'guermatapetes': {
        'host': 'mail.guermatapetes.com.br',
        'porta': 587,
        'usuario': 'cobranca@guermatapetes.com.br',
        'senha': 'Cobranc@01',
    },
}

def enviar_email_empresa(empresa, assunto, mensagem, destinatarios):
    config = CONFIGURACOES_EMAIL.get(empresa)

    if not config:
        raise ValueError(f"Empresa '{empresa}' não configurada.")

    connection = EmailBackend(
        host=config['host'],
        port=config['porta'],
        username=config['usuario'],
        password=config['senha'],
        use_tls=False,
        fail_silently=False
    )

    email = EmailMessage(
        subject=assunto,
        body=mensagem,
        from_email=config['usuario'],
        to=destinatarios,
        connection=connection
    )

    email.send()