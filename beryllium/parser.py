from ast import Program, Function, ExitStmt

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected):
        token = self.current()
        if not token or token.type != expected:
            raise SyntaxError(
                f"Expected {expected}, got {token.type if token else 'EOF'}"
            )
        self.pos += 1
        return token

    def parse(self):
        functions = []
        while self.current():
            functions.append(self.parse_function())
        return Program(functions)

    def parse_function(self):
        self.eat("FUNC")
        name = self.eat("IDENT").value
        self.eat("LPAREN")
        self.eat("RPAREN")
        self.eat("LBRACE")

        body = []
        while self.current().type != "RBRACE":
            body.append(self.parse_statement())

        self.eat("RBRACE")
        return Function(name, body)

    def parse_statement(self):
        token = self.current()

        if token.type == "EXIT":
            self.eat("EXIT")
            code = int(self.eat("NUMBER").value)
            self.eat("SEMI")
            return ExitStmt(code)

        raise SyntaxError(f"Unknown statement at {token.line}:{token.col}")
