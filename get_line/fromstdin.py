"""fromstdin - Training and Testing Framework
Usage: fromstdin.py [options] <input>

Options:
    --text=<textmodel>         Text model [default: text.txt]
    --features=<features>      Features model [default: features.txt]
    --test=<testset>           Testing set [default: testset.txt]
    --vectorizer=<vectorizer>  The vectorizec [default: vector.txt]

Read data from <input> file. Use "-" for reading from stdin.
"""
import sys

def main(fname, text, features, test, vectorizer):
    if fname == "-":
        f = sys.stdin
    else:
        f = open(fname)
    process(f, text, features, test, vectorizer)
    print ("main func done")

def process(f, text, features, test, vectorizer):
    print ("processing")
    print ("input parameters", text, features, test, vectorizer)
    print ("reading input stream")
    for line in f:
        print (line.strip("\n"))
    print ("processing done")


if __name__ == "__main__":
    from docopt import docopt
    args = docopt(__doc__)
    print (args)
    infile = args["<input>"]
    textfile = args["--text"]
    featuresfile = args["--features"]
    testfile = args["--test"]
    vectorizer = args["--vectorizer"]
    main(infile, textfile, featuresfile, testfile, vectorizer)
