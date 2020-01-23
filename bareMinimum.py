# Science Fair 2020 - Aiden Lee and Emelia Lowe - Pedersen
# Sample tester

# dependencies
import time
import tqdm
import json

# settings
settings = {
    'cipherID':'template',
    'trialNum':10,
    'wordlistPath':'C:\Scifair\wordlist.txt',
    'outputPath':'C:\Scifair\data\TemplateData.txt'
    }

# setup
startTime = 0


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
    ciphertexts.append(encrypt(i.upper()))

# tester
for trialNum in range(settings['trialNum']):
    # trial data collection setup
    trialData = {
        'cipherID':settings['cipherID'],
        'trialNum':trialNum,
        'data':{}
        }
    # runs for however many ciphertexts
    # trades time for accuracy by running each sub-trial seperatley
    for testCiphertext in ciphertexts:
        with open(settings['wordlistPath']) as wordlist:
            startTime = time.time()
            line = ''
            line = wordlist.readline()
            while line:
                if encrypt(line.upper()) == testCiphertext:
                    trialData['data'].append({
                        'ciphertext': testCiphertext,
                        'cleartext': line, 
                        'time': time.time()-startTime
                        })
                    break
    with open(settngs['outputPath']) as output:
        json.dump(trialData,output)





