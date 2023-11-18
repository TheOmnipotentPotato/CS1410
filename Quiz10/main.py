import doctor
import lunch

if __name__ == "__main__":
    dr = doctor.Doctor(10)
    l = lunch.Lunch("Pizza Hut")

    print(dr.display())
    print(l.display())


