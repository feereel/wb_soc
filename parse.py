import sys
import csv
import logging
import argparse

def read_process_csv(csv_file_path: str) -> dict[str, list[dict]]:
    data = {}
    try:
        with open(csv_file_path, 'r') as csvf:
            csv_reader = csv.DictReader(csvf)
            for row in csv_reader:
                if row['process.pid'] in data:
                    data[row['process.pid']] += [row]
                else:
                    data[row['process.pid']] = [row]
    except Exception as e:
        logging.error('Failed to process data', exc_info=e)
        exit(1)
    return data

def write_process_csv(csv_data: dict[str, list[dict]], output: str = '') -> None:
    try:
        if output:
            csvf = open(output, 'w')
        else:
            csvf = sys.stdout
        fieldnames = ["@timestamp",
                      "process.command_line",
                      "process.executable",
                      "process.working_directory",
                      "process.pid",
                      "process.parent.pid",
                      "process.user.id",
                      "process.parent.command_line"]
        writer = csv.DictWriter(csvf, fieldnames)
        writer.writeheader()
        for data in csv_data.values():
            for row in data:
                writer.writerow(row)
        csvf.close()
    except Exception as e:
        logging.error('Failed to process data', exc_info=e)
        exit(1)

def set_parent_command(csv_data: dict[str, list[dict]]) -> dict[str, list[dict]]:
    for process_pid, data in csv_data.items():
        for row_data in data:
            parent_pid = row_data['process.parent.pid']
            if parent_pid in csv_data and csv_data[parent_pid]:
                parent_row = csv_data[parent_pid][0]
                row_data['process.parent.command_line'] = parent_row['process.command_line']
            else:
                row_data['process.parent.command_line'] = ''
            logging.info(f"{process_pid} -> {parent_pid} with command {row_data['process.parent.command_line']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-log',
                        '--loglevel',
                        default='error',
                        help='Provide logging level.' )
    parser.add_argument('-f',
                        '--file',
                        help='CSV file.')
    
    parser.add_argument('-o',
                        '--output',
                        default='',
                        help='Output file. Default is stdout.')

    args = parser.parse_args()

    logging.basicConfig( level=args.loglevel.upper() )
    
    csv_data = read_process_csv(args.file)
    set_parent_command(csv_data)
    write_process_csv(csv_data, args.output)
    