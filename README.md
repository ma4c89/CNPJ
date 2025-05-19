# 🔍 Consulta de CNPJ - Python + CustomTkinter

Este projeto é uma aplicação desktop que permite a consulta de informações públicas de empresas brasileiras a partir do CNPJ, utilizando a [API pública do CNPJ.ws](https://publica.cnpj.ws/) com uma interface moderna desenvolvida em **CustomTkinter**.

---

## 🖼️ Interface
- Desenvolvida com **CustomTkinter** (baseada no Tkinter, com estilo moderno).
- Layout limpo, responsivo e amigável.
- Resultados organizados e fáceis de ler.

---

## ⚙️ Funcionalidades

- ✅ Entrada do CNPJ (com ou sem pontuação).
- ✅ Validação automática do formato do CNPJ.
- ✅ Consulta à API pública [cnpj.ws](https://publica.cnpj.ws).
- ✅ Exibe:
  - Razão Social
  - Atividade principal
  - Lista de atividades secundárias
- ✅ Contador de consultas e interações com o sistema.
- ✅ Mensagens informativas e feedback visual.
- ✅ Uso de **multithreading** para evitar travamentos na interface.

---

## 📦 Requisitos

- Python 3.7 ou superior
- Bibliotecas:
  ```bash
  pip install customtkinter requests
