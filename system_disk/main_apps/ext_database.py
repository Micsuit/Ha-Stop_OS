"""
This extension script will identify the extension of 
the file and return the correct program to open it.
"""

NOTEPAD = "notepad"
HXVW = "hxvw"


all_ext = {".txt": NOTEPAD, ".py": NOTEPAD, ".ini": NOTEPAD, ".log": NOTEPAD, ".c": NOTEPAD, ".cpp": NOTEPAD, 
           ".cs": NOTEPAD, ".hx": HXVW, ".README": NOTEPAD, ".md": NOTEPAD, ".html": NOTEPAD, ".bat": NOTEPAD,
           ".xml": NOTEPAD, ".pyc": HXVW, ".h": NOTEPAD, ".json": NOTEPAD, ".sh": NOTEPAD, ".yml": NOTEPAD,
           ".t3s": NOTEPAD, ".hpp": NOTEPAD, ".gitignore": NOTEPAD, ".cg": NOTEPAD, ".f":NOTEPAD, ".m": NOTEPAD,
           ".asm": NOTEPAD, ".au3": NOTEPAD, ".ABAP": NOTEPAD, ".bas": NOTEPAD, ".bf": NOTEPAD, ".cl": NOTEPAD,
           ".cljx": NOTEPAD, ".cob": NOTEPAD, ".coffee": NOTEPAD, ".cr": NOTEPAD, ".d": NOTEPAD, ".dart": NOTEPAD,
           ".delphi": NOTEPAD, ".erl": NOTEPAD, ".exs": NOTEPAD, ".go": NOTEPAD, ".groovy": NOTEPAD, ".hs": NOTEPAD,
           ".i": NOTEPAD, ".java": NOTEPAD, ".jl": NOTEPAD, ".jrl": NOTEPAD, ".js": NOTEPAD, ".kt": NOTEPAD,
           ".lisp": NOTEPAD, ".lua": NOTEPAD, ".ml": NOTEPAD, ".nim": NOTEPAD, "p6": NOTEPAD, ".pas": NOTEPAD,
           ".php": NOTEPAD, ".pl": NOTEPAD, ".pro": NOTEPAD, ".ps": NOTEPAD, ".ps1": NOTEPAD, ".r": NOTEPAD, 
           ".rb": NOTEPAD, ".rs": NOTEPAD, ".scala": NOTEPAD, ".sml": NOTEPAD, ".sol": NOTEPAD, ".spl": NOTEPAD,
           ".sql": NOTEPAD, ".swift": NOTEPAD, ".tcl": NOTEPAD, ".ts": NOTEPAD, ".vb": NOTEPAD, ".ws": NOTEPAD}


def load_ext(ext) -> str:
    return all_ext[ext] if ext in all_ext else None
    