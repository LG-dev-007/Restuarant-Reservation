class SetUpDay:
    @staticmethod
    def setup_tables(table_list, num_t):
        x: int = 0
        while x < num_t:
            table_list.append("0")
            x += 1

    def __init__(self, date, h_t, num_t2, num_t4, num_t6, num_t8):
        self.date = date
        self.high_traffic = h_t
        self.t2 = []
        self.t4 = []
        self.t6 = []
        self.t8 = []
        # Fill the List
        self.setup_tables(self.t2, num_t2)
        self.setup_tables(self.t4, num_t4)
        self.setup_tables(self.t6, num_t6)
        self.setup_tables(self.t8, num_t8)
