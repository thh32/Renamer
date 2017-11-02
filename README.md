# Renamer
Gives each sequence in a FASTA file a unique name


Give each sequence a number for the sequence in the file, the files name and a 20 character long unique ID.


Run for phylophlan using;

for cfile in *.faa ; do echo $cfile && python Renamer.py -i $cfile -o ${cfile}.UNIQ.faa && gzip ${cfile} ; done


