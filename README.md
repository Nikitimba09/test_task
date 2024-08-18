#Replace Values Script

#Description

This Python script allows you to replace strings in a text file based on key-value pairs specified in the configuration file. The script performs the replacements and outputs the changed lines to the console, sorting them by the number of replacements (starting with the largest).

#Requirements

To run the script, Python version 3.6 or higher is required.

#Download

* Clone the repository or download the script:

```
git clone https://github.com/Nikitimba09/test_task.git
cd replace-values-script
```

#Usage

###1. Create a configuration file

The configuration file must contain replacement pairs in the key=value format, where:

* key is the value that needs to be replaced.
* value — the value to replace with.

*Example configuration file (config.txt):*
***
````
a=z  
b=y  
c=x
````
###2. Create a text file for processing:  
The text file must contain the lines of text in which the replacements will be made.

*Example text file (input.txt):*
***
````
jgrebk6hnae  
cnhjrfyjvth3nxr  
b#sjcf_ansvo!  
djf#aemfaaofna%  
````

###3. Run the script:
Use the command below to run the script, specifying the names of the configuration and text files as command line arguments:

````
python3 main.py config.txt input.txt
````

##*Result:*

The changed lines will be output to the console, sorted by the number of replacements.