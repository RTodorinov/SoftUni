
# path = input().split("\\")
# path_name_with_ext = path[-1].split(".")
# print(f"File name: {path_name_with_ext[0]}"
#       f"\nFile extension: {path_name_with_ext[1]}")


# когато има повече точки в последния файл
path = input().split("\\")
path_name_with_ext = path[-1]

path_name_parts = path_name_with_ext.split(".")
extension = path_name_parts.pop()
print(f"File name: {'.'.join(path_name_parts)}"
      f"\nFile extension: {extension}")

