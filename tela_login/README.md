Descrição:
----------------------------------------
Este projeto utiliza a biblioteca PySimpleGUI para criar uma interface gráfica de usuário (GUI) simples que coleta informações de e-mail, senha e caminhos de pastas para anexos e planilhas. O objetivo é demonstrar a criação de uma aplicação GUI que valida entradas de e-mail e senha, além de permitir a seleção de pastas específicas.

Funcionalidades:
-----------------------
Entrada de E-mail e Senha:
-------------------------------------------
A GUI permite que o usuário insira um endereço de e-mail e uma senha, com um campo adicional para confirmar a senha.

Validação de E-mail e Senha:
-----------------------------------------
A função validar_email utiliza expressões regulares para garantir que o e-mail inserido siga um padrão aceitável.
As senhas inseridas nos campos "Senha" e "Confirmar senha" são comparadas para garantir que são iguais.

Seleção de Pastas:
-----------------------------------------
A interface inclui botões que abrem um navegador de arquivos para selecionar pastas para anexos e planilhas.

Mensagens de Erro:
----------------------------------
Se as senhas não coincidirem ou se o e-mail for inválido, a aplicação exibirá uma mensagem de erro apropriada utilizando pop-ups.

Saída no Console:
------------------------------------------
Se todas as entradas forem válidas, as informações coletadas são impressas no console.

Dependências:
-------------------------------------------
- PySimpleGUI: Biblioteca utilizada para criar a interface gráfica de usuário.
- re: Biblioteca padrão do Python para trabalhar com expressões regulares, usada para validar o formato do e-mail.
- time: Biblioteca padrão para implementar a função sleep, que adiciona um pequeno atraso antes de fechar a janela.

Como Usar:
---------------------
Instale as Dependências:
---------------------------------
1. Assegure-se de que você tem o PySimpleGUI instalado. Você pode instalá-lo usando pip: pip install pysimplegui

2. Execute o Script:

Execute o script Python. Uma janela com a interface de entrada será aberta.

3. Insira as Informações:

Preencha os campos de e-mail, senha e confirme a senha. Selecione as pastas conforme necessário.

4. Salvar:

Clique no botão "Salvar". Se houver algum erro nas entradas, uma mensagem pop-up aparecerá com instruções. Caso contrário, as informações serão exibidas no console.

Observações:
------------------------------------------
Este exemplo é uma demonstração básica de como criar e validar entradas em uma GUI com PySimpleGUI.
É importante sempre validar e tratar as entradas de usuário para garantir a segurança e a integridade dos dados.
