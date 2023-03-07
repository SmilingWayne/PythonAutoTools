import os

folder_path = 'Contents'
for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    # TODO: Modify this line👇 to find the result you want.
    # TODO: Remember the "."!!!!!

    new_filename = "".join(filename.split(
        '.')[:-1]) + '_new_.' + filename.split('.')[-1]

    new_file_path = os.path.join(folder_path, new_filename)
    os.rename(file_path, new_file_path)
