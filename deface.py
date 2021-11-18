import os, csv

def read_in_maskless():
    maskless = []
    # Replace this path to wherever you have housed the list of maskless vidoes.
    with open('/Users/clairemcnamara/Desktop/Research/Code/mask_list.csv','rt') as f:
        data = csv.reader(f)
        for row in data:
          maskless.append(row[0])
    return maskless

def anonymise_video(filename):
    print(filename)
    os.system("deface " + filename)
    os.remove(filename)

if __name__ == "__main__":
    maskless = read_in_maskless()
    
    # Replace this directory with the one that you wish to house the anonymised videos.
    directory = "/Users/clairemcnamara/Desktop/Research/Processed_Notated_Datasets_Final_Anonymised/"
    for filename in os.listdir(directory):
        if filename != '.DS_Store':
            subdir = os.path.join(directory, filename)
            for subfilename in os.listdir(subdir):
                if subfilename != '.DS_Store':
                    subsubdir = os.path.join(subdir, subfilename)
                    for subsubfilename in os.listdir(subsubdir):
                        if subfilename != '.DS_Store':
                            # If just anonymising the videos without the child wearing a mask
                            # parts = subsubfilename.split('_')
                            # if parts[1] in maskless:
                            #     anonymise_video(os.path.join(subsubdir, subsubfilename))

                            # To anonymise every video
                            if "anonymized" not in subsubfilename:
                                anonymise_video(os.path.join(subsubdir, subsubfilename))