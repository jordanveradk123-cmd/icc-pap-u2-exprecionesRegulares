def main():

    def runEjemplo1():
     import re
     patron = r"ab*"
     palabras = ["a", "ab", "abbb", "abab", "b", ""]

     for p in palabras:
      print(f"{p} -> {bool(re.fullmatch(patron, p))}")

    
    def runEjemplo2():
     import re
     regex = r"[T|O][0-9]{3}"
     lista = ["T001", "O120", "T01", "X001", "T0001"]

     for string in lista:
      # En Java .matches() es igual a fullmatch() en Python, no a match()
      resultado = bool(re.fullmatch(regex, string))
      print(f"{string} => {resultado}")
  
    def runEjemplo3():
     import re
     texto = "Sensores: T001 reporta 23,5 C; O001 reporta 12 PERSONAS; T002 reporta -2 C."
     patron = re.compile(r"[TO][0-9]{3}")

     for matcher in patron.finditer(texto):
      print(f"Encontrado: {matcher.group()}, posición: {matcher.start()}")


    if __name__ == "_main_":
        main()
