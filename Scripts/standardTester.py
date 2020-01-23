# Science Fair 2020 - Aiden Lee and Emilia Lowe - Pedersen
# Sample tester
# Writes all results to a text file, and also saves it to an array

# dependencies
import time
import json
from tqdm import tqdm

# settings
settings = {
    'cipherID':'template',
    'trialNum':10,
    'wordlistPath':'C:\Scifair\wordlist.txt',
    'outputPath':'C:\Scifair\data\TemplateData.txt'
    }

# setup
startTime = 0
jsonData = {
    'data':{}
    }

# encrytion library setup

# encryption fuction
def encrypt(cleartext):
    # reset the machine to a set state
    return cleartext

# cleartexts
cleartexts = [
    'counselling',
    'epiperipheral',
    'semichorus',
    'preexpectation',
    'secondsighted',
    'pasgarde',
    'tuberculum',
    'brumalia',
    'songy',
    'barrancas'
    ]

# ciphertext generation
ciphertexts=[]
for i in cleartexts:
    ciphertexts.append(encrypt(i.strip().upper()))

# fancy console info
print('Now running tester: {}'.format(settings['cipherID']))
print('Outputing to {}'.format(settings['outputPath']))
print('Number of ciphertexts: {}'.format(len(ciphertexts)))
print('Scheduled for {} trials'.format(settings['trialNum']))

# tqdm setup
tmp=(settings['trialNum']*len(ciphertexts))
progBar=tqdm(total=tmp,leave=True)

# tester
for trialNum in range(settings['trialNum']):
    # trial data collection setup
    trialData = {
        'cipherID':settings['cipherID'],
        'trialNum':trialNum,
        'data':{}
        }
    # main testing loop
    for testCiphertext in ciphertexts:
        progBar.update(1)
        with open(settings['wordlistPath']) as wordlist:
            startTime = time.time()
            line = ''
            line = wordlist.readline()
            # loops through entire wordlist
            while line:
                # checks for a match with selected ciphertext
                if encrypt(line.strip().upper()) == testCiphertext:
                    # records data
                    trialData['data'].append({
                        'ciphertext': testCiphertext,
                        'cleartext': line, 
                        'time': time.time()-startTime
                        })
                    break
    # dumps data to a text file
    with open(settngs['outputPath']) as output:
        json.dump(trialData,output,indent=4)
    # saves data in an array
    jsonData['data'].append(trialData)
# stops the progress bar
progBar.close()
print('results')
print(jsonData)
