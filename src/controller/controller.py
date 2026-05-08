import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from service.service import FilmeService, SalaService, SessaoService
import view.view as v


# ─── AUTH ─────────────────────────────────────────────────────────────────────

def fazer_login():
    while True:
        usuario, senha = v.tela_login()
        if usuario == "admin" and senha == "admin":
            return True
        v.msg_login_erro()


# ─── FILMES ───────────────────────────────────────────────────────────────────

def controller_filmes():
    while True:
        opcao = v.menu_crud("Filmes")

        if opcao == "1":
            filmes = FilmeService.listar()
            v.exibir_filmes(filmes)

        elif opcao == "2":
            v.cabecalho("Cadastrar Filme")
            titulo, tema, classificacao, duracao = v.form_filme()
            FilmeService.criar(titulo, tema, classificacao, duracao)
            v.msg_sucesso("Filme cadastrado com sucesso!")

        elif opcao == "3":
            filmes = FilmeService.listar()
            v.exibir_filmes(filmes)
            if not filmes:
                continue
            filme_id = v.pedir_id_filme()
            filme = FilmeService.buscar_por_id(filme_id)
            if not filme:
                v.msg_erro("Filme não encontrado.")
                continue
            v.cabecalho("Editar Filme")
            titulo, tema, classificacao, duracao = v.form_filme(
                filme["titulo"], filme["tema"], filme["classificacao"], filme["duracao"]
            )
            FilmeService.atualizar(filme_id, titulo, tema, classificacao, duracao)
            v.msg_sucesso("Filme atualizado com sucesso!")

        elif opcao == "4":
            filmes = FilmeService.listar()
            v.exibir_filmes(filmes)
            if not filmes:
                continue
            filme_id = v.pedir_id_filme()
            filme = FilmeService.buscar_por_id(filme_id)
            if not filme:
                v.msg_erro("Filme não encontrado.")
                continue
            FilmeService.deletar(filme_id)
            v.msg_sucesso("Filme excluído com sucesso!")

        elif opcao == "0":
            break
        else:
            v.msg_erro("Opção inválida.")


# ─── SALAS ────────────────────────────────────────────────────────────────────

def controller_salas():
    while True:
        opcao = v.menu_crud("Salas")

        if opcao == "1":
            salas = SalaService.listar()
            v.exibir_salas(salas)

        elif opcao == "2":
            v.cabecalho("Cadastrar Sala")
            numero_sala, lotacao_max = v.form_sala()
            if SalaService.buscar_por_numero(numero_sala):
                v.msg_erro(f"Sala {numero_sala} já cadastrada.")
                continue
            SalaService.criar(numero_sala, lotacao_max)
            v.msg_sucesso("Sala cadastrada com sucesso!")

        elif opcao == "3":
            salas = SalaService.listar()
            v.exibir_salas(salas)
            if not salas:
                continue
            numero_sala = v.pedir_numero_sala()
            sala = SalaService.buscar_por_numero(numero_sala)
            if not sala:
                v.msg_erro("Sala não encontrada.")
                continue
            v.cabecalho("Editar Sala")
            _, lotacao_max = v.form_sala(sala["numero_sala"], sala["lotacao_max"])
            SalaService.atualizar(numero_sala, lotacao_max)
            v.msg_sucesso("Sala atualizada com sucesso!")

        elif opcao == "4":
            salas = SalaService.listar()
            v.exibir_salas(salas)
            if not salas:
                continue
            numero_sala = v.pedir_numero_sala()
            sala = SalaService.buscar_por_numero(numero_sala)
            if not sala:
                v.msg_erro("Sala não encontrada.")
                continue
            SalaService.deletar(numero_sala)
            v.msg_sucesso("Sala excluída com sucesso!")

        elif opcao == "0":
            break
        else:
            v.msg_erro("Opção inválida.")


# ─── SESSÕES ──────────────────────────────────────────────────────────────────

def controller_sessoes():
    while True:
        opcao = v.menu_crud("Sessões")

        if opcao == "1":
            sessoes = SessaoService.listar()
            v.exibir_sessoes(sessoes)

        elif opcao == "2":
            filmes = FilmeService.listar()
            if not filmes:
                v.msg_erro("Cadastre pelo menos um filme antes.")
                continue
            salas = SalaService.listar()
            if not salas:
                v.msg_erro("Cadastre pelo menos uma sala antes.")
                continue
            v.cabecalho("Cadastrar Sessão")
            numero_sala, horario, filme_id, publico = v.form_sessao(filmes)
            if not SalaService.buscar_por_numero(numero_sala):
                v.msg_erro(f"Sala {numero_sala} não encontrada.")
                continue
            SessaoService.criar(numero_sala, horario, filme_id, publico)
            v.msg_sucesso("Sessão cadastrada com sucesso!")

        elif opcao == "3":
            sessoes = SessaoService.listar()
            v.exibir_sessoes(sessoes)
            if not sessoes:
                continue
            filmes = FilmeService.listar()
            sessao_id = v.pedir_id_sessao()
            sessao = SessaoService.buscar_por_id(sessao_id)
            if not sessao:
                v.msg_erro("Sessão não encontrada.")
                continue
            v.cabecalho("Editar Sessão")
            numero_sala, horario, filme_id, publico = v.form_sessao(
                filmes,
                sessao["numero_sala"], sessao["horario"],
                sessao["filme_id"], sessao["publico"]
            )
            if not SalaService.buscar_por_numero(numero_sala):
                v.msg_erro(f"Sala {numero_sala} não encontrada.")
                continue
            SessaoService.atualizar(sessao_id, numero_sala, horario, filme_id, publico)
            v.msg_sucesso("Sessão atualizada com sucesso!")

        elif opcao == "4":
            sessoes = SessaoService.listar()
            v.exibir_sessoes(sessoes)
            if not sessoes:
                continue
            sessao_id = v.pedir_id_sessao()
            sessao = SessaoService.buscar_por_id(sessao_id)
            if not sessao:
                v.msg_erro("Sessão não encontrada.")
                continue
            SessaoService.deletar(sessao_id)
            v.msg_sucesso("Sessão excluída com sucesso!")

        elif opcao == "0":
            break
        else:
            v.msg_erro("Opção inválida.")


# ─── RELATÓRIO ────────────────────────────────────────────────────────────────

def controller_relatorio():
    dados = SessaoService.relatorio()
    v.exibir_relatorio(dados)