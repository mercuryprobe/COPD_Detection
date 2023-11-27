import os

directory = 'C:/Users/mercu/OneDrive/Desktop/College/sem5/ML/Assignments/Project'

categories = ['noisy', 'timeshifted', 'timestretched', 'pitchshifted']
features = ['spectrograms', 'mfcc', 'chroma', 'cens']

for category in categories:
    for feature in features:
        folder = category + '_' + feature
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
