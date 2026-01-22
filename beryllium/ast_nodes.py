from dataclasses import dataclass

@dataclass
class Program:
    functions: list

@dataclass
class Function:
    name: str
    body: list

@dataclass
class ExitStmt:
    code: int
