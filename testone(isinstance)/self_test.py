rclass Reminder():
    def ad(self,x,y):
        result = x+y
        return result

    def minus(self,x,y):
        result = x-y
        return result

    def div(self,x,y):
        result = x/y
        return result

    def rais(self,x,y):
        result = x/y
        return result

    def po(self,x,y):
        result = pow(x,y)
        return result

    def create_num_list(self, length):
        list = [x for x in range(length)]
        return list

    def addo(self, x, y):
        number_types = (int , long, float,complex)
        if isinstance (x, number_types) and isinstance(y , number_types):
            return x+y
        else:
            raise ValueError("there is an error please recheck")
