import os
from augustus_id import id
import glob
from Bio import SeqIO
from multiprocessing import Pool
import shutil

file_location = '/opt/mydata'
os.chdir(file_location)

tmp_dir = '/opt/mydata/tmp'
os.makedirs(tmp_dir)

cds_dir = '/opt/mydata/cds'
os.makedirs(cds_dir)
tr_cds_dir = '/opt/mydata/tr_cds'
os.makedirs(tr_cds_dir)


def augustus(filename):
    augustus_species_tag = id(filename)
    augustus_out = os.path.splitext(filename) + '.gff3'
    os.system('augustus --gff3=on --species=' + augustus_species_tag + ' ' + filename + ' > ' + augustus_out)
    return (augustus_out)


def gffread(filename, option=''):
    filename_no_extension = os.path.splitext(filename)
    gff_cds = filename_no_extension + '_cds.fa'
    gff_tr_cds = filename_no_extension + '_tr_cds.fa'
    genomic_seqs_fasta = f'{filename_no_extension}.fna'
    os.system('gffread ' + filename + ' -g ' + genomic_seqs_fasta + ' -x ' + gff_cds + ' -y ' + gff_tr_cds)
    os.system(f'mv {gff_tr_cds} {tr_cds_dir}'), os.system(f'mv {gff_cds} {cds_dir}')
    return


def orthofinder(file_ortho_location, option=''):
    return os.system('orthofinder -d -f ' + file_ortho_location)


def split_fasta(fasta_file):
    with open(fasta_file) as input_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
            handle = record.id + '.fna'
            SeqIO.write(record, handle, "fasta")
    return print(f'splitting of fasta file {fasta_file} status: done')

def join_gff(file, read_files):
    with open(file, "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())


def workflow(folder_name=file_location):
    os.chdir(folder_name)
    var = 0
    files_list = os.listdir()
    for file in files_list:
        if file.endswith('fna'):
            var = 1
        elif file.endswith('.gff'):
            var = 2
    if var == 0:
        return 'something is wrong in the input file'
    elif var == 1:
        for file in files_list:
            print(f'the file going is {file}')
            os.system(f'mv {file} {tmp_dir}')
            os.chdir(tmp_dir)
            split_fasta(file)
            files_list = os.listdir()
            results = (Pool(5).map(augustus, files_list))
            gff3_file = f'{os.path.splitext(file)}.gff3'
            join_gff(gff3_file, results)  # function to create
            # os.system(f'mv {file} {file_location}')
            # for file in os.listdir():
              # os.remove(file)
            print(f'the file {file} has finished augustus')
    else:
        os.chdir(tmp_dir)
        for file in files_list:
            if file.endswith('.fna'):
                print(f'the file going is {file}')
                gffread(file)
                print(f'the file {file} has finished gffread')
    orthofinder(tr_cds_dir)

print(workflow())
