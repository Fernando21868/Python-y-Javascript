import csv
import os

os.makedirs('./Python/headerRemoved', exist_ok=True)

for csv_file_name in os.listdir('./Python'):
    if not csv_file_name.endswith('.csv'):
        continue

    print('Removing header from ' + csv_file_name+'...')

    # TODO: Read the CSV file in (skipping first row)
    csv_rows = []
    csv_file_obj = open('./Python/'+csv_file_name)
    reader_obj = csv.reader(csv_file_obj)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
    csv_file_obj.close()

    # TODO: Write ou the CSV file
    csv_file_obj = open(os.path.join(
        './Python/headerRemoved', csv_file_name), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()
