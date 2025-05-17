# 🔍 Consulta de CNPJ com Python

Este projeto é um sistema simples em Python que permite consultar **informações públicas de empresas brasileiras** através do número do CNPJ, utilizando a API gratuita [CNPJ.ws](https://publica.cnpj.ws).

## 🚀 O que o sistema faz

Ao digitar um CNPJ válido, o sistema retorna no terminal:
- ✅ **Razão Social** da empresa
- 🏢 **Atividade principal**
- 📌 **Atividades secundárias** (se existirem)

---

## ⚠️ Aviso

Os dados consultados são **públicos** e obtidos via **API gratuita**.  
Nenhuma informação sensível é coletada, armazenada ou compartilhada.

API oficial: [https://publica.cnpj.ws](https://publica.cnpj.ws)

---

## 🛠 Tecnologias Utilizadas

- 🐍 **Python** – linguagem principal do sistema  
- 🔗 **requests** – biblioteca para realizar as requisições HTTP  
- 📄 **pprint** – utilizada para imprimir os dados de forma organizada no terminal  
- 🌐 **API pública CNPJ.ws** – fonte oficial dos dados consultados  

---

## 📎 Exemplo de uso

```bash
python cnpj_consulta.py
