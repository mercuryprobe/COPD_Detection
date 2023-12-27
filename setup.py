"""
Set-up the project directory. The script generates the
required folders in the project (current-working) directory
at the time of execution.
"""

import os


def generate_folders():
    directory = os.path.join(os.getcwd(), 'src')
    categories = ['noisy', 'timeshifted', 'timestretched', 'pitchshifted']
    features = ['spectrograms', 'mfcc', 'chroma', 'cens']

    for category in categories:
        for feature in features:
            folder = category + '_' + feature
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)


if __name__ == '__main__':
    generate_folders()