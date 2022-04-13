#the identifier of augustus form a NCBI .fna file
d = {'species': 'identifier', 'Homo sapiens': 'human', 'Drosophila melanogaster': 'fly', 'Arabidopsis thaliana': 'arabidopsis',
     'Brugia malayi': 'brugia', 'Aedes aegypti': 'aedes', 'Tribolium castaneum': 'tribolium',
     'Schistosoma mansoni': 'schistosoma', 'Tetrahymena thermophila': 'tetrahymena', 'Galdieria sulphuraria': 'galdieria',
     'Zea mays': 'maize', 'Toxoplasma gondii': 'toxoplasma', 'Caenorhabditis elegans': '(elegans)',
     'Aspergillus fumigatus': 'aspergillus_fumigatus', 'Aspergillus nidulans': '(anidulans)',
     'Aspergillus oryzae': 'aspergillus_oryzae', 'Aspergillus terreus': 'aspergillus_terreus',
     'Botrytis cinerea': 'botrytis_cinerea', 'Candida albicans': 'candida_albicans',
     'Candida guilliermondii': 'candida_guilliermondii', 'Candida tropicalis': 'candida_tropicalis',
     'Chaetomium globosum': 'chaetomium_globosum', 'Coccidioides immitis': 'coccidioides_immitis',
     'Coprinus cinereus': 'coprinus_cinereus', 'Nicotiana attenuata': 'coyote_tobacco',
     'Cryptococcus neoformans gattii': 'cryptococcus_neoformans_gattii',
     'Cryptococcus neoformans neoformans': 'cryptococcus_neoformans_neoformans_JEC21',
     'Cryptococcus neoformans': '(cryptococcus)', 'Debaryomyces hansenii': 'debaryomyces_hansenii',
     'Encephalitozoon cuniculi': 'encephalitozoon_cuniculi_GB', 'Eremothecium gossypii': 'eremothecium_gossypii',
     'Fusarium graminearum': '(fusarium)', 'Histoplasma capsulatum': '(histoplasma)',
     'Kluyveromyces lactis': 'kluyveromyces_lactis', 'Laccaria bicolor': 'laccaria_bicolor', 'Petromyzon marinus': 'lamprey',
     'Leishmania tarentolae': 'leishmania_tarentolae', 'Lodderomyces elongisporus': 'lodderomyces_elongisporus',
     'Magnaporthe grisea': 'magnaporthe_grisea', 'Neurospora crassa': '(neurospora)',
     'Phanerochaete chrysosporium': '(pchrysosporium)', 'Pichia stipitis': 'pichia_stipitis',
     'Rhizopus oryzae': 'rhizopus_oryzae', 'Saccharomyces cerevisiae': '(saccharomyces)',
     'Schizosaccharomyces pombe': 'schizosaccharomyces_pombe',
     'Thermoanaerobacter tengcongensis': 'thermoanaerobacter_tengcongensis', 'Trichinella spiralis': 'trichinella',
     'Ustilago maydis': '(ustilago)', 'Yarrowia lipolytica': 'yarrowia_lipolytica', 'Nasonia vitripennis': 'nasonia',
     'Solanum lycopersicum': 'tomato', 'Chlamydomonas reinhardtii': 'chlamydomonas', 'Amphimedon queenslandica': 'amphimedon',
     'Pneumocystis jirovecii': 'pneumocystis', 'Triticum aestivum': 'wheat', 'Gallus gallus': 'chicken',
     'Danio rerio': 'zebrafish', 'Escherichia coli': 'E_coli_K12', 'Staphylococcus aureus': 's_aureus',
     'Volvox carteri': 'volvox'}

def id(filename):
    with open(filename) as f:
        return d[' '.join(f.readline().split(' ')[1:3])]

