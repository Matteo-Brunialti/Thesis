import os
from augustus_id import id
import glob

file_location = '/opt/mydata'
os.chdir(file_location)
directory_cds_tr = 'cds_tr'
directory_cds = 'cds'


def augustus(filename):
    filename_no_extention = no_exetention(filename)
    augustus_species_tag = id(filename)
    augustus_out = filename_no_extention + '.gff3'
    os.system('augustus --gff3=on --species=' + augustus_species_tag + ' ' + filename + ' > ' + augustus_out)
    return


def gffread(filename):
    filename_no_extention = no_exetention(filename)
    gff_in = filename_no_extention + '.gff3'  # it's the same of augustus_out
    gff_cds = filename_no_extention + '_cds.fa'
    gff_cds_tr = filename_no_extention + '_cds_tr.fa'
    os.system('gffread ' + gff_in + ' -g ' + filename + ' -x ' + gff_cds + ' -y ' + gff_cds_tr)
    os.mkdir(directory_cds_tr), os.mkdir(directory_cds)
    os.system('mv *tr.fa ' + directory_cds_tr), os.system('mv *cds.fa ' + directory_cds)
    return


def orthofinder(file_ortho_location):
    return os.system('orthofinder -f ' + file_location + '/' + file_ortho_location)


def files(ext):
    return glob.glob(ext)


def extention(string):
    for i in string[::-1]:
        if i == '.':
            return string[len(string) - string.index(i):]


def no_exetention(string):
    for i in string[::-1]:
        if i == '.':
            return string[:len(string) - string.index(i)]


def workflow():
    files_list = files('.')  # list of file in directory
    var = 0
    for i in files_list:
        i = extention(i)
        if i == '.fna':
            var = 1
        elif i == '.gff3':
            var = 2
            break
    if var == 0:
        return print('error no files or worng files in directory')
    if var == 1:
        for i in files_list:
            print('the file going is:' + i)
            augustus(i)  # augustus
            print('augustus done')
    if var == 2:
        for i in files_list:
            if extention(i) == '.gff3':
                print('the file going is:' + i)
                gffread(i)  # gffread
                print('gffread done')


# orthofinder command
orthofinder(file_location + '/' + directory_cds)  # orthofinder
print('orthofinder done')

#orthofinder command
orthofinder() #orthofinder
print('orthofinder done')
