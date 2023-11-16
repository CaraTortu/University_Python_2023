from os.path import exists

def copy_from_to_number(in_filename: str, out_filename: str) -> None:
    '''
    # This is an awful way to do this. 
    
    infile = open(infilename)
    outfile = open(outfilename, "w")
    i = 1
    for line in infile:
        outfile.write(str(i) + ": "+ line)
        i+=1
    infile.close()
    outfile.close()
    '''
    
    
    # Better implementation
    if not exists(in_filename):
        print(f"ERROR: {in_filename} does not exist.")
        return 

    with open(in_filename) as f:
        contents = f.readlines()

    with open(out_filename, "w") as f:
        for i, line in enumerate(contents):
            f.write(f"{i+1}: {line}")


def main():
    input_file = input("Enter file to read from: ")
    out_file = input("Enter file to write to: ")
    copy_from_to_number(input_file, out_file)


if __name__ == "__main__":
    main()
