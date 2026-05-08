import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cinema.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tema TEXT NOT NULL,
            classificacao TEXT NOT NULL,
            duracao INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER NOT NULL UNIQUE,
            lotacao_max INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER NOT NULL,
            horario TEXT NOT NULL,
            filme_id INTEGER NOT NULL,
            publico INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (numero_sala) REFERENCES salas(numero_sala),
            FOREIGN KEY (filme_id) REFERENCES filmes(id)
        );
    """)

    conn.commit()
    conn.close()