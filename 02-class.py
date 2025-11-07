class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am a {self.age} year old {self.gender}.")

    

human = Human("aman",20,"male");
human.introduce();

human2 = Human("radha",19,"female");
human2.introduce();