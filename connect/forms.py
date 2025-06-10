from django import forms
from .models import Colaborador, Cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class FormVend (forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'


class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'email',
            'documento',
            'telefone1',
            'telefone2',
            'CEP',
            'estado',
            'cidade',
            'bairro',
            'endereco',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            Fieldset(
                'Informações Pessoais',
                'nome',
                'email',
                'cpf',
                'telefone1',
                'telefone2',
                css_class='col-md-4'
            ),
            Fieldset(
                'Endereço',
                'CEP',
                'estado',
                'cidade',
                'bairro',
                'endereco',
                css_class='col-md-4'
            ),
            ButtonHolder(
                Submit('submit', 'Salvar', css_class='btn btn-primary')
            )
        )