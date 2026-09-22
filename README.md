# 🧮 Algoritmo de Quine-McCluskey

> Uma ferramenta computacional para minimização exata de funções booleanas.

[![Acessar Aplicação Web](https://img.shields.io/badge/Acessar-Aplicação_Web-blue?style=for-the-badge&logo=vercel)](https://quine-mccluskey.vercel.app/)

> **Aviso sobre o primeiro acesso:** O carregamento inicial da aplicação web pode demorar alguns segundos a mais. Isso ocorre porque a hospedagem suspende a aplicação após um período de inatividade. O primeiro clique liga o servidor, mas as execuções seguintes ocorrem em tempo real.

Implementação do Algoritmo de Quine-McCluskey em Python para encontrar a versão mínima de funções booleanas a partir de seus mintermos. Este projeto foi desenvolvido para resolver o problema da escalabilidade: enquanto os Mapas de Karnaugh são excelentes para até 4 variáveis, eles se tornam inviáveis e suscetíveis a erros humanos para números maiores de variáveis. 

O projeto é especialmente útil para estudantes de **Sistemas Digitais da Universidade de Brasília (UnB)** e entusiastas de eletrônica digital que precisam projetar ou conferir circuitos lógicos combinacionais complexos.

---

## ✨ Funcionalidades

- **Minimização Automatizada:** Calcula os implicantes primos e os implicantes primos essenciais para gerar a expressão lógica mínima (Soma de Produtos).
- **Escalabilidade:** Lida facilmente com funções que possuem um número grande de variáveis.
- **Interface Web:** Conta com uma aplicação interativa e acessível via navegador para facilitar os estudos teóricos e práticos.

## 🛠️ Tecnologias Utilizadas

- **Python:** Implementação do motor principal do algoritmo de minimização algébrica.
- **Next.js / React:** Tecnologias base para a construção da interface de usuário da versão web.
- **Vercel:** Hospedagem da aplicação online.

## 🚀 Como executar localmente (Python)

Se você deseja rodar o algoritmo diretamente no seu terminal ou integrá-lo em outros scripts Python:

### Pré-requisitos
- Python 3.x instalado.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/markvncs/mccluskey-api.git
