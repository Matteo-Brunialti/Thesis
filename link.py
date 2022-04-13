import os
from augustus_id import id
import glob

file_location = '/root/mydata'

def augustus(filename, filename_no_extention):
    augustus_species_tag = id(filename)
    augustus_out = filename_no_extention + '.gff3'
    return os.system('augustus --gff3=on --species=' + augustus_species_tag + ' ' + filename + ' > ' + augustus_out)

def gffread(filename, filename_no_extention):
    gff_in = filename_no_extention + '.gff3' #it's the same of augustus_out
    gff_cds = filename_no_extention + '_cds.fa'
    gff_tr_cds = filename_no_extention + '_tr_cds.fa'
    return os.system('gffread ' + gff_in + ' -g ' + filename + ' -x ' + gff_cds + ' -y ' + gff_tr_cds)

def orthofinder():
    return os.system('./orthofinder -f' + file_location)

def files(ext):
    return glob.glob(ext)

for i in files('*.fna'):
    filename_no_extention = i[:-4]
    print('the file going is:' + i)
    augustus(i, filename_no_extention)  #augustus
    print('augustus done')
    gffread(i, filename_no_extention)  #gffread
    print('gffread done')

#orthofinder command
orthofinder() #orthofinder
print('orthofinder done')
