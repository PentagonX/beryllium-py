import re
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str
    line: int
    col: int


TOKEN_SPEC = [
    ("FUNC",    r"func\b"),
    ("EXIT",    r"exit\b"),
    ("NUMBER",  r"\d+"),
    ("IDENT",   r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("LPAREN",  r"\("),
    ("RPAREN",  r"\)"),
    ("LBRACE",  r"\{"),
    ("RBRACE",  r"\}"),
    ("SEMI",    r";"),
    ("SKIP",    r"[ \t]+"),
    ("NEWLINE", r"\n"),
    ("MISMATCH", r"."),
]

MASTER_REGEX = "|".join(
    f"(?P<{name}>{regex})" for name, regex in TOKEN_SPEC
)

def lex(code: str):
    line = 1
    col = 1

    for match in re.finditer(MASTER_REGEX, code):
        kind = match.lastgroup
        value = match.group()

        if kind == "NEWLINE":
            line += 1
            col = 1
            continue

        if kind == "SKIP":
            col += len(value)
            continue

        if kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character {value!r} at {line}:{col}")

        yield Token(kind, value, line, col)
        col += len(value)
