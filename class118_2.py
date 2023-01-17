# class greeting:
#     def sayhello(self):
#         print("Hello!")
#
# x = greeting()
# x.sayhello()

class gr:
    def saynice(self):
        self.sayhello()
        print("Nice to meet you!")

    def sayhello(self):
        print("Hello!")

xyz = gr()
xyz.saynice()



class xyz:
    def zero(self):
        self.abc()
        print("ZERO====!")

    def abc(self):
        print("ABC!")

test = xyz()
test.zero()