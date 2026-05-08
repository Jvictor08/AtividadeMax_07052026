import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from model.model import init_db
from controller.controller import (
    fazer_login,
    controller_filmes,
    controller_salas,
    controller_sessoes,
    controller_relatorio,
)
import view.view as v
 
def main():
    init_db()
    fazer_login()
 
    while True:
        opcao = v.menu_principal()
 
        if opcao == "1":
            controller_filmes()
        elif opcao == "2":
            controller_salas()
        elif opcao == "3":
            controller_sessoes()
        elif opcao == "4":
            controller_relatorio()
        elif opcao == "0":
            v.limpar()
            print("\n  Até logo! 🎬\n")
            break
        else:
            v.msg_erro("Opção inválida.")
 
 
if __name__ == "__main__":
    main()