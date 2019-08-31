import zad_2
import zad_4

score_1 = zad_2.Main().start()
if score_1 is True:
    print("test PASS")
else:
    print("test FAIL")

score_2 = zad_4.Main().start()
if score_2 is True:
    print("test PASS")
else:
    print("test FAIL")