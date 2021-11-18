import os, csv, shutil

def read_in_months():
    activity_list = []
    months = {}
    # Replace this filepath with the filepath to the csv that contains the activity months.
    with open('/Users/clairemcnamara/Desktop/Research/Code/activity.csv','rt') as f:
        data = csv.reader(f)
        index = 0
        for row in data:
            if index > 0:
                month_list = row[0].split(';')
                month_list.pop(0)
                subindex = 1
                activity_name = month_list[0]
                activity_name = activity_name.replace(" ", "")
                months[activity_name] = []
                for i in range(0, len(month_list)):
                    if i == 0:
                        activity_list.append(month_list[0])
                    elif subindex == i and month_list[i] != '':
                        months[activity_name].append(month_list[i])
                        subindex = subindex + 4
            index = index + 1
    return activity_list, months

if __name__ == "__main__":
    _, months = read_in_months()  

    # Replace the directory with the directory that contains the videos in the original format.
    directory = "/Users/clairemcnamara/Desktop/Research/Processed_Notated_Datasets/"
    # Replace the output_directory with the directory you wish the sorted videos to be placed in.
    output_directory = "/Users/clairemcnamara/Desktop/Research/Processed_Notated_Datasets_Final/"

    # Creates all the sub directories for the vidoes to be copied into.
    for activity in months:
        tmp_output_directory = output_directory + activity + "/"
        if not os.path.exists(tmp_output_directory):
            os.makedirs(tmp_output_directory)

        younger = tmp_output_directory + "younger" + "/"
        if not os.path.exists(younger):
            os.makedirs(younger)

        for month in months[activity]:
            month_tmp_output_directory = tmp_output_directory + month + "/"
            if not os.path.exists(month_tmp_output_directory):
                os.makedirs(month_tmp_output_directory)

    # Places the vidoes into the correct subdirectories.
    for filename in os.listdir(directory):
        subdir = os.path.join(directory, filename)
        if not ".DS_Store" in filename:
            tmp_output_directory = output_directory + filename + "/"

            if not ".DS_Store" in filename:
                for subfilename in os.listdir(subdir):
                    filename_parts = subfilename.split('_')
                    month = filename_parts[2]

                    if not ".DS_Store" in subfilename:
                        if int(month) < int(months[filename][0]):
                            month_tmp_output_directory = tmp_output_directory + "younger" + "/"
                        elif int(month) >= int(months[filename][len(months[filename]) - 1]):
                            month_tmp_output_directory = tmp_output_directory + months[filename][len(months[filename]) - 1] + "/"
                        else:
                            found = False
                            for i in range(0, len(months[filename]) - 1):
                                if int(month) == int(months[filename][i]):
                                    month_tmp_output_directory = tmp_output_directory + months[filename][i] + "/"
                                    found = True
                                elif int(month) < int(months[filename][i + 1]):
                                    month_tmp_output_directory = tmp_output_directory + months[filename][i] + "/"
                                    found = True
                                if found:
                                    break
                    
                    input = directory + filename + "/" + subfilename
                    output = month_tmp_output_directory + subfilename
                    shutil.copy(input, output)
                                    