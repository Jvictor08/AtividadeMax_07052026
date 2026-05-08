import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from model.model import get_connection

# ─── FILMES ───────────────────────────────────────────────────────────────────

class FilmeService:

    @staticmethod
    def listar():
        conn = get_connection()
        rows = conn.execute("SELECT * FROM filmes ORDER BY id").fetchall()
        conn.close()
        return rows

    @staticmethod
    def buscar_por_id(filme_id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM filmes WHERE id = ?", (filme_id,)).fetchone()
        conn.close()
        return row

    @staticmethod
    def criar(titulo, tema, classificacao, duracao):
        conn = get_connection()
        conn.execute(
            "INSERT INTO filmes (titulo, tema, classificacao, duracao) VALUES (?, ?, ?, ?)",
            (titulo, tema, classificacao, duracao)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(filme_id, titulo, tema, classificacao, duracao):
        conn = get_connection()
        conn.execute(
            "UPDATE filmes SET titulo=?, tema=?, classificacao=?, duracao=? WHERE id=?",
            (titulo, tema, classificacao, duracao, filme_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(filme_id):
        conn = get_connection()
        conn.execute("DELETE FROM filmes WHERE id = ?", (filme_id,))
        conn.commit()
        conn.close()


# ─── SALAS ────────────────────────────────────────────────────────────────────

class SalaService:

    @staticmethod
    def listar():
        conn = get_connection()
        rows = conn.execute("SELECT * FROM salas ORDER BY numero_sala").fetchall()
        conn.close()
        return rows

    @staticmethod
    def buscar_por_numero(numero_sala):
        conn = get_connection()
        row = conn.execute("SELECT * FROM salas WHERE numero_sala = ?", (numero_sala,)).fetchone()
        conn.close()
        return row

    @staticmethod
    def criar(numero_sala, lotacao_max):
        conn = get_connection()
        conn.execute(
            "INSERT INTO salas (numero_sala, lotacao_max) VALUES (?, ?)",
            (numero_sala, lotacao_max)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(numero_sala, lotacao_max):
        conn = get_connection()
        conn.execute(
            "UPDATE salas SET lotacao_max=? WHERE numero_sala=?",
            (lotacao_max, numero_sala)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(numero_sala):
        conn = get_connection()
        conn.execute("DELETE FROM salas WHERE numero_sala = ?", (numero_sala,))
        conn.commit()
        conn.close()


# ─── SESSÕES ──────────────────────────────────────────────────────────────────

class SessaoService:

    @staticmethod
    def listar():
        conn = get_connection()
        rows = conn.execute("""
            SELECT s.id, s.numero_sala, s.horario, f.titulo AS filme, s.publico
            FROM sessoes s
            JOIN filmes f ON s.filme_id = f.id
            ORDER BY s.id
        """).fetchall()
        conn.close()
        return rows

    @staticmethod
    def buscar_por_id(sessao_id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM sessoes WHERE id = ?", (sessao_id,)).fetchone()
        conn.close()
        return row

    @staticmethod
    def criar(numero_sala, horario, filme_id, publico):
        conn = get_connection()
        conn.execute(
            "INSERT INTO sessoes (numero_sala, horario, filme_id, publico) VALUES (?, ?, ?, ?)",
            (numero_sala, horario, filme_id, publico)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(sessao_id, numero_sala, horario, filme_id, publico):
        conn = get_connection()
        conn.execute(
            "UPDATE sessoes SET numero_sala=?, horario=?, filme_id=?, publico=? WHERE id=?",
            (numero_sala, horario, filme_id, publico, sessao_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(sessao_id):
        conn = get_connection()
        conn.execute("DELETE FROM sessoes WHERE id = ?", (sessao_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def relatorio():
        conn = get_connection()
        rows = conn.execute("""
            SELECT
                s.id,
                s.horario,
                s.numero_sala,
                sal.lotacao_max,
                f.titulo AS filme,
                f.classificacao,
                f.duracao,
                s.publico,
                ROUND(s.publico * 100.0 / sal.lotacao_max, 1) AS ocupacao_pct
            FROM sessoes s
            JOIN filmes f ON s.filme_id = f.id
            JOIN salas sal ON s.numero_sala = sal.numero_sala
            ORDER BY s.horario
        """).fetchall()
        conn.close()
        return rows