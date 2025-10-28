from flask import Flask
from teste import app

import json
from datetime import datetime

# Arquivo onde os dados serão salvos
ARQUIVO = "historico_financeiro.json"

# Carrega dados existentes (ou cria lista vazia)
try:
    with open(ARQUIVO, "r") as f:
        historico = json.load(f)
except FileNotFoundError:
    historico = []

def salvar():
    with open(ARQUIVO, "w") as f:
        json.dump(historico, f, indent=4)

def adicionar_movimento(tipo):
    descricao = input("Descrição: ")
    valor = float(input("Valor (R$): "))
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    movimento = {
        "data": data,
        "descricao": descricao,
        "tipo": tipo,
        "valor": valor
    }
    historico.append(movimento)
    salvar()
    print("Movimento adicionado com sucesso!\n")

def mostrar_historico():
    print("\n=== HISTÓRICO FINANCEIRO ===")
    for item in historico:
        sinal = "+" if item["tipo"] == "entrada" else "-"
        print(f"[{item['data']}] {sinal} R${item['valor']:.2f} - {item['descricao']}")
    print("============================\n")

def calcular_saldo():
    saldo = 0
    for item in historico:
        if item["tipo"] == "entrada":
            saldo += item["valor"]
        else:
            saldo -= item["valor"]
    print(f"💰 Saldo atual: R${saldo:.2f}\n")

while True:
    print("1. Adicionar entrada")
    print("2. Adicionar saída")
    print("3. Ver histórico")
    print("4. Ver saldo")
    print("5. Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_movimento("entrada")
    elif opcao == "2":
        adicionar_movimento("saida")
    elif opcao == "3":
        mostrar_historico()
    elif opcao == "4":
        calcular_saldo()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
