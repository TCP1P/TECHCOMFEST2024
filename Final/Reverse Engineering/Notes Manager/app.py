#!/usr/bin/python

def main():
    print("What is the login credential for the Notes Manager application in the pre-configured device?")
    print("Answer Format: username:password")
    ans1 = input("Answer: ")
    if ans1 != "N1n0:iloveyou":
        print("Better luck next time!")
        exit()

    print("What is the content of Secret Note #1?")
    print("Answer Format: 32-hex-characters")
    ans2 = input("Answer: ")
    if ans2 != "d17f59e0eb5016d76f7de6f87e615603":
        print("Better luck next time!")
        exit()

    print("What is the content of Secret Note #2?")
    print("Answer Format: 32-hex-characters")
    ans3 = input("Answer: ")
    if ans3 != "c38ceb3ecfde894861e708f7a817f72c":
        print("Better luck next time!")
        exit()

    print("Congrats!")
    print("TCF2024{C0ngr4tul4ti0n_F0r_P4ss1ng_Y0ur_CXMAP_Ex4m_DM_M3_F0r_Y0uR_C3rt1fic4ti0n}")

if __name__ == "__main__":
    main()