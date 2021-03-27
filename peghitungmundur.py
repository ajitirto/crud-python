import time

def penghitungMundur(startMinute, startSecond):
    totalSecond = startMinute * 60 + startSecond
    print("Waktu anda : ")
    while totalSecond:
        mins, secs = divmod(totalSecond, 60)
        print(f'{mins:02d}:{secs:02d}', end = "\r")
        time.sleep(1)
        totalSecond-=1
    print("Habis ")
    print("Selesai !")

if __name__ == "__main__":
    penghitungMundur(00,5)