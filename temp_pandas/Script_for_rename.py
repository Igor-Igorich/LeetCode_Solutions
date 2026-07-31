import os

def rename_pattern(
        directory: str,
        old_pattern: str,
        new_pattern: str
        ) -> None:
    
    """Renaming files containing a specific pattern

    Args:
        directory (str): path to the file folder
        old_pattern (str): component of the name to changen
        new_pattern (str): new component of the name
    """
    
    for filename in os.listdir(directory):
        if old_pattern in filename:
            new_filename = filename.replace(old_pattern, new_pattern, 1)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            os.rename(old_path, new_path)
            print(f'Renamed {filename} to {new_filename}')


dir = input('Enter directory: ')
old = input('Enter old pattern: ')
new = input('Enter new pattern: ')

rename_pattern(directory= dir, old_pattern= old, new_pattern= new)