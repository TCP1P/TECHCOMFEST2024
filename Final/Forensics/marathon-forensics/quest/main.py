import time

def verify(index ,question, answer):
    while True:
        result = input(f'\n[{index}/5] {question} : ')
        print("Your input : ", result)
        if result != f'{answer}':
            print("Wrong answer😵‍💫, please try again!")
            time.sleep(3)
        else:
            print("Congratulation, you can answer the question correctly!")
            time.sleep(1)
            break

def header():
    head = """
            $$\      $$\                           $$\    $$\                                         
            $$$\    $$$ |                          $$ |   $$ |                                        
$$$$\       $$$$\  $$$$ |$$$$$$\  $$$$$$\ $$$$$$\$$$$$$\  $$$$$$$\  $$$$$$\ $$$$$$$\        $$$$\     
\____|      $$\$$\$$ $$ |\____$$\$$  __$$\\____$$\_$$  _| $$  __$$\$$  __$$\$$  __$$\       \____|    
$$$$\       $$ \$$$  $$ |$$$$$$$ $$ |  \__$$$$$$$ |$$ |   $$ |  $$ $$ /  $$ $$ |  $$ |      $$$$\     
\____|      $$ |\$  /$$ $$  __$$ $$ |    $$  __$$ |$$ |$$\$$ |  $$ $$ |  $$ $$ |  $$ |      \____|    
            $$ | \_/ $$ \$$$$$$$ $$ |    \$$$$$$$ |\$$$$  $$ |  $$ \$$$$$$  $$ |  $$ |                
$$$$$$$$\   \__|     \__|\_______\__|     \_______|$$\___/\__|  \__|\______/\__| $$\_|$$$$$$\   $$\   
$$  _____|                                         \__|                        $$$$ |$$$ __$$\$$$$ |  
$$ |   $$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$\  $$$$$$$\$$\ $$$$$$$\ $$$$$$$\       \_$$ |$$$$\ $$ \_$$ |  
$$$$$\$$  __$$\$$  __$$\$$  __$$\$$  __$$\$$  _____$$ $$  _____$$  _____|        $$ |$$\$$\$$ | $$ |  
$$  __$$ /  $$ $$ |  \__$$$$$$$$ $$ |  $$ \$$$$$$\ $$ $$ /     \$$$$$$\          $$ |$$ \$$$$ | $$ |  
$$ |  $$ |  $$ $$ |     $$   ____$$ |  $$ |\____$$\$$ $$ |      \____$$\         $$ |$$ |\$$$ | $$ |  
$$ |  \$$$$$$  $$ |     \$$$$$$$\$$ |  $$ $$$$$$$  $$ \$$$$$$$\$$$$$$$  |      $$$$$$\$$$$$$  $$$$$$\ 
\__|   \______/\__|      \_______\__|  \__\_______/\__|\_______\_______/       \______\______/\______|
                                                                                                      
                                                                                                      
=======================================================================================================
=======================================================================================================

    """
    print(head)

def announcement():
    print("Welcome to the marathon forensics 101!", end="")
    input()
    input("press enter to continue ...")

def enrtypoint():
    print("""
=======================================================================================================
                                            ENTRY POINT
=======================================================================================================

    Before we start our jurney, i want to make sure that you are ready for this.
    Please retrieve all the file from protected archive.
    The file itself only \033[33mcontains 2 emoji per file.\033[39m
    I am not sure you can crack this archive file, but somehow I believe you can do it.
    If you already retrieve the file, please enter it below.
    Make sure you input it in correct order.

=======================================================================================================
=======================================================================================================""")
    
    verify(0, "Enter the emoji", "😁😀😍🤩😛😫😰🙂📦😂😋👍😃😂😴🥲🤩😍😋🤨🤣😂👍😋")

def challenge():
    print("""
=======================================================================================================
                                            CHALLENGE
=======================================================================================================
    
    So here is the story, there is a hacker that want to hack someone pc.
    
    1. The attacker send a phishing email to victim.
    2. The email contains an archive file that contains a malicious file.
    3. The malware itself will download a script from attacker's server and execute it.
    
    The police somehow caught this attacker and get his pc, Please help the police
    to investigate it. You can use all of emoji to unlock the archived file that contains
    attacker pc image folders. 
    

    \033[33mNote : Be careful with the malicious file, don't get your pc hacked\033[39m

=======================================================================================================
=======================================================================================================""")
    
    verify(1, "What is attacker and victim email address (format : attacker@example.xyz:victim@example.xyz)", "apelnotahacker101@gmail.com:s3buahapel@gmail.com")
    verify(2, "To verify the attachment you got is right, please input md5sum of the file (format : 83f9714e58283d82843f8669dbb3524b)", "67f30fe89067ea88ae45a34ec4ece1d1")
    verify(3, "What is the document password?", "secret")
    verify(4, "Where is the script will be stored in victim device? (format : %PATH%/exmaple.bat)", "%TEMP%/201ae9c7d15006574ceb3edd0b972e0a1d3f9437.vbs")
    verify(5, "What is the message showed when attacker successfully attack victim device? (format : message here 1e2917dff)", "your pc has been hacked b8c7fdfc3c2a710")

def flag():
    print("""
=======================================================================================================
                                            FLAG
=======================================================================================================
""")
    while True:
        for i in range(0xf):
            try:
                flag = "TCF2024{9cef58a96b1350867f17bfcc9e984bae2bf7590f}"
                print(f'\033[32m[{i:x}]  Here is your flag : {flag} [{i:x}]', end='\r')
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('bye')
                exit()
        for i in range(0xf):
            try:
                print(f'[{i:x}]  h3Re 1s y0uR fL4g : {flag} [{i:x}]', end='\r')
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('bye')
                exit()
        for i in range(0xf):
            try:
                print(f'[{i:x}]  hEr3 i5 yOUr Fl4G : {flag} [{i:x}]', end='\r')
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('bye')
                exit()

if __name__ == "__main__":
    header()
    announcement()
    enrtypoint()
    challenge()
    flag()

