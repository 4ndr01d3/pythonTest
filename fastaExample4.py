#This is a module that provides a FastA file parser. It serves to demonstrate the
#use of exceptions using try, except, raise, and finally

class ParseError(Exception): #Create a new class of exception
    pass

def getFastARecord(f):
    """Retrieves the next FastA record from the already opened file f. 
       Return a tuple (sequence title, sequence string) 
       or None if at end of file. Raises a ParseError"""
    line = f.readline()
    while line.isspace() and line != '':
        line = f.readline()
    if line == '':
        return None
    if not line.startswith('>'):
        raise ParseError("Expected '>' at start of next sequence record. "+
        "Is this a FastA file?")
    title = line[1:-1]
    seq = ""
    line = f.readline()

    #this uses the strict format of a fasta file which requires at least 
    #one empty line between records
    while (not line.isspace()) and (line != ''): 
        seq += line.rstrip()
        line = f.readline()
    return (title, seq)

def getAllFastARecords(path):
    """Attempts to open the file path, the returns a list of all FastA records in the file 
       as tuples of the form (title, sequence string)."""

    try:
        f = open(path, "r");
    except IOError: 
        #here we catch an IOError 
        #(i.e. the file doesn't exist, can't be opened, is corrupt, 
        #we don't have permissions etc...)
        return None

    #from here we know f has been successfully opened, so it must be closed
    try:
        records = []
        rec = getFastARecord(f)
        while rec != None:
            records.append(rec)
            rec = getFastARecord(f)
    except ParseError: #if there is a parse error return no records
        return None
    finally:
        f.close()

    return records
