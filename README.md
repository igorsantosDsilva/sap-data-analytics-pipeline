# 📊 SAP Production Pipeline – Data Engineering Project

Pipeline de dados automatizado para ingestão, processamento e monitoramento de dados de produção a partir do SAP, com geração de snapshots horários e relatório visual.

---

## 🚀 Overview

Este projeto implementa um **pipeline de dados batch com execução horária**, responsável por extrair dados diretamente do SAP, processá-los e gerar indicadores de desempenho operacional.

O pipeline foi projetado considerando **restrições reais de ambiente corporativo**, como ausência de API, utilizando automação via SAP GUI.

---

## 🧠 Problem Statement

Em ambientes industriais, o acompanhamento da produção geralmente ocorre de forma manual ou com atraso, dificultando a tomada de decisão.

Este projeto resolve esse problema através de:

* Ingestão automatizada de dados do SAP
* Processamento incremental por hora
* Persistência de histórico acumulado
* Geração de métricas de produtividade em tempo quase real

---

## ⚙️ Pipeline Architecture
<img src='[ARCHITECTURE] sap-data-analytics-pipeline - ARCHITECTURE - sap-data-analytics-pipeline.jpg' alt='Arquitetura do Pipeline ETL'>

---

## 🔄 Data Pipeline Stages

### 🔹 1. Data Ingestion

Responsável por extrair os dados diretamente do SAP:

* Automação via `win32com` (SAP GUI Scripting)
* Controle de processo (start/stop SAP)
* Execução de transação SAP
* Exportação de dados em `.xls`

📌 Simula cenários reais onde não há acesso via API.

---

### 🔹 2. Data Processing

* Leitura de arquivos XLS
* Limpeza e padronização dos dados
* Agregações:

  * Produção finalizada
  * Insucesso
  * Ordens iniciadas

---

### 🔹 3. Incremental Snapshot

A cada execução:

* Geração de snapshot baseado na hora atual
* Estrutura:

```text
HORA | SUCESSO | INSUCESSO | INICIADAS
```

* Processamento restrito ao horário operacional (09h–17h)

---

### 🔹 4. Data Persistence

* Armazenamento em arquivo Excel (`relatorio_horario.xlsx`)
* Histórico incremental (append)
* Cálculo automático de métricas:

```text
META = crescimento linear
DIFERENÇA = META - PRODUÇÃO
```

---

### 🔹 5. Data Visualization

* Geração de relatório visual com `matplotlib`
* Renderização de tabela com:

  * Estilização
  * Destaque condicional (performance vs meta)
* Output em imagem (`.png`)

---

## 🗂 Project Structure

```bash
sap-production-pipeline/
│
├── config/
│   └── settings.py
│
├── datasets/
│   ├── zwm117.xls
│   └── relatorio_horario.xlsx
│
├── img/
│   ├── logo_empresa.png
│   └── relatorio_final.png
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── .env
└── README.md
```

---

## 🛠 Tech Stack

* **Python**
* **VBScript**
* **pandas**
* **matplotlib**
* **win32com (SAP GUI Automation)**
* **psutil**
* **openpyxl**

---

## 📊 Key Engineering Concepts

Este projeto demonstra na prática:

* Data Pipeline Design
* Batch Processing (Hourly)
* Data Ingestion from Legacy Systems
* Incremental Data Processing
* Data Persistence Strategy
* Automation of External Systems (SAP GUI)
* Separation of Concerns (extract / transform / load)

---

## ▶️ Execution

```bash
python main.py
```

* Agendar via **Windows Task Scheduler** para execução horária

---

## 📈 Output

* Dataset incremental de produção
* Métricas de performance operacional
* Relatório visual automatizado
* Base pronta para integração com sistemas de BI

---

<div align="center">

**Feito por [@Igor Santos](www.linkedin.com/in/igor-santos-50791a227) 😁**

</div>
