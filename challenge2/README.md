# Project Definition:

The project I have planned to start is a Python service that works as a command-line tool or an argument-based tool and performs various tasks. For now, I have considered four methods or four capabilities for this service, two of which are relatively simple and the other two are more challenging. To write this service, you can use various argument-based packages such as argparse.

# Methods:

1. The first thing this service should do is to take a list of numbers and separate the even and odd numbers and return the output as two separate lists, one for even numbers and one for odd numbers. The -l or --list option is the desired option for this Python service.

2. The second method of this service is to take a string as input and perform certain specified changes on this string and return the edited input as output. The option for this method is -s or --string.

3. The third method is to obtain the public IP and internal IP of the system and the network in which this service is executed and return it as output. The option for this method is -i or --ip.

4. The fourth method, which is the most challenging method, takes an email as input and selects the social network that should be displayed in the option and checks whether this email has an active account on this social network or not. The option for this method is -e or --email.

#Requirements:

1. All methods should be written in separate files and the main code should be placed in the main file so that the service can be executed by running the main file.

2. All packages should be listed in a separate requirements file.

3. The code should be run in a virtual environment by creating an env for Python version 9 or 10 (preferably 9) and after installing the packages, the code should be executed properly in it.

4. The service should have a complete -h or --help option so that by running python main --help, all options and their guides can be seen in detail.

