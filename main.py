import getcode

secret_code = getcode.get_code(total_values=8, duplicate=False)

print("secret_code:", secret_code)