import re


# Solution №1
class FileNameExtractor:
    @staticmethod
    def extract_file_name(file):
        s = file.split('_')[0] + '_'
        s1 = file.replace(s, '')
        s2 = s1.split('.')[2]
        return s1.replace(s2, '')[:-1]


launch = FileNameExtractor()
print(launch.extract_file_name(file="1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))


# Solution №2
# class FileNameExtractor:
#     @staticmethod
#     def extract_file_name(dirty_file_name):
#         return re.match(r"\d+_(.+?\..+?)\.", dirty_file_name).group(1)
