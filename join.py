
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['fsqgk.zip.000.NOTES', 'fsqgk.zip.001.NOTES', 'fsqgk.zip.002.NOTES', 'fsqgk.zip.003.NOTES', 'fsqgk.zip.004.NOTES', 'fsqgk.zip.005.NOTES', 'fsqgk.zip.006.NOTES', 'fsqgk.zip.007.NOTES', 'fsqgk.zip.008.NOTES', 'fsqgk.zip.009.NOTES', 'fsqgk.zip.010.NOTES', 'fsqgk.zip.011.NOTES', 'fsqgk.zip.012.NOTES', 'fsqgk.zip.013.NOTES', 'fsqgk.zip.014.NOTES', 'fsqgk.zip.015.NOTES', 'fsqgk.zip.016.NOTES', 'fsqgk.zip.017.NOTES', 'fsqgk.zip.018.NOTES', 'fsqgk.zip.019.NOTES', 'fsqgk.zip.020.NOTES', 'fsqgk.zip.021.NOTES', 'fsqgk.zip.022.NOTES', 'fsqgk.zip.023.NOTES', 'fsqgk.zip.024.NOTES', 'fsqgk.zip.025.NOTES', 'fsqgk.zip.026.NOTES', 'fsqgk.zip.027.NOTES', 'fsqgk.zip.028.NOTES', 'fsqgk.zip.029.NOTES', 'fsqgk.zip.030.NOTES', 'fsqgk.zip.031.NOTES', 'fsqgk.zip.032.NOTES', 'fsqgk.zip.033.NOTES', 'fsqgk.zip.034.NOTES', 'fsqgk.zip.035.NOTES', 'fsqgk.zip.036.NOTES', 'fsqgk.zip.037.NOTES', 'fsqgk.zip.038.NOTES', 'fsqgk.zip.039.NOTES'],'fsqgk.zip')
print('unziping')
with zipfile.ZipFile('fsqgk.zip', 'r') as zip_ref:
    zip_ref.extractall('fsqgk')
os.remove('fsqgk.zip')
os.remove('join.py')
