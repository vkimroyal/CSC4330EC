import re


# Lexical Analyzer
def isVar(str):
    return re.search("[a-z]|[A-Z]|_{6,8}", str)


class Lexical:
    def __init__(self, str):
        self.str = str

    # Print message for Lexical Error
    def error(self):
        print("Lexical Error.")
        exit()

    # Check Lexemes
    def checkLex(self):
        lexemes = []

        # Start --> Init
        for lex in self.str:
            if lex == "init":
                lexemes.append('INIT')
            elif lex == "during":
                lexemes.append('DRNG')
            elif lex == "exec":
                lexemes.append('EXEC')
            elif lex == "given":
                lexemes.append("GIVN")
            elif lex == "ifnot":
                lexemes.append("IFNO")
            elif lex == "term":
                lexemes.append("TERM")
            elif lex == "snum":
                lexemes.append("SNUM")
            elif lex == "inum":
                lexemes.append("INUM")
            elif lex == "lnum":
                lexemes.append("LNUM")
            elif lex == "+":
                lexemes.append("PLUS")
            elif lex == "-":
                lexemes.append("MNUS")
            elif lex == "*":
                lexemes.append("MULT")
            elif lex == "/":
                lexemes.append("DIVS")
            elif lex == "(":
                lexemes.append("STRP")
            elif lex == ")":
                lexemes.append("ENDP")
            elif lex == "=":
                lexemes.append("SIGN")
            elif lex == "<":
                lexemes.append("LESS")
            elif lex == ">":
                lexemes.append("MORE")
            elif lex == "<=":
                lexemes.append("LEEQ")
            elif lex == ">=":
                lexemes.append("MOEQ")
            elif lex == ":=":
                lexemes.append("EQTO")
            elif lex == "/=":
                lexemes.append("NOEQ")
            elif lex == "and":
                lexemes.append("AND")
            elif lex == "or":
                lexemes.append("OR")
            elif lex == ":":
                lexemes.append("BLKS")
            elif lex == ";":
                lexemes.append("BLKE")
            elif lex == "{":
                lexemes.append("BRKS")
            elif lex == "}":
                lexemes.append("BRKE")
            elif lex.isnumeric():
                lexemes.append('int')
            elif isVar(lex):
                lexemes.append('id')
            else:
                self.error()

        return lexemes
