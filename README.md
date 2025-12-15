# Formulário de Login em Python (CustomTkinter)

Este projeto é um **formulário de login desenvolvido totalmente em Python**, utilizando a biblioteca **CustomTkinter**, que permite criar interfaces gráficas modernas, limpas e com suporte nativo a modo escuro.

O objetivo principal deste projeto é **estudar e praticar conceitos de interfaces gráficas (GUI)**, organização de código e lógica básica de autenticação, sendo ideal para iniciantes que estão aprendendo Python e querem sair do terminal para algo visual.

---

## 🧠 Visão geral do funcionamento

O formulário permite que o usuário:

* Digite um nome de usuário
* Digite uma senha
* Clique em um botão de login
* Receba um feedback visual informando se o login foi bem-sucedido ou não

A validação do login é feita comparando os dados digitados com valores definidos diretamente no código.

---

## 🧩 Tecnologias utilizadas

* **Python 3**
* **CustomTkinter** (extensão moderna do Tkinter)

O CustomTkinter facilita a criação de interfaces mais bonitas e organizadas, sem a complexidade de frameworks maiores.

---

## 🎨 Configuração visual da aplicação

Logo no início do código, a aparência da aplicação é configurada:

```python
ctk.set_appearance_mode("dark")
```

Isso ativa o **modo escuro**, melhorando a experiência visual e deixando a interface mais moderna.

---

## 🪟 Criação da janela principal

A janela principal do formulário é criada com:

```python
janela = ctk.CTk()
janela.title("Formulário de Cadastro")
janela.geometry("300x300")
```

Aqui são definidos:

* O tipo da janela (`CTk`)
* O título exibido no topo
* O tamanho da janela

---

## 👤 Campo de usuário

O campo de usuário é composto por dois elementos:

1. Um **Label**, que identifica o campo
2. Um **Entry**, onde o usuário digita seu nome

```python
Lbel_usuario = ctk.CTkLabel(janela, text="Login do Usuário: ")
entry_usuario = ctk.CTkEntry(janela, placeholder_text="Digite seu usuário")
```

O `placeholder_text` serve como uma dica visual dentro do campo de entrada.

---

## 🔒 Campo de senha

De forma semelhante ao campo de usuário, o campo de senha também possui:

* Um texto explicativo (Label)
* Um campo de entrada (Entry)

```python
Lbel_usuario = ctk.CTkLabel(janela, text="Senha do Usuário: ")
entry_senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha: ")
```

Este campo é responsável por capturar a senha digitada pelo usuário.

---

## 🔘 Botão de login

O botão é o elemento responsável por **executar a verificação do login**:

```python
bot_loguin = ctk.CTkButton(janela, text="Loguin", command=verificar_login)
```

Quando clicado, ele chama a função `verificar_login()`.

---

## ⚙️ Função de verificação de login

A função central do sistema é:

```python
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "Pedro" and senha == "1234":
        verificacao.configure(text="Login bem sucedido!", text_color="green")
    else:
        verificacao.configure(text="Login falhou. Tente novamente.", text_color="red")
```

Ela funciona da seguinte forma:

* Captura os valores digitados pelo usuário
* Compara com os dados esperados
* Exibe uma mensagem de sucesso ou erro
* Altera a cor do texto conforme o resultado

Esse feedback visual melhora muito a experiência do usuário.

---

## 📢 Mensagem de retorno ao usuário

O resultado do login é exibido em um `Label` vazio, que é atualizado dinamicamente:

```python
verificacao = ctk.CTkLabel(janela, text="")
```

Esse componente é atualizado dentro da função de verificação.

---

## ▶️ Execução da aplicação

Por fim, a aplicação é iniciada com:

```python
janela.mainloop()
```

Esse comando mantém a janela aberta e escutando as interações do usuário.

---

## 🚀 Possíveis melhorias futuras

Este projeto pode evoluir para algo mais robusto, como:

* Validação usando banco de dados
* Criptografia de senhas
* Máscara de senha no campo de entrada
* Tela de cadastro de usuários
* Navegação entre múltiplas janelas

---

## 📌 Conclusão

Este projeto é um excelente ponto de partida para quem está aprendendo **Python com interfaces gráficas**, ajudando a entender:

* Organização de código
* Eventos e callbacks
* Interação com o usuário
* Conceitos básicos de autenticação

Simples, didático e com muito espaço para evolução 🚀
