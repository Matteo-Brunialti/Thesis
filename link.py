import os
from augustus_id import id
import glob
from Bio import SeqIO
from multiprocessing import Pool
import shutil

file_location = '/opt/mydata'
os.chdir(file_location)

# my directory
path = '/opt/mydata'
augustus_dir = f'{path}/augustus'
gffread_dir = f'{path}/gffread'
tmp_dir = f'{path}/tmp'
tr_cds_dir = f'{gffread_dir}/tr_cds'
cds_dir = f'{gffread_dir}/cds'
orthofinder_dir = f'{path}/Orthofinder'


def build(foldername=os.getcwd()):
    l = ['/tmp', '/augustus', '/gffread', '/gffread/cds', '/gffread/tr_cds',
         '/Orthofinder']
    for directory in l:
        if not os.path.exists(foldername + directory):
            os.makedirs(foldername + directory)
    return


build()  # building data structure


def augustus(filename):
    augustus_out = filename.split('.')[0] + '.gff3'
    os.system(f'augustus --gff3=on --species={id(filename)} {filename} > {augustus_out}')  # --gff3=on
    return


def gffread(filename, option=''):
    filename_no_extension = filename.split('.')[0]
    os.system(
        f'gffread {filename} -g {filename_no_extension}.fna -x {filename_no_extension}_cds.fa -y {filename_no_extension}_tr_cds.fa')
    return


def orthofinder(file_ortho_location, option=''):
    os.system(f'orthofinder -d -f {file_ortho_location}')
    return f'orthofinder is done'


def split_fasta(fasta_file):
    l = []
    with open(fasta_file) as input_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
            handle = record.id + '.fna'
            l.append(handle)
            SeqIO.write(record, handle, "fasta")
    print(f'splitting of fasta file {fasta_file} status: done')
    return l


def join_gff(file, file_list):
    with open(file, "wb") as outfile:
        for f in file_list:
            f = f.split('.')[0] + '.gff3'
            with open(f, "rb") as infile:
                outfile.write(infile.read())


def workflow(path='/opt/mydata'):
    os.chdir(path)

    # base case no files are given
    if glob.glob('*.fna') == [] and glob.glob('*.gff3') == [] and os.listdir(augustus_dir) == []:
        return 'the files are incorrect'

    for f in os.listdir(path):
        if f.endswith('.fna'):
            shutil.move(f'{path}/f', augustus_dir)
        elif f.endswith('.gff3'):
            shutil.move(f'{path}/f', gffread_dir)

    os.chdir(tmp_dir)
    # augustus
    if len(os.listdir(gffread_dir)) - 2 != len(os.listdir(augustus_dir)):
        for f in os.listdir(augustus_dir):
            print(f'the file {f} has started augustus')

            shutil.copy(f'{augustus_dir}/{f}', tmp_dir)
            my_list = split_fasta(f)
            Pool(10).map(augustus, my_list)
            join_gff(f.split('.')[0] + '.gff3', my_list) # join gff with a list of gff3 file
            shutil.copy(f'{tmp_dir}/' + f.split('.')[0] + '.gff3', gffread_dir)

            print(f'the file {f} has generated gff3, status: done')
    for tf in os.listdir(tmp_dir):
        os.remove(tf)
    # gffread
    print(f'gffread analysis has started')
    for f in os.listdir(augustus_dir):
        shutil.copy(f'{augustus_dir}/{f}', tmp_dir)
    for f in os.listdir(gffread_dir):
        if f.endswith('.gff3'):
            shutil.copy(f'{gffread_dir}/{f}', tmp_dir)
    for f in os.listdir(tmp_dir):
        print(f'the file {f} has started gffread')

        gffread(f)
        shutil.copy(f'{tmp_dir}/' + f.split('.')[0] + '_tr_cds.fa', tr_cds_dir)
        shutil.copy(f'{tmp_dir}/' + f.split('.')[0] + '_cds.fa', cds_dir)

        print(f'the file {f} has generated cds and tr_cds, status: done')
    for tf in os.listdir(tmp_dir):
        os.remove(tf)

    # orthofinder
    print(f'orthofinder has started')
    for f in os.listdir(tr_cds_dir):
        shutil.copy(f, tmp_dir)
    orthofinder(tmp_dir)
    shutil.copytree(f'{tmp_dir}/OrthoFinder', orthofinder_dir)
    print(f'orthofinder done, you can find the data in the Orthofinder folder')

    return 'analysis done'


print(workflow())
