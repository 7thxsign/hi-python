import threading
import time

def walk_the_dog(first, last):
    time.sleep(8)
    print(f"Walking the dog {first} {last} is complete.")

def take_out_trash():
    time.sleep(2)
    print("Taking out the trash is complete.")

def get_mail():
    time.sleep(4)
    print("Getting mail is complete.")

chore1 = threading.Thread(target=walk_the_dog, args=("Bondhu", "Raja"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print('All done!')