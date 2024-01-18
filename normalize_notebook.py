from nbformat import read, write, NO_CONVERT, validate, ValidationError, normalize

# Read the notebook
with open('your_notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = read(f, as_version=NO_CONVERT)

# Normalize the notebook
nb = normalize(nb)

# Validate the notebook
try:
    validate(nb)
except ValidationError as e:
    print(f"Validation error: {e}")

# Write the notebook back to the file
with open('your_notebook.ipynb', 'w', encoding='utf-8') as f:
    write(nb, f)