class my_string():
    table = {
            'A' : 90,
            'B' : 91,
            'C' : 92,
            'D' : 93,
            'E' : 94,
            'F' : 80,
            'G' : 81,
            'H' : 82,
            'I' : 83,
            'J' : 83,
            'K' : 84,
            'L' : 70,
            'M' : 71,
            'N' : 72,
            'O' : 73,
            'P' : 74,
            'Q' : 60,
            'R' : 61,
            'S' : 62,
            'T' : 63,
            'U' : 64,
            'V' : 50,
            'W' : 51,
            'X' : 52,
            'Y' : 53,
            'Z' : 54
            }

    def __init__(self, string):
        self.string = string
        self.prepared_str = ""
        self.encoded_str = ""
        self.decoded_str = ""

    def prepare(self):
        self.prepared_str = self.string.upper().replace(" ","")
    
    def char_exists(self, char_from_string):
        if char_from_string in my_string.table.keys():
            char_code = my_string.table[char_from_string]
            return char_code
        else:
            print("¡Cuidado! Esto no es una letra: " + str(char_from_string))
            exit()

    def encode(self):
        self.prepare()
        for char in self.prepared_str:
            self.encoded_str += str(self.char_exists(char))
        return self.encoded_str

    def pair_exists(self, pair_from_string):
        if pair_from_string in my_string.table.values():
            keys_list = [key  for (key, value) in my_string.table.items() if value == pair_from_string]
            key_code = keys_list[0]
            return key_code
        else:
            print("¡Cuidado! Esta no es una combinación válida: " + str(pair_from_string))
            exit()

    def decode(self):
        for pair in range(0, len(self.string), 2):
            print(self.string[pair:pair + 2])
            self.decoded_str += str(self.pair_exists(int(self.string[pair:pair + 2])))

        return self.decoded_str


#cadena_inicial = "hola mundo"
cadena_inicial = "827370907164729373"
cadena = my_string(cadena_inicial)
# print("Cadena introducida: ", str(cadena_inicial))
# print("Cadena codificada: ", str(cadena.encode()))
print("Cadena decodificada: ", str(cadena.decode()))
