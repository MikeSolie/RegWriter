## Windows Registry Key Writer
This program writes user input, date and time, and the current working directory to the Windows registry. The user can define a subkey and the value to be written to that subkey.

# Requirements
This program was written in Python 3 and uses the following libraries:

`os`
`winreg`
`datetime`

# How to Use
When the program is run, it will prompt the user to input a subkey and a value for that subkey. After the user inputs these values, the program will write the subkey and value to a new key in the Windows registry. The program will also write the date and time of the run and the current working directory to the same key.

# How it Works
The program contains three functions:

`date_time()` stores the current date and time of when the program is run and returns that value.
`pwd()` stores the current working directory and returns that value.
`new_key(key_name, sub_key, value)` creates a new key in the Windows registry using the provided key name and writes the provided subkey and value to that new key.
The `main()` function prompts the user to input a subkey and value for the new key in the registry. It then calls `date_time()` and `pwd()` to get the date/time and current working directory, respectively. Finally, it calls `new_key()` three times: once for the user input subkey and value, and twice more for the date/time and current working directory.

Disclaimer
Editing the Windows registry can cause serious problems if done incorrectly. It is recommended to back up the registry before making any changes. This program should be used with caution and at the user's own risk.

License
This project is licensed under the MIT License. See the LICENSE file for details.
