import sys
import os

def evaluate(prote, fieldSize):
	maxCharge = 14
	lenght = len(prote)
	last = len(prote)-fieldSize
	find = False

	if lenght < fieldSize: #prote size < fieldsize
		text = ''
                charge = 0.0
                #read the next lenght caracteres
                for j in range(lenght):
                        #hold the sequence of characteres
                        text += prote[j]
                        #compute the netCharge
                        if j == 0: #first caracter
                                charge += 0.996
                        elif j == lenght-1: #last caracter
                                charge += -1.0
                        elif prote[j] == 'C':
                                charge += -0.085
                        elif prote[j] == 'D':
                                charge += -1.0
                        elif prote[j] == 'E':
                                charge += -0.999
                        elif prote[j] == 'R':
                                charge += 1.0
                        elif prote[j] == 'K':
                                charge += 0.999
                        elif prote[j] == 'H':
                                charge += 0.048
                if charge < maxCharge:
			text=''
		saida = text+'\r'+'\n'
		return saida

	#for each character (does not include the last fieldsize characteres)
	for i in range(len(prote)-fieldSize+1):
		text = ''
		charge = 0.0
		#read the next fieldSize caracteres
		for j in range(fieldSize):
			#hold the sequence of characteres
			text += prote[i+j]
                        #compute the netCharge
                        if i == 0 and j == 0: #first caracter
                          	charge += 0.996
                        elif i == last and j == fieldSize-1: #last caracter
                          	charge += -1.0
                        elif prote[i+j] == 'C':
                          	charge += -0.085
                        elif prote[i+j] == 'D':
                            	charge += -1.0
                        elif prote[i+j] == 'E':
                            	charge += -0.999
                        elif prote[i+j] == 'R':
                          	charge += 1.0
                        elif prote[i+j] == 'K':
                          	charge += 0.999
                        elif prote[i+j] == 'H':
                          	charge += 0.048
		if charge >= maxCharge:
			find = True
			delta = i + fieldSize
			#hold the sequence of the next fieldSize characteres
			#for j in range(fieldSize):
				#if delta+j < lenght:
					#text += prote[delta+j]
			break
	#if len(text) == fieldSize:
	if not find:
		text='' #does not find the max charge
	saida = text+'\r'+'\n'
	return saida


#main function
def main():
	names = []
	fieldSize = 30
	blockSize = 1000
        #read the program arguments
        if len(sys.argv) < 3:
                print "Use: python", sys.argv[0], "<input complete file name>", "<output root file name>"
                sys.exit(0)

        filein = sys.argv[1] #input file name
        rootfileout = sys.argv[2] #output root file name

        #read the file's contents
        fin = open(filein, 'r')
        contents = fin.read()
	
	#open the first block of the output file
	block = 1
	fileout  = rootfileout + '_' + str(block) + '.txt'
        fout = open(fileout, 'w')
	#start the block size counter
	count = 0
	
	#split the file's contents by '>'
        proteins = str.split(contents, '>')[1:] #the file header is discarded
	#handle each protein...
        for prot in proteins:
		seq = []
                lista = str.split(prot, '\n') #split each protein 
		names.append(lista[0]) #salve the names
		#concatenate the sequences of amino acids of the protein
		for temp in lista[1:]:
			seq.append(temp[:])	
		seqfinal = ''.join(seq) 
		protName = str.split(lista[0]) #take the first name
		#fout.write(protName[0] + ',' +  evaluate(seqfinal, fieldSize))
		fout.write('>' + lista[0] + '\n' +  evaluate(seqfinal, fieldSize))
		print protName[0]
		count += 1 #increase the block size
		if (count % blockSize) == 0: #block is full: change the output file
			count = 0
			block += 1
			fout.close()
			fileout = rootfileout + '_' + str(block) + '.txt'
        		fout = open(fileout, 'w')
	if count == 0: #the last created file does not contain data, than remove it
		os.remove(fileout)
        fin.close()
	fout.close()
	print 'Done!'

main()
