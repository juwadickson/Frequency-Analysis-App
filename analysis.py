from operator import countOf
import re
import sys
from typing import List, Dict
# This is my second commit
def main() -> None:
    """ Entrypoint of program run as module """

    file_name = read_args() # Save filename from Arguement passed
    try:
        content = read_file(file_name)
        print("Cipher Text :\n")
        print(content)

        """ Analyse the Cipher Text and Give Statistic of Char """
        analysis(content)

        flag = True
        while flag:
            try:
                """ Display an Option Entry to Perform Action Based on User Option Input """
                print("\n\nOption: \n")
                print("1) Take replace rule\n")
                print("2) Exit\n")

                optionValue = int(input("Option> "))

                if optionValue == 1:
                    format_info() # Display the Replacement Rule Format Info

                    """ Verify if replacement rule format is valid"""
                    format = True
                    while format:
                        replacementRule = input("Enter Replacement Rule-> ")
                        
                        pattern = "^([A-Z](:)[a-z](,)?)+"
                        charMapping = {}
                        Arr = []

                        if(re.fullmatch(pattern,replacementRule)):
                            ruleArr = re.split(",",replacementRule) # Create a list of Rule Pairs by removing the comma
                            for rule in ruleArr:
                                ruleSplit = re.split(":",rule) # Get Cipher Text Char and Plain Text Char from the Rule Pairs
                                # Dictionary to check if Cipher Text Char contains all alphabet
                                for letter in ruleSplit:
                                    Arr.append(letter) # Append each letter in the rule pair to check for duplicate value
                            for char in Arr:
                                if countOf(Arr, char) > 1:
                                    print("\n\t*** Invalid Replacement Rule ***\n")
                                    print("%s appears more than once"%(char))
                                    format_info()
                                    format = False
                                    flag = True
                                    break
                                else:
                                    # return the mapping after succesful verification
                                    charMapping[ruleSplit[0]] = ruleSplit[1]

                            if(charMapping):
                                """ Check if All Characters have been  Visited in The Replacement Rule"""
                                letterVisited = ""
                                for key in charMapping:
                                    letterVisited += key
                                
                                if check_rule_ispangram(letterVisited) == False:
                                    proceedFlag = True
                                    while proceedFlag:
                                        try:
                                            print("\t*** The Cipher Text Char in Replacement Rule does not contain all Alphabet ***")
                                            print("Option: \n1 to continue with Replacement Rule\n2 to Enter a New Replacement Rule\n3 to exit program ***")
                                            proceed = int(input("Proceed> "))
                                            if proceed == 1:
                                                # Action on replacement rule Begin Here
                                                plainTextContent = ""
                                                for cipherLetter in content:
                                                    if cipherLetter.isspace():
                                                        plainTextContent += cipherLetter
                                                    elif not cipherLetter.isalnum():
                                                        plainTextContent += cipherLetter
                                                    else:
                                                        count = 0
                                                        for key in charMapping:
                                                            plainTextChar = charMapping[key]
                                                            
                                                            if cipherLetter == key:
                                                                plainTextContent += plainTextChar
                                                                break
                                                            else:
                                                                count += 1
                                                        if count == len(charMapping):
                                                            plainTextContent += cipherLetter
                                                            count = 0
                                                """ After Verification of Replacement Rule Perform Action on Cipher Text"""
                                                print("\nCipher Text :\n")
                                                print(content)
                                                analysis(content)
                                                print("\n\nPlain Text: \n\n")
                                                # Plain Text Result of Replacement rule is displayed here
                                                print(plainTextContent)
                                                # Action on replacement rule Ends Here
                                                # ***********************
                                                proceedFlag = False
                                                format = False
                                                flag = True
                                            elif proceed == 2:
                                                proceedFlag = False
                                                format = True
                                            elif proceed == 3:
                                                proceedFlag = False
                                                flag = False
                                                exit()
                                            else:
                                                print("\n*** Invalid Option Selected ***")
                                                proceedFlag = False
                                                format = True
                                        except ValueError:
                                            print("\n\t*** ValueError: Invalid Input, Integer Required ***\n\n")
                                            proceedFlag = False
                                            format = True       

                        else:
                            print("\n\t*** Invalid Replacement Rule ***\n")
                            format_info()
                            format = False
                            flag = True
                        
                        
                elif optionValue == 2:
                    flag = False
                    exit() 

                else:
                    print("\n\t**** Invalid Option Selected ****\n")
                    flag = True

            except ValueError as ve:
                print("\n\t*** ValueError: Invalid Input, Integer Required ***")
                flag = True

    except FileNotFoundError:
        msg = "*** Sorry, the file " + file_name + " does not exist.***\n*** Ensure the file is saved in the same folder as the program file ***"
        print(msg)



def read_args():
    if len(sys.argv) != 2:
        print("Usage: python -m analysis [filename]")
        exit()
    return sys.argv[1]

def read_file(file_name: str):
    with open(file_name,"r") as file_handle:
        return file_handle.read()

def analysis(contents: str):
    letter_analysis = {}
    for letter in contents:
        if(letter.isspace() or letter.isalnum() == False): 
            pass
        else:
            letter_analysis[letter] = contents.count(letter)
    print("\nAnalysis :\n")
    for key,value in letter_analysis.items():
        result = key + "->" + str(value) + ","
        print(result,end=' ')

def format_info():
    print("\n******** REPLACEMENT RULE FORMAT *********\n")
    print("* Cipher Text Char:Plain Text Char.\n* Input pairs should be seperated by a comma\n")
    print("* Cipher Text Char and Plain Text Char should not occur more than once")
    print("* Format: M:a,B:c,C:d .....")
    print("\n******** REPLACEMENT RULE FORMAT *********\n")

""" Function to check if Cipher Text in Replacement Rule contains all alphabet"""
def check_rule_ispangram(str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in str:
            return False
    return True

if __name__ == "__main__":
    main()

