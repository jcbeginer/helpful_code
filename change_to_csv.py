import re

def txt_to_csv(input_filepath, output_filepath):
    with open(input_filepath, 'r') as txt_file:
        lines = txt_file.readlines()

    # Define a regex pattern to extract the necessary data
    #pattern = r'(\d+월 \d+) (\d+):(\d+):(\d+) .+ mptcp path index : (\d+), cwnd: (\d+), cwnd - queued: (\d+)'
    pattern = r'(\d+월 \d+) (\d+):(\d+):(\d+) .+ mptcp path index : (\d+), cwnd: (-?\d+), cwnd - queued: (-?\d+)'
    # Create a CSV header
    csv_data = ['Date,HH,MM,SS,Path_Index,CWND,CWND_Queued\n']

    for line in lines:
        match = re.search(pattern, line)
        if match:
            date = match.group(1)
            hh = match.group(2)
            mm = match.group(3)
            ss = match.group(4)
            path_index = match.group(5)
            cwnd = match.group(6)
            cwnd_queued = match.group(7)
            
            cwnd = int(cwnd)
            cwnd_queued = int(cwnd_queued)
          
            csv_data.append(f"{date},{hh},{mm},{ss},{path_index},{cwnd},{cwnd_queued}\n")

    with open(output_filepath, 'w') as csv_file:
        csv_file.writelines(csv_data)

# Provide the appropriate file paths
input_txt_file = "./231010_iperf_3_MPTCP.txt"
output_csv_file = "output_csv_file.csv"

txt_to_csv(input_txt_file, output_csv_file)
