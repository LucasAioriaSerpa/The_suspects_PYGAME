#imports
import ttg as ttg

class ex():
    def __init__(self, ex:int):
        self.ex = ex
    def do_ex(self):
        print(f"exercicio: {self.ex}")
        match self.ex:
            case 1:
                """TODO: Se o professor não se atrasar, a aula começara na hora certa.
                logo, se os alunos e o professor não se atrasarem, a aula começara na hora certa
                """
                vars_ttg = {
                    "Professor se atrasa":"p",
                    "Aula começa na hora certa":"q",
                    "Alunos se atrasam":"r"
                }
                x = ttg.Truths([vars_ttg["Professor se atrasa"],vars_ttg["Aula começa na hora certa"],vars_ttg["Alunos se atrasam"]],
                                ["((~p => q) and (~p and ~r)) => q"],ints=False)
                print(f'{x}\n{x.valuation()}\n\n')
            case 2:
                """TODO: p: joão esteve aqui || q: pedro esteve aqui || r: o quadro negro estareia cheio de poesias
                        (p and q) and (p => r) and (~r) => q"""
                x = ttg.Truths(['p','q','r'],['(p and q) and (p => r) and (~r) => q'],ints=False)
                print(f"{x}\n{x.valuation()}\n\n")
if __name__ == "__main__":
    ex(int(input("Digite um exercicio!\n→ "))).do_ex()
