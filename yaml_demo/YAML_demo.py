import yaml

# Безопасное чтение
#print("=== Безопасное чтение (safe_load) ===")
#with open('yaml_demo/ya.yaml', 'r') as file:
#    safe_data = yaml.safe_load(file)
#    print(safe_data)

print("\n=== Обычное чтение (load) ===")
with open('yaml_demo/ya.yaml', 'r') as file:
    normal_data = yaml.load(file, Loader=yaml.UnsafeLoader)
    print(normal_data)