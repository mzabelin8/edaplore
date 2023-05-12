class Type:
    def __init__(self, data, column_name):
        self.data = data

        self.column_name = column_name
        self.type_name = ''

        self.count_values = 0
        self.miss_values = 0

