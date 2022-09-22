import example

student1 = example.Student("Lojze", 12345, 1)
student1.oceni("Elektrotehnika", 10)
student1.napreduj()

fakulteta_fe = example.Fakulteta()
fakulteta_fe.vpis(student1)

print(fakulteta_fe.studenti)