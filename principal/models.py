from django.db import models


class Contato(models.Model):
    ASSUNTO_CHOICES = (
        ("banho", "Serviço de Banho"),
        ("atendimento", "Atendimento ao Cliente"),
        ("infraestrutura", "Instalações e Limpeza"),
        ("preco", "Preços e Transparência"),
        ("outro", "Outro"),
    )

    nome = models.CharField(verbose_name="Nome", max_length=50)
    email = models.EmailField(verbose_name="E-mail", max_length=100)
    assunto = models.CharField(
        verbose_name="Assunto",
        max_length=20,
        default="todos",
        choices=ASSUNTO_CHOICES,
    )
    mensagem = models.TextField(verbose_name="Mensagem")
    data = models.DateTimeField(verbose_name="Data Envio", auto_now_add=True)
    lido = models.BooleanField(verbose_name="Lido", default=False, blank=True)

    def __str__(self):
        return f"{self.nome} [{self.email}]"

    class Meta:
        verbose_name = "Formulário de Contato"
        verbose_name_plural = "Formulários de Contatos"
        ordering = ["-data"]
