# 🎬 MAX Cinema — Sistema de Gerenciamento

Sistema de gerenciamento de cinema desenvolvido em Python, com interface via console e persistência em banco de dados SQLite.

---

## Descrição

O MAX Cinema permite o controle completo de filmes, salas e sessões de um cinema, oferecendo cadastro, edição, exclusão e geração de relatórios de ocupação, tudo por meio de menus interativos no terminal.

---

## Funcionalidades

- **Autenticação** — acesso protegido por login e senha
- **Gestão de Filmes** — cadastro com título, tema, classificação etária e duração
- **Gestão de Salas** — cadastro com número e lotação máxima
- **Gestão de Sessões** — vinculação de filme e sala com horário e público registrado
- **Relatório de Sessões** — visão consolidada com percentual de ocupação por sessão

---

## Estrutura do Projeto

```
src/
├── main.py                  # Ponto de entrada da aplicação
├── model/
│   └── model.py             # Conexão com SQLite e criação das tabelas
├── service/
│   └── service.py           # Regras de negócio e operações no banco
├── controller/
│   └── controller.py        # Orquestração entre view e service
└── view/
    └── view.py              # Menus, formulários e exibição no console
```

---

## Tecnologias

- Python 3.x
- SQLite3 (biblioteca padrão — sem dependências externas)

---

## Como Executar

```bash
cd src
python main.py
```

**Credenciais de acesso:**

| Campo  | Valor   |
|--------|---------|
| Login  | `admin` |
| Senha  | `admin` |

---

## Banco de Dados

O arquivo `cinema.db` é criado automaticamente na primeira execução, contendo as tabelas:

- `filmes` — dados dos filmes cadastrados
- `salas` — dados das salas disponíveis
- `sessoes` — sessões com referência a filme e sala
