import argparse

def main(args)
    parser = argparse.ArgumentParser(description="Crack ciphers\
            based on a dictionary attack")
    parser.add_argument("cipher",option="store",type="str")
    parser.add_argument("--dict",option="store",type="str",
            default="/usr/share/dict/cracklib-small")

    results = parser.parse_args(args)

