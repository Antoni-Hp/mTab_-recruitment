import zad_1
import zad_2
import zad_3
import zad_4


def condition(score):
    if score is True:
        print("test PASS")
    else:
        print("test FAIL")


condition(zad_1.Main().start())
condition(zad_2.Main().start())
condition(zad_3.Main().start())
condition(zad_4.Main().start())
