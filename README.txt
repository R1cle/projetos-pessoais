# 🧾 Gerador de Currículo em PDF com Python

Este projeto foi desenvolvido para automatizar a criação de currículos profissionais em PDF utilizando a linguagem Python e a biblioteca ReportLab.

## 💡 O que o projeto faz

A aplicação gera um currículo formatado em PDF com base em dados fornecidos (nome, e-mail, telefone, resumo, experiências, formação e habilidades). É uma solução simples, direta e funcional para quem quer ter um currículo apresentável de forma automatizada.

## ⚙️ Tecnologias Utilizadas

- Python 3
- ReportLab (para geração de PDF)

## 🛠️ Como eu fiz

Comecei criando uma versão que interagia com o usuário via terminal, usando `input()`. No entanto, ao testar em ambientes que não suportam entrada interativa (como alguns notebooks e sandboxed environments), percebi a necessidade de adaptar o projeto. Assim, modifiquei o código para usar dados simulados diretamente no script — o que também facilita testes e demonstrações públicas.

## 📄 Exemplo de uso

Ao executar o script, um currículo PDF será gerado automaticamente com dados de exemplo. Você pode modificar o dicionário `data` para personalizar com suas próprias informações.

```bash
python curriculo_generator.py
