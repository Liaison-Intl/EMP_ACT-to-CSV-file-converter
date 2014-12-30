from optparse import OptionParser
import ACT_2014_2015_config
import csv

def run(options):
    """
    Runs script
    :return:
    """
    # Parse args
    input_file_path = options['input_file_path']
    output_file_path = options['output_file_path']

    # Load layout config
    file_layout = ACT_2014_2015_config.layout

    # Open source ACT file, load into memory
    with open(input_file_path, ) as input_file:
        input_file_data = input_file.readlines()

    # Convert lines
    converted_records = []
    for input_record in input_file_data:

        converted_record = []

        for field in file_layout:
            converted_record.append(input_record[field['start_position']:field['end_position']+1])

        converted_records.append(converted_record)

    # Save to new file
    with open(output_file_path, 'wb') as output_file:
        write_file = csv.writer(output_file, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        header_row = [y['field'] for y in file_layout]
        write_file.writerow(header_row)
        write_file.writerows(converted_records)

def convert_line(fixed_width_text, splits):
    """
    :param line: non-delimited text
    :param splits: list of dicts {field, start_position, end_position}
    :return: comma delimited text
    """

    delimited_text = ""

    for split in splits:
        pass

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-i", "--input",
                      dest="input_file_path", metavar="/path/to/file",
                      action="store", type="string",
                      help="Specify ACT source file to convert")

    parser.add_option("-o", "--output",
                      dest="output_file_path", metavar="/path/to/file",
                      action="store", type="string",
                      help="Specify file name and location of converted output file")

    (options, args) = parser.parse_args()
    run_options = vars(options)

    run(run_options)