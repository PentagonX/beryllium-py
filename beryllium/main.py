# main.py
from .lexer import lex
from .parser import Parser
from .ast_nodes import Program, Function, ExitStmt
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: beryll <file.by>")
        sys.exit(1)

    path = Path(sys.argv[1])
    code = path.read_text()

    tokens = list(lex(code))
    parser = Parser(tokens)
    ast = parser.parse()

    print("Parsed successfully!")
    print(ast)

if __name__ == "__main__":
    main()
