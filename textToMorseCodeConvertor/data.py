class Data():
    def __init__(self):
        with open('morse_code.csv', 'r') as file:
            self.data = file.readlines()
        self.data_dict = self.convert_to_dict()

    def convert_to_dict(self):
        data_dict = {}
        for line in self.data:
            data_dict[line.split(',')[0]] = line.split(',')[1].split('\n')[0]
        return data_dict

    def convert_text_to_code(self, input_str):
        morse_code = ""
        for char in input_str:
            try:
                morse_code += f"{self.data_dict[char.upper()]} "
            except KeyError as e:
                morse_code += f"{char} "
        morse_code.replace('\n', '')
        return morse_code
