import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def cabecalho(titulo):
    print("\n" + "═" * 50)
    print(f"  🎬  {titulo}")
    print("═" * 50)


def pausar():
    input("\n  [Enter para continuar]")


def pedir(prompt, obrigatorio=True):
    while True:
        valor = input(f"  {prompt}: ").strip()
        if valor or not obrigatorio:
            return valor
        print("  ⚠  Campo obrigatório.")


def pedir_inteiro(prompt, minimo=None, maximo=None):
    while True:
        try:
            valor = int(pedir(prompt))
            if minimo is not None and valor < minimo:
                print(f"  ⚠  Valor mínimo: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠  Valor máximo: {maximo}")
                continue
            return valor
        except ValueError:
            print("  ⚠  Digite um número inteiro.")


# ─── LOGIN ────────────────────────────────────────────────────────────────────

def tela_login():
    limpar()
    cabecalho("Sistema de Cinema — Login")
    usuario = pedir("Usuário")
    senha   = pedir("Senha")
    return usuario, senha


def msg_login_erro():
    print("\n  ❌  Usuário ou senha incorretos.\n")
    pausar()


# ─── MENU PRINCIPAL ───────────────────────────────────────────────────────────

def menu_principal():
    limpar()
    cabecalho("Menu Principal")
    print("  1. Filmes")
    print("  2. Salas")
    print("  3. Sessões")
    print("  4. Relatório de Sessões")
    print("  0. Sair")
    print()
    return pedir("Opção")


# ─── MENU GENÉRICO DE CRUD ────────────────────────────────────────────────────

def menu_crud(entidade):
    limpar()
    cabecalho(f"Gerenciar {entidade}")
    print("  1. Listar")
    print("  2. Cadastrar")
    print("  3. Editar")
    print("  4. Excluir")
    print("  0. Voltar")
    print()
    return pedir("Opção")


# ─── FILMES ───────────────────────────────────────────────────────────────────

def exibir_filmes(filmes):
    limpar()
    cabecalho("Filmes Cadastrados")
    if not filmes:
        print("  Nenhum filme cadastrado.")
    else:
        print(f"  {'ID':<5} {'Título':<28} {'Tema':<15} {'Class.':<8} {'Dur.(min)'}")
        print("  " + "-" * 65)
        for f in filmes:
            print(f"  {f['id']:<5} {f['titulo']:<28} {f['tema']:<15} {f['classificacao']:<8} {f['duracao']}")
    pausar()


def form_filme(titulo="", tema="", classificacao="", duracao=""):
    print()
    novo_titulo        = pedir(f"Título [{titulo}]", obrigatorio=not titulo) or titulo
    novo_tema          = pedir(f"Tema [{tema}]", obrigatorio=not tema) or tema
    novo_classificacao = pedir(f"Classificação (L/10/12/14/16/18) [{classificacao}]", obrigatorio=not classificacao) or classificacao
    novo_duracao       = pedir_inteiro(f"Duração em minutos [{duracao}]", minimo=1) if not duracao else (
        pedir(f"Duração em minutos [{duracao}]", obrigatorio=False) or duracao
    )
    return novo_titulo, novo_tema, novo_classificacao, int(novo_duracao)


def pedir_id_filme():
    return pedir_inteiro("ID do Filme", minimo=1)


# ─── SALAS ────────────────────────────────────────────────────────────────────

def exibir_salas(salas):
    limpar()
    cabecalho("Salas Cadastradas")
    if not salas:
        print("  Nenhuma sala cadastrada.")
    else:
        print(f"  {'Nº Sala':<10} {'Lotação Máx.'}")
        print("  " + "-" * 25)
        for s in salas:
            print(f"  {s['numero_sala']:<10} {s['lotacao_max']}")
    pausar()


def form_sala(numero_sala="", lotacao_max=""):
    print()
    num  = pedir_inteiro(f"Número da sala [{numero_sala}]", minimo=1) if not numero_sala else (
        int(pedir(f"Número da sala [{numero_sala}]", obrigatorio=False) or numero_sala)
    )
    lot  = pedir_inteiro(f"Lotação máxima [{lotacao_max}]", minimo=1) if not lotacao_max else (
        int(pedir(f"Lotação máxima [{lotacao_max}]", obrigatorio=False) or lotacao_max)
    )
    return int(num), int(lot)


def pedir_numero_sala():
    return pedir_inteiro("Número da Sala", minimo=1)


# ─── SESSÕES ──────────────────────────────────────────────────────────────────

def exibir_sessoes(sessoes):
    limpar()
    cabecalho("Sessões Cadastradas")
    if not sessoes:
        print("  Nenhuma sessão cadastrada.")
    else:
        print(f"  {'ID':<5} {'Sala':<6} {'Horário':<18} {'Filme':<28} {'Público'}")
        print("  " + "-" * 65)
        for s in sessoes:
            print(f"  {s['id']:<5} {s['numero_sala']:<6} {s['horario']:<18} {s['filme']:<28} {s['publico']}")
    pausar()


def form_sessao(filmes, numero_sala="", horario="", filme_id="", publico=""):
    print()
    print("  Filmes disponíveis:")
    for f in filmes:
        print(f"    [{f['id']}] {f['titulo']}")
    print()
    num_sala  = pedir_inteiro(f"Número da sala [{numero_sala}]", minimo=1) if not numero_sala else (
        int(pedir(f"Número da sala [{numero_sala}]", obrigatorio=False) or numero_sala)
    )
    hor       = pedir(f"Horário (ex: 2025-06-01 20:00) [{horario}]", obrigatorio=not horario) or horario
    ids_validos = [f['id'] for f in filmes]
    while True:
        fid = pedir_inteiro(f"ID do Filme [{filme_id}]", minimo=1)
        if fid in ids_validos:
            break
        print("  ⚠  Filme não encontrado.")
    pub = pedir_inteiro(f"Público [{publico}]", minimo=0) if not publico else (
        int(pedir(f"Público [{publico}]", obrigatorio=False) or publico)
    )
    return int(num_sala), hor, fid, int(pub)


def pedir_id_sessao():
    return pedir_inteiro("ID da Sessão", minimo=1)


# ─── RELATÓRIO ────────────────────────────────────────────────────────────────

def exibir_relatorio(dados):
    limpar()
    cabecalho("Relatório de Sessões")
    if not dados:
        print("  Nenhuma sessão cadastrada.")
        pausar()
        return

    total_publico   = sum(r['publico'] for r in dados)
    total_capacidade = sum(r['lotacao_max'] for r in dados)
    ocupacao_geral  = round(total_publico * 100.0 / total_capacidade, 1) if total_capacidade else 0

    print(f"  {'ID':<5} {'Horário':<18} {'Sala':<6} {'Lotação':<9} {'Filme':<22} {'Class.':<7} {'Dur.':<6} {'Público':<9} {'Ocup.%'}")
    print("  " + "-" * 90)
    for r in dados:
        print(
            f"  {r['id']:<5} {r['horario']:<18} {r['numero_sala']:<6} "
            f"{r['lotacao_max']:<9} {r['filme']:<22} {r['classificacao']:<7} "
            f"{r['duracao']:<6} {r['publico']:<9} {r['ocupacao_pct']}%"
        )

    print("  " + "-" * 90)
    print(f"\n  Total de sessões  : {len(dados)}")
    print(f"  Total de público  : {total_publico}")
    print(f"  Ocupação geral    : {ocupacao_geral}%")
    pausar()


# ─── MENSAGENS GENÉRICAS ──────────────────────────────────────────────────────

def msg_sucesso(texto):
    print(f"\n  ✅  {texto}")
    pausar()


def msg_erro(texto):
    print(f"\n  ❌  {texto}")
    pausar()