class Student:
    def __init__(self, first_name="", name="", nb_student=0, level=0):
        self.__first_name = first_name
        self.__name = name
        self.__nb_student = nb_student
        self.__nb_credit = 0
        self.__level = level

    def add_credits(self, new_credit):
        if new_credit > 0:
            self.__nb_credit += new_credit
        else:
            print("Erreur : Le nombre de crédits à ajouter doit être supérieur à zéro.")

    def __student_Eval(self):
        if self.__nb_credit >= 90:
            return "Excellent"
        elif self.__nb_credit >= 80:
            return "Très bien"
        elif self.__nb_credit >= 70:
            return "Bien"
        elif self.__nb_credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.__name}")
        print(f"Prénom: {self.__first_name}")
        print(f"Identifiant étudiant: {self.__nb_student}")
        print(f"Niveau: {self.__student_Eval()}")


john_doe = Student(first_name="John", name="Doe", nb_student=145, level=60)


john_doe.add_credits(100)

john_doe.studentInfo()
