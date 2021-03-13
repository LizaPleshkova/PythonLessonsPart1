import zipfile
import os

folder_path = r'E:\Python\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\my\venv\folder1'
zip_path = r'E:\Python\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\my\venv\folder1\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# my_zip.write('E:\\Python\\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\\my\\venv\\folder1\\new1\\text1.txt', compress_type=zipfile.ZIP_DEFLATED, arcname='1.txt')
# my_zip.write('E:\\Python\\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\\my\\venv\\folder1\\new1\\text1.txt', 'new.txt', compress_type=zipfile.ZIP_DEFLATED)

for folder, sub_folders, files in os.walk(folder_path):
    print(files)
    for file in files:
        my_zip.write(os.path.join(folder, file))
my_zip.close()