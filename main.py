import getcode

secret_code = getcode.get_code(total_values=4, duplicate=False)

print("secret_code:", secret_code)