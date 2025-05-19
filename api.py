import customtkinter
import requests
import threading
import re

contador_consultas = 0
contador_interacoes = 0

def limpar_cnpj(cnpj):
    return re.sub(r"[^\d]", "", cnpj)

def cnpj_valido(cnpj):
    return cnpj.isdigit() and len(cnpj) == 14

def consultar_cnpj():
    global contador_consultas

    resultado.configure(state="normal")
    resultado.delete("0.0", "end")
    resultado.insert("0.0", "🔄 Consultando... Aguarde.")
    resultado.configure(state="disabled")

    def tarefa():
        global contador_consultas
        cnpj_raw = campo_cnpj.get().strip()
        cnpj = limpar_cnpj(cnpj_raw)

        if not cnpj_valido(cnpj):
            atualizar_resultado("⚠️ Digite um CNPJ válido com 14 números.")
            return

        url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

        try:
            resposta = requests.get(url)
            dados = resposta.json()

            razao_social = dados.get("razao_social", "Não disponível")
            atividade_principal = dados["estabelecimento"]["atividade_principal"]["descricao"]
            atividades_secundarias = dados["estabelecimento"].get("atividades_secundarias", [])

            texto = f"🏢 Razão Social:\n{razao_social}\n\n"
            texto += f"💼 Atividade Principal:\n{atividade_principal}\n\n"
            texto += "📋 Atividades Secundárias:\n"

            if atividades_secundarias:
                for i, atividade in enumerate(atividades_secundarias, 1):
                    texto += f"  {i}. {atividade['descricao']}\n"
            else:
                texto += "  Nenhuma cadastrada."

            atualizar_resultado(texto)
            contador_consultas += 1
        except Exception as e:
            atualizar_resultado(f"❌ Erro ao consultar o CNPJ:\n{e}")

    threading.Thread(target=tarefa).start()

def atualizar_resultado(texto):
    resultado.configure(state="normal")
    resultado.delete("0.0", "end")
    resultado.insert("0.0", texto)
    resultado.configure(state="disabled")

def ao_fechar():
    print(f"[INFO] Total de consultas: {contador_consultas}")
    print(f"[INFO] Interações registradas: {contador_interacoes}")
    janela.destroy()

def registrar_interacao(event=None):
    global contador_interacoes
    contador_interacoes += 1

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("640x520")
janela.title("🔎 Consulta de CNPJ")
janela.resizable(False, False)
janela.protocol("WM_DELETE_WINDOW", ao_fechar)

titulo = customtkinter.CTkLabel(janela, text="Consulta de CNPJ", font=("Arial", 26, "bold"))
titulo.pack(pady=25)

campo_cnpj = customtkinter.CTkEntry(janela, placeholder_text="Digite o CNPJ (com ou sem pontuação)", font=("Arial", 14))
campo_cnpj.pack(pady=10, padx=20, fill="x")
campo_cnpj.bind("<FocusIn>", registrar_interacao)

botao_consultar = customtkinter.CTkButton(janela, text="🔍 Consultar", command=consultar_cnpj, font=("Arial", 14), cursor="hand2")
botao_consultar.pack(pady=10)
botao_consultar.bind("<Button-1>", registrar_interacao)

resultado = customtkinter.CTkTextbox(janela, height=260, font=("Courier New", 13))
resultado.pack(pady=20, padx=20, fill="both", expand=True)
resultado.configure(state="disabled")

janela.mainloop()
