from subprocess import check_output
def test_bf0461f5474cd711525dcd104452005b():    #        tab delimited annotated sequence stream
    URI = '''https://api.mg-rast.org/annotation/sequence/mgm4447943.3?evalue=10&type=organism&source=SwissProt'''
    CMD = '''curl 'https://api.mg-rast.org/annotation/sequence/mgm4447943.3?evalue=10&type=organism&source=SwissProt' 2> bf0461f5474cd711525dcd104452005b.err > bf0461f5474cd711525dcd104452005b.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_339b8286827d5051c693e51049ee5cf6():    #       tab delimited annotated sequence stream
    CMD = '''curl -X POST -d '{"source":"SwissProt","type":"organism","data":["000821a2e2f63df1a3873e4b280002a8","15bf1950bd9867099e72ea6516e3d602"]}' "https://api.mg-rast.org/annotation/sequence/mgm4447943.3" 2> 339b8286827d5051c693e51049ee5cf6.err > 339b8286827d5051c693e51049ee5cf6.out'''
    o = check_output(CMD, shell=True)
def test_4978084e1997239e5ea92c873262585e():    #        tab delimited blast m8 with annotation
    URI = '''https://api.mg-rast.org/annotation/similarity/mgm4447943.3?identity=80&type=function&source=KO'''
    CMD = '''curl 'https://api.mg-rast.org/annotation/similarity/mgm4447943.3?identity=80&type=function&source=KO' 2> 4978084e1997239e5ea92c873262585e.err > 4978084e1997239e5ea92c873262585e.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_68b42706feff1891cc279d2b34c83ea7():    #       tab delimited blast m8 with annotation
    CMD = '''curl -X POST -d '{"source":"KO","type":"function","data":["000821a2e2f63df1a3873e4b280002a8","15bf1950bd9867099e72ea6516e3d602"]}' "https://api.mg-rast.org/annotation/sequence/mgm4447943.3" 2> 68b42706feff1891cc279d2b34c83ea7.err > 68b42706feff1891cc279d2b34c83ea7.out'''
    o = check_output(CMD, shell=True)
def test_093f18b3f9fdf63756d185ca3eb4600a():    #        Calculate alpha diversity value for given ID and taxon level.
    URI = '''https://api.mg-rast.org/compute/alphadiversity/mgm4447943.3?level=order'''
    CMD = '''curl 'https://api.mg-rast.org/compute/alphadiversity/mgm4447943.3?level=order' 2> 093f18b3f9fdf63756d185ca3eb4600a.err > 093f18b3f9fdf63756d185ca3eb4600a.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_be43b392342e558d8285fda7ce6304d3():    #        Calculate rarefaction x-y coordinates for given ID and taxon level.
    URI = '''https://api.mg-rast.org/compute/rarefaction/mgm4447943.3?level=order'''
    CMD = '''curl 'https://api.mg-rast.org/compute/rarefaction/mgm4447943.3?level=order' 2> be43b392342e558d8285fda7ce6304d3.err > be43b392342e558d8285fda7ce6304d3.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_68e5cdee454154209011533a7cc5723e():    #        Produce NCBI-BLAST sequence alinments for given md5sum and its hits.
    URI = '''https://api.mg-rast.org/compute/blast/mgm4447943.3?md5=15bf1950bd9867099e72ea6516e3d602'''
    CMD = '''curl 'https://api.mg-rast.org/compute/blast/mgm4447943.3?md5=15bf1950bd9867099e72ea6516e3d602' 2> 68e5cdee454154209011533a7cc5723e.err > 68e5cdee454154209011533a7cc5723e.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_08a8e4cd32d6f24f22775e83254557a3():    #       Calculate normalized values for given input data.
    CMD = '''curl -X POST -d '{"columns": ["mgm4441619.3","mgm4441656.4","mgm4441680.3","mgm4441681.3"], "rows": ["Eukaryota","Bacteria","Archaea"], "data": [[135,410,848,1243],[4397,6529,71423,204413],[1422,2156,874,1138]]}' "https://api.mg-rast.org/compute/normalize" 2> 08a8e4cd32d6f24f22775e83254557a3.err > 08a8e4cd32d6f24f22775e83254557a3.out'''
    o = check_output(CMD, shell=True)
def test_352f914894421f3fc8369da8b05ca764():    #       Calculate a distance matrix for given input data.
    CMD = '''curl -X POST -d '{"distance":"euclidean","columns": ["mgm4441619.3","mgm4441656.4","mgm4441680.3","mgm4441681.3"], "rows": ["Eukaryota","Bacteria","Archaea"], "data": [[135,410,848,1243],[4397,6529,71423,204413],[1422,2156,874,1138]]}' "https://api.mg-rast.org/compute/distance" 2> 352f914894421f3fc8369da8b05ca764.err > 352f914894421f3fc8369da8b05ca764.out'''
    o = check_output(CMD, shell=True)
def test_1cc8a59993211d6b8f8aaf30f9b36aff():    #       Calculate a dendrogram for given input data.
    CMD = '''curl -X POST -d '{"raw":0,"cluster":"mcquitty","columns": ["mgm4441619.3","mgm4441656.4","mgm4441680.3","mgm4441681.3"], "rows": ["Eukaryota","Bacteria","Archaea"], "data": [[135,410,848,1243],[4397,6529,71423,204413],[1422,2156,874,1138]]}' "https://api.mg-rast.org/compute/heatmap" 2> 1cc8a59993211d6b8f8aaf30f9b36aff.err > 1cc8a59993211d6b8f8aaf30f9b36aff.out'''
    o = check_output(CMD, shell=True)
def test_7e57d184dd8e9688f4f69e903dd78039():    #       Calculate a PCoA for given input data.
    CMD = '''curl -X POST -d '{"raw":1,"distance":"euclidean","columns": ["mgm4441619.3","mgm4441656.4","mgm4441680.3","mgm4441681.3"], "rows": ["Eukaryota","Bacteria","Archaea"], "data": [[135,410,848,1243],[4397,6529,71423,204413],[1422,2156,874,1138]]}' "https://api.mg-rast.org/compute/pcoa" 2> 7e57d184dd8e9688f4f69e903dd78039.err > 7e57d184dd8e9688f4f69e903dd78039.out'''
    o = check_output(CMD, shell=True)
def test_854ae4e0208dbc8ac43d23d04d9d8ea8():    #        Returns a darkmatter sequence file.
    URI = '''https://api.mg-rast.org/darkmatter/mgm4447943.3?'''
    CMD = '''curl 'https://api.mg-rast.org/darkmatter/mgm4447943.3?' 2> 854ae4e0208dbc8ac43d23d04d9d8ea8.err > 854ae4e0208dbc8ac43d23d04d9d8ea8.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_a1f7d6aa8a46de535b50f25a228bbc57():    #        Returns a single sequence file.
    URI = '''https://api.mg-rast.org/download/mgm4447943.3?file=350.1'''
    CMD = '''curl 'https://api.mg-rast.org/download/mgm4447943.3?file=350.1' 2> a1f7d6aa8a46de535b50f25a228bbc57.err > a1f7d6aa8a46de535b50f25a228bbc57.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_0ad289490c101f5d4a34b76e3cf17dd4():    #        Summary of MG-RAST analysis-pipeline workflow and commands.
    URI = '''https://api.mg-rast.org/download/history/mgm4447943.3'''
    CMD = '''curl 'https://api.mg-rast.org/download/history/mgm4447943.3' 2> 0ad289490c101f5d4a34b76e3cf17dd4.err > 0ad289490c101f5d4a34b76e3cf17dd4.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_475ea223c2861425b17473d42c5aab8f():    #        Returns a list of sets of sequence files for the given id.
    URI = '''https://api.mg-rast.org/download/mgm4447943.3?stage=650'''
    CMD = '''curl 'https://api.mg-rast.org/download/mgm4447943.3?stage=650' 2> 475ea223c2861425b17473d42c5aab8f.err > 475ea223c2861425b17473d42c5aab8f.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_c93ca883230dbbca572572124767bd03():    #       lists the contents of the user inbox
    CMD = '''curl -X GET -H "auth: auth_key" "https://api.mg-rast.org/inbox" 2> c93ca883230dbbca572572124767bd03.err > c93ca883230dbbca572572124767bd03.out'''
    o = check_output(CMD, shell=True)
def test_0da1888480b0709036726fec8d547773():    #       view status of AWE inbox actions
    CMD = '''curl -X GET -H "auth: auth_key" "https://api.mg-rast.org/inbox/pending?queued&completed" 2> 0da1888480b0709036726fec8d547773.err > 0da1888480b0709036726fec8d547773.out'''
    o = check_output(CMD, shell=True)
def test_fd3ce4cad9fbb586184601df43e59a5b():    #       receives user inbox data upload, auto-uncompress if has .gz or .bz2 file extension
    CMD = '''curl -X POST -H "auth: auth_key" -F "upload=@sequences.fastq" "https://api.mg-rast.org/inbox" 2> fd3ce4cad9fbb586184601df43e59a5b.err > fd3ce4cad9fbb586184601df43e59a5b.out'''
    o = check_output(CMD, shell=True)
def test_8cf68cacf8a4010ad82a3fcc7b094b53():    #       delete indicated file from inbox
    CMD = '''curl -X DELETE -H "auth: auth_key" "https://api.mg-rast.org/inbox/cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" 2> 8cf68cacf8a4010ad82a3fcc7b094b53.err > 8cf68cacf8a4010ad82a3fcc7b094b53.out'''
    o = check_output(CMD, shell=True)
def test_48e721ca63c3610650285c1e1fe6de8e():    #       unpacks an archive upload into mutlple inbox files. supports: .zip, .tar, .tar.gz, .tar.bz2
    CMD = '''curl -X GET -H "auth: auth_key" -F "format=tar" "https://api.mg-rast.org/inbox/upload/cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" 2> 48e721ca63c3610650285c1e1fe6de8e.err > 48e721ca63c3610650285c1e1fe6de8e.out'''
    o = check_output(CMD, shell=True)
def test_4e7cb41ce81012d43762466725fc65c9():    #       get basic file info - returns results and updates shock node
    CMD = '''curl -X GET -H "auth: auth_key" "https://api.mg-rast.org/inbox/info/cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" 2> 4e7cb41ce81012d43762466725fc65c9.err > 4e7cb41ce81012d43762466725fc65c9.out'''
    o = check_output(CMD, shell=True)
def test_94c8286b3e5003f03e1ea3ea70bcc8f2():    #       validate metadata spreadsheet in inbox
    CMD = '''curl -X GET -H "auth: auth_key" "https://api.mg-rast.org/inbox/validate/cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" 2> 94c8286b3e5003f03e1ea3ea70bcc8f2.err > 94c8286b3e5003f03e1ea3ea70bcc8f2.out'''
    o = check_output(CMD, shell=True)
def test_925d23448291db8cd558c04f26adf94c():    #       runs sequence stats on file in user inbox - submits AWE job
    CMD = '''curl -X GET -H "auth: auth_key" "https://api.mg-rast.org/inbox/stats/cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" 2> 925d23448291db8cd558c04f26adf94c.err > 925d23448291db8cd558c04f26adf94c.out'''
    o = check_output(CMD, shell=True)
def test_a4527dd2910b4bd523947240f20d3fca():    #       cancel (delete) given AWE job ID
    CMD = '''curl -X GET -H "auth: auth_key" "https://api.mg-rast.org/inbox/cancel/cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" 2> a4527dd2910b4bd523947240f20d3fca.err > a4527dd2910b4bd523947240f20d3fca.out'''
    o = check_output(CMD, shell=True)
def test_5dcf850e81902a6e19861158ebeeec49():    #       rename indicated file from inbox
    CMD = '''curl -X POST -H "auth: auth_key" "https://api.mg-rast.org/inbox/rename" 2> 5dcf850e81902a6e19861158ebeeec49.err > 5dcf850e81902a6e19861158ebeeec49.out'''
    o = check_output(CMD, shell=True)
def test_e70762df20c7be49a5f742a91ab6f0cf():    #       create fastq file from sff file - submits AWE job
    CMD = '''curl -X POST -H "auth: auth_key" -F "sff_file=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" "https://api.mg-rast.org/inbox/sff2fastq" 2> e70762df20c7be49a5f742a91ab6f0cf.err > e70762df20c7be49a5f742a91ab6f0cf.out'''
    o = check_output(CMD, shell=True)
def test_77cc651f99544db3fe87afd017f43cfa():    #       demultiplex seq file with barcode file - submits AWE job
    CMD = '''curl -X POST -H "auth: auth_key" -F "seq_file=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" -F "barcode_file=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" "https://api.mg-rast.org/inbox/demultiplex" 2> 77cc651f99544db3fe87afd017f43cfa.err > 77cc651f99544db3fe87afd017f43cfa.out'''
    o = check_output(CMD, shell=True)
def test_a234d523384cae184f53ec5d561e28d8():    #       merge overlapping paired-end fastq files - submits AWE job
    CMD = '''curl -X POST -H "auth: auth_key" -F "retain=1" -F "pair_file_1=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" -F "pair_file_2=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" "https://api.mg-rast.org/inbox/pairjoin" 2> a234d523384cae184f53ec5d561e28d8.err > a234d523384cae184f53ec5d561e28d8.out'''
    o = check_output(CMD, shell=True)
def test_7502b6ba11a891b18291be501bb44672():    #       merge overlapping paired-end fastq files and demultiplex based on index file - submits AWE job
    CMD = '''curl -X POST -H "auth: auth_key" -F "pair_file_1=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" -F "pair_file_2=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" -F "index_file=cfb3d9e1-c9ba-4260-95bf-e410c57b1e49" "https://api.mg-rast.org/inbox/pairjoin_demultiplex" 2> 7502b6ba11a891b18291be501bb44672.err > 7502b6ba11a891b18291be501bb44672.out'''
    o = check_output(CMD, shell=True)
def test_14ff2d38c41218f3af58b2004a5d69a2():    #        Returns a set of data matching the query criteria.
    URI = '''https://api.mg-rast.org/library?limit=20&order=name'''
    CMD = '''curl 'https://api.mg-rast.org/library?limit=20&order=name' 2> 14ff2d38c41218f3af58b2004a5d69a2.err > 14ff2d38c41218f3af58b2004a5d69a2.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_77b4d2434b8f73ff6848e966f239402c():    #        Returns a single data object.
    URI = '''https://api.mg-rast.org/library/mgl52924?verbosity=full'''
    CMD = '''curl 'https://api.mg-rast.org/library/mgl52924?verbosity=full' 2> 77b4d2434b8f73ff6848e966f239402c.err > 77b4d2434b8f73ff6848e966f239402c.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_63db592a6ed698b4d53d5252491e6f5c():    #        Return functional hierarchy
    URI = '''https://api.mg-rast.org/m5nr/ontology?source=Subsystems&min_level=level3'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/ontology?source=Subsystems&min_level=level3' 2> 63db592a6ed698b4d53d5252491e6f5c.err > 63db592a6ed698b4d53d5252491e6f5c.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_530de3b8d27c7229184f7b4931f0efd9():    #        Return organism hierarchy
    URI = '''https://api.mg-rast.org/m5nr/taxonomy?filter=Bacteroidetes&filter_level=phylum&min_level=genus'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/taxonomy?filter=Bacteroidetes&filter_level=phylum&min_level=genus' 2> 530de3b8d27c7229184f7b4931f0efd9.err > 530de3b8d27c7229184f7b4931f0efd9.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_bef098bdd304902d730cab5a79a1f191():    #        Return all sources in M5NR
    URI = '''https://api.mg-rast.org/m5nr/sources'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/sources' 2> bef098bdd304902d730cab5a79a1f191.err > bef098bdd304902d730cab5a79a1f191.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_3f462bbac13117870755eead0dc46d64():    #        Return annotation of given source protein ID
    URI = '''https://api.mg-rast.org/m5nr/accession/YP_003268079.1'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/accession/YP_003268079.1' 2> 3f462bbac13117870755eead0dc46d64.err > 3f462bbac13117870755eead0dc46d64.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_cbd270785474a895912f3737f1cc7b25():    #        Return annotations for alias IDs containing the given text
    URI = '''https://api.mg-rast.org/m5nr/alias/GI:485708283'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/alias/GI:485708283' 2> cbd270785474a895912f3737f1cc7b25.err > cbd270785474a895912f3737f1cc7b25.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_a00503660af17c9ab8a505c2dff4a0af():    #        Return annotation(s) or sequence of given md5sum (M5NR ID)
    URI = '''https://api.mg-rast.org/m5nr/md5/000821a2e2f63df1a3873e4b280002a8?source=InterPro'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/md5/000821a2e2f63df1a3873e4b280002a8?source=InterPro' 2> a00503660af17c9ab8a505c2dff4a0af.err > a00503660af17c9ab8a505c2dff4a0af.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_45c7e500a0bf8585f96da513807d6a2d():    #        Return annotations for function names containing the given text
    URI = '''https://api.mg-rast.org/m5nr/function/sulfatase?source=GenBank'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/function/sulfatase?source=GenBank' 2> 45c7e500a0bf8585f96da513807d6a2d.err > 45c7e500a0bf8585f96da513807d6a2d.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_be4fe029618e91007d6758acc3f6b851():    #        Return annotations for organism names containing the given text
    URI = '''https://api.mg-rast.org/m5nr/organism/akkermansia?source=KEGG'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/organism/akkermansia?source=KEGG' 2> be4fe029618e91007d6758acc3f6b851.err > be4fe029618e91007d6758acc3f6b851.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_e7d349855e898967f0efb647fc0e8462():    #        Return annotation(s) for md5sum (M5NR ID) of given sequence
    URI = '''https://api.mg-rast.org/m5nr/sequence/MSTAITRQIVLDTETTGMNQIGAHYEGHKIIEIGAVEVVNRRLTGNNFHVYLKPDRLVDPEAFGVHGIADEFLLDKPTFAEVADEFMDYIRGAELVIHNAAFDIGFMDYEFSLLKRDIPKTNTFCKVTDSLAVARKMFPGKRNSLDALCARYEIDNSKRTLHGALLDAQILAEVYLAMTGGQTSMAFAMEGETQQQQGEATIQRIVRQASKLRVVFATDEEIAAHEARLDLVQKKGGSCLWRA?source=TrEMBL'''
    CMD = '''curl 'https://api.mg-rast.org/m5nr/sequence/MSTAITRQIVLDTETTGMNQIGAHYEGHKIIEIGAVEVVNRRLTGNNFHVYLKPDRLVDPEAFGVHGIADEFLLDKPTFAEVADEFMDYIRGAELVIHNAAFDIGFMDYEFSLLKRDIPKTNTFCKVTDSLAVARKMFPGKRNSLDALCARYEIDNSKRTLHGALLDAQILAEVYLAMTGGQTSMAFAMEGETQQQQGEATIQRIVRQASKLRVVFATDEEIAAHEARLDLVQKKGGSCLWRA?source=TrEMBL' 2> e7d349855e898967f0efb647fc0e8462.err > e7d349855e898967f0efb647fc0e8462.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_57873ec56edbca158a5e32984a69f535():    #       Return annotations of given source protein IDs
    CMD = '''curl -X POST -d '{"order":"function","data":["YP_003268079.1","COG1764"]}' "https://api.mg-rast.org/m5nr/accession" 2> 57873ec56edbca158a5e32984a69f535.err > 57873ec56edbca158a5e32984a69f535.out'''
    o = check_output(CMD, shell=True)
def test_757f6029083aa957a0614f386bba2c09():    #       Return annotations for aliases containing the given texts
    CMD = '''curl -X POST -d '{"order":"function","data":["GI:485708283","fig|511145.6.peg.216"]}' "https://api.mg-rast.org/m5nr/alias" 2> 757f6029083aa957a0614f386bba2c09.err > 757f6029083aa957a0614f386bba2c09.out'''
    o = check_output(CMD, shell=True)
def test_5ade830aaf8947985af71d44e1952d16():    #       Return annotations or sequences of given md5sums (M5NR ID)
    CMD = '''curl -X POST -d '{"source":"InterPro","data":["000821a2e2f63df1a3873e4b280002a8","15bf1950bd9867099e72ea6516e3d602"]}' "https://api.mg-rast.org/m5nr/md5" 2> 5ade830aaf8947985af71d44e1952d16.err > 5ade830aaf8947985af71d44e1952d16.out'''
    o = check_output(CMD, shell=True)
def test_4737573e4564fda6a5783742ca88db4c():    #       Return annotations for function names containing the given texts
    CMD = '''curl -X POST -d '{"source":"GenBank","limit":50,"data":["sulfatase","phosphatase"]}' "https://api.mg-rast.org/m5nr/function" 2> 4737573e4564fda6a5783742ca88db4c.err > 4737573e4564fda6a5783742ca88db4c.out'''
    o = check_output(CMD, shell=True)
def test_9d1b020daf035e015741ae38eaa4d504():    #       Return annotations for organism names containing the given texts
    CMD = '''curl -X POST -d '{"source":"KEGG","order":"accession","data":["akkermansia","yersinia"]}' "https://api.mg-rast.org/m5nr/organism" 2> 9d1b020daf035e015741ae38eaa4d504.err > 9d1b020daf035e015741ae38eaa4d504.out'''
    o = check_output(CMD, shell=True)
def test_9b7bc182a5851760d64822e3da629fbb():    #       Return annotations for md5s (M5NR ID) of given sequences
    CMD = '''curl -X POST -d '{"source":"GenBank","order":"source","data":["MAGENHQWQGSIL","MAGENHQWQGSIL"]}' "https://api.mg-rast.org/m5nr/sequence" 2> 9b7bc182a5851760d64822e3da629fbb.err > 9b7bc182a5851760d64822e3da629fbb.out'''
    o = check_output(CMD, shell=True)
def test_94477516fd2a92c2e1a63b78c2f749ab():    #        Returns a BIOM object.
    URI = '''https://api.mg-rast.org/matrix/organism?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=family&source=RefSeq&evalue=15'''
    CMD = '''curl 'https://api.mg-rast.org/matrix/organism?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=family&source=RefSeq&evalue=15' 2> 94477516fd2a92c2e1a63b78c2f749ab.err > 94477516fd2a92c2e1a63b78c2f749ab.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_dc50f6494186a9686e4aba71532cd125():    #        Returns a BIOM object.
    URI = '''https://api.mg-rast.org/matrix/function?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=level3&source=Subsystems&identity=80'''
    CMD = '''curl 'https://api.mg-rast.org/matrix/function?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=level3&source=Subsystems&identity=80' 2> dc50f6494186a9686e4aba71532cd125.err > dc50f6494186a9686e4aba71532cd125.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_afca8786a7ba38d62c54efc0e0f47755():    #        Returns static template for metadata object relationships and types
    URI = '''https://api.mg-rast.org/metadata/template'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/template' 2> afca8786a7ba38d62c54efc0e0f47755.err > afca8786a7ba38d62c54efc0e0f47755.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_5f0e7489e011a9ec5c40918acb32e754():    #        Returns static controlled vocabularies used in metadata. By default returns all CVs at latest version. If label and version options used, returns those specific values.
    URI = '''https://api.mg-rast.org/metadata/cv?label=country'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/cv?label=country' 2> 5f0e7489e011a9ec5c40918acb32e754.err > 5f0e7489e011a9ec5c40918acb32e754.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_7d7bce8d921ba0083806b0aa6aafbe19():    #        Returns static ontology used in metadata for the given name and version.
    URI = '''https://api.mg-rast.org/metadata/ontology?name=biome&version=2017-04-15'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/ontology?name=biome&version=2017-04-15' 2> 7d7bce8d921ba0083806b0aa6aafbe19.err > 7d7bce8d921ba0083806b0aa6aafbe19.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_eb28e5343d589f377ec80bcd95c63f93():    #        Returns all versions available for given ontology.
    URI = '''https://api.mg-rast.org/metadata/version?label=biome'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/version?label=biome' 2> eb28e5343d589f377ec80bcd95c63f93.err > eb28e5343d589f377ec80bcd95c63f93.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_88aed515f7afbd8c9038c71a2b088eb6():    #        Returns list of unique metadata values submitted by users for given label
    URI = '''https://api.mg-rast.org/metadata/view/biome'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/view/biome' 2> 88aed515f7afbd8c9038c71a2b088eb6.err > 88aed515f7afbd8c9038c71a2b088eb6.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_c44c8b35b39a74ddc9e20ff501d7d67d():    #        Returns full nested metadata for a project in same format as template, or metadata for a single metagenome.
    URI = '''https://api.mg-rast.org/metadata/export/mgp128'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/export/mgp128' 2> c44c8b35b39a74ddc9e20ff501d7d67d.err > c44c8b35b39a74ddc9e20ff501d7d67d.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_c9ae49e087db2722acb6e25ca9a29132():    #       Create project with given metadata spreadsheet and metagenome IDs, either upload or shock node
    CMD = '''curl -X POST -F "metagenome=mgm12345" -F "metagenome=mgm67890" -F "upload=@metadata.xlsx" "https://api.mg-rast.org/metadata/import" 2> c9ae49e087db2722acb6e25ca9a29132.err > c9ae49e087db2722acb6e25ca9a29132.out'''
    o = check_output(CMD, shell=True)
def test_2c603ef4c925f2b5b0110d677193669a():    #       Update project with given metadata spreadsheet and metagenome IDs, either upload or shock node
    CMD = '''curl -X POST -F "project=mgp123" -F "upload=@metadata.xlsx" "https://api.mg-rast.org/metadata/update" 2> 2c603ef4c925f2b5b0110d677193669a.err > 2c603ef4c925f2b5b0110d677193669a.out'''
    o = check_output(CMD, shell=True)
def test_1f241ea51e9d8688cc41b4cde83fd0b0():    #       Validate given metadata spreadsheet, either upload or shock node
    CMD = '''curl -X POST -F "upload=@metadata.xlsx" "https://api.mg-rast.org/metadata/validate" 2> 1f241ea51e9d8688cc41b4cde83fd0b0.err > 1f241ea51e9d8688cc41b4cde83fd0b0.out'''
    o = check_output(CMD, shell=True)
def test_17dc47fbbb7d58c69fd69c9e996d9a94():    #        Validate given metadata value
    URI = '''https://api.mg-rast.org/metadata/validate?category=sample&label=material&value=soil'''
    CMD = '''curl 'https://api.mg-rast.org/metadata/validate?category=sample&label=material&value=soil' 2> 17dc47fbbb7d58c69fd69c9e996d9a94.err > 17dc47fbbb7d58c69fd69c9e996d9a94.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_eb494bafc265fe1ecd27703324278476():    #        Returns a set of data matching the query criteria.
    URI = '''https://api.mg-rast.org/metagenome?limit=20&order=name'''
    CMD = '''curl 'https://api.mg-rast.org/metagenome?limit=20&order=name' 2> eb494bafc265fe1ecd27703324278476.err > eb494bafc265fe1ecd27703324278476.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_0c9e1784736939f8eea4df3ee19e60b8():    #        Returns a single data object.
    URI = '''https://api.mg-rast.org/metagenome/mgm4447943.3?verbosity=metadata'''
    CMD = '''curl 'https://api.mg-rast.org/metagenome/mgm4447943.3?verbosity=metadata' 2> 0c9e1784736939f8eea4df3ee19e60b8.err > 0c9e1784736939f8eea4df3ee19e60b8.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_59a9013eb264ffdc2c5d1ab80b487a71():    #        Submits profile creation
    URI = '''https://api.mg-rast.org/profile/mgm4447943.3?source=RefSeq&format=biom'''
    CMD = '''curl 'https://api.mg-rast.org/profile/mgm4447943.3?source=RefSeq&format=biom' 2> 59a9013eb264ffdc2c5d1ab80b487a71.err > 59a9013eb264ffdc2c5d1ab80b487a71.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_d5cb4930331ec889e859fa815fdcc48b():    #        Returns a set of data matching the query criteria.
    URI = '''https://api.mg-rast.org/project?limit=20&order=name'''
    CMD = '''curl 'https://api.mg-rast.org/project?limit=20&order=name' 2> d5cb4930331ec889e859fa815fdcc48b.err > d5cb4930331ec889e859fa815fdcc48b.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_d754c6a2f59125b6f5b06562eb0cfc3b():    #        Returns a single data object.
    URI = '''https://api.mg-rast.org/project/mgp128?verbosity=full'''
    CMD = '''curl 'https://api.mg-rast.org/project/mgp128?verbosity=full' 2> d754c6a2f59125b6f5b06562eb0cfc3b.err > d754c6a2f59125b6f5b06562eb0cfc3b.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_b9e674e88feb451d3bdcb549756ef850():    #        Returns a set of data matching the query criteria.
    URI = '''https://api.mg-rast.org/sample?limit=20&order=name'''
    CMD = '''curl 'https://api.mg-rast.org/sample?limit=20&order=name' 2> b9e674e88feb451d3bdcb549756ef850.err > b9e674e88feb451d3bdcb549756ef850.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_cc9ab29aac803a9025381f15a4ffb394():    #        Returns a single data object.
    URI = '''https://api.mg-rast.org/sample/mgs25823?verbosity=full'''
    CMD = '''curl 'https://api.mg-rast.org/sample/mgs25823?verbosity=full' 2> cc9ab29aac803a9025381f15a4ffb394.err > cc9ab29aac803a9025381f15a4ffb394.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_458942635efb2b87477ccd0ba9565a1c():    #        Elastic search
    URI = '''https://api.mg-rast.org/search?material=saline water'''
    CMD = '''curl 'https://api.mg-rast.org/search?material=saline water' 2> 458942635efb2b87477ccd0ba9565a1c.err > 458942635efb2b87477ccd0ba9565a1c.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_2fc0943b297f5b1c1beedbff1b971a6f():    #        Checks if the referenced JSON structure is a valid template
    URI = '''https://api.mg-rast.org/validation/template/'''
    CMD = '''curl 'https://api.mg-rast.org/validation/template/' 2> 2fc0943b297f5b1c1beedbff1b971a6f.err > 2fc0943b297f5b1c1beedbff1b971a6f.out'''
    o = check_output("curl {}".format(URI), shell=True)
def test_84167878cdbb204047cc950e6fdb7b13():    #        Returns a single data object.
    URI = '''https://api.mg-rast.org/validation/data/?template='''
    CMD = '''curl 'https://api.mg-rast.org/validation/data/?template=' 2> 84167878cdbb204047cc950e6fdb7b13.err > 84167878cdbb204047cc950e6fdb7b13.out'''
    o = check_output("curl {}".format(URI), shell=True)
