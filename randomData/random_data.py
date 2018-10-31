import random
import string

class Generate_Random_Data(object):

    def generate_random_correct_email(self):
        x = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=1))
        n = random.randint(4, 12)
        x = x + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        x = x + "@"
        n = random.randint(2, 12)
        x = x + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        x = x + "."
        n = random.randint(2, 5)
        x = x + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))
        return x
