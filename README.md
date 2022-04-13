TOPIC: FREQUENCY ANALYSIS APPLICATION

DESCRIPTION: 
Frequency analysis is based on the fact that, in any given stretch of written language, certain letters and combinations of letters occur with varying frequencies. This application help crypto analyst to make frequency analysis on cipher text.

This Application has no GUI, it is a command line application and takes one arguments (cipher.txt) as input.

After application run it analyze cipher.txt and give statistic of chars at the same screen.
it then displays an Option:
1) Take replace rule
2) Exit

If option 1 will be typed then system get replacement rule for analysis. Format of rule looks like CSV like input for example (M:a,A:b,N:c,U:d,S:e,C:f, (So on...))

Input format description:
1. input pairs should be separated by comma ","
2. Cipher Text Char:Plain Text Char

After input given according to given input all cipher text chars will be replaced by given rule. So 
M replaced as a , A replaced by b and so on..

LANGUAGE
This program is written in Python Language

STEPS
1. PASS an arguement of file_name to the program file
2. The application READS the content of the file and save it in a variable
3. The app ANALYSE the frequency of each letter in the Cipher Text and Return the Statistic
4. The app GET user input for the Replacement Rule
5. The app VERIFY the replacement rule to ensure it follows the format for the replacement rule
6. The app EXTRACTS the Cipher Text Char and Plain Text Char pairs from the replacement rule
7. The CipherText is DECRYPTED following the replacement rule
8. The result of the Analysis and Plain Text is DISPLAYED to the screen.

SETUP

1. Install Python 3.9 on your Machine
2. Creat a Folder
3. Save the files analysis.py and .txt file in the same folder created
4. Open your command line interface by searchin cmd, or Windows + R, then search cmd
5. cd to the Folder location path
6. Run command 'python -m analysis [file_name.txt]' to RUN app

