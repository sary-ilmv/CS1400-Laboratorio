import ast
import pytest

def test_area_script():
    # Fix 1: Target the correct file name from your folder
    with open("2area.py", "r", encoding="utf-8") as f:
        student_code = f.read()

    tree = ast.parse(student_code)

    # 1. Check for 'import math'
    has_math_import = any(
        isinstance(node, ast.Import) and any(alias.name == "math" for alias in node.names)
        for node in ast.walk(tree)
    )
    assert has_math_import, "Falta importar la biblioteca 'math'."

    # 2. Check for variable 'radio_circulo'
    has_radio_variable = any(
        isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "radio_circulo" for t in node.targets
        )
        for node in ast.walk(tree)
    )
    assert has_radio_variable, "Debes definir la variable 'radio_circulo'."

    # 3. Check math.pi usage (checks both left and right sides of multiplication)
    uses_math_pi = any(
        isinstance(node, ast.Attribute) 
        and isinstance(node.value, ast.Name) 
        and node.value.id == "math" 
        and node.attr == "pi"
        for node in ast.walk(tree)
    )
    assert uses_math_pi, "Debes utilizar 'math.pi' para realizar el cálculo."

    # 4. Check print() function call
    has_print = any(
        isinstance(node, ast.Call) 
        and isinstance(node.func, ast.Name) 
        and node.func.id == "print"
        for node in ast.walk(tree)
    )
    assert has_print, "Debes utilizar la función 'print()' para mostrar el resultado."