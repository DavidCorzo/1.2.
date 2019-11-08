import yaml
import shutil
import os
from datetime import date


def read_yml(filename='D:/UFM-Cursos/Semestre_2-[Julio-Diciembre_2019]/_____SumaDeCursosUFM1.2____/dir.yml'):
    with open(filename, mode='r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f'{exc} error on opening yml')


def eliminate_current_copy_in_drive(file_to_delete):
    os.remove(file_to_delete)


def sync_to_drive(path_source, path_destination):
    shutil.copy2(path_source, path_destination)


def main():
    master = read_yml()
    master_directories = []
    master_names = []
    for k, v in master.items():
        if 'google_drive' not in str(k):
            master_directories.append(v[0])
            master_names.append(v[1])
        elif 'google_drive' in str(k):
            google_drive = master[k]

    pdfs_in_google_drive = os.listdir(google_drive)

    if str(pdfs_in_google_drive) != str([]):

        # for elimination_in_drive in pdfs_in_google_drive:
        #     dir_elim = google_drive + '/' + elimination_in_drive
        #     print(dir_elim)
        #     eliminate_current_copy_in_drive(dir_elim)

        counter = 0
        for i in master_directories:
            for remote_pdf in pdfs_in_google_drive:
                if master_directories[counter] in remote_pdf:
                    print('master => ',
                          master_directories[counter], 'in remote pdf', remote_pdf)
            counter += 1
    else:
        counter_1 = 0
        # for elimination_in_drive in pdfs_in_google_drive:
        #     dir_elim = google_drive + '/' + elimination_in_drive
        #     print(dir_elim)
        #     eliminate_current_copy_in_drive(dir_elim)

        for directory in master_directories:
            dir_remote_pdf_name = google_drive + \
                '/' + master_names[counter_1] + '.pdf'
            sync_to_drive(master_directories[counter_1], dir_remote_pdf_name)
            counter_1 += 1


if __name__ == "__main__":
    main()
