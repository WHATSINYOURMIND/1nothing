import types
print("check if a given value is compiled code or not")
code = compile("print('Hello')", "sample", "exec")
print(isinstance(code,types.CodeType))
print(isinstance(('fun'), types.CodeType))
print("\nCheck if a given value is a module:")
print(isinstance(types, types.ModuleType))
