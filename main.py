from datetime import datetime, date, time

from PIL import Image


from application.salary import calculate_salary 
from application.db.people import get_employees 





if __name__ == '__main__':

    print(datetime.now())

    result = calculate_salary()
    print(result)


    result2 = get_employees()
    print(result2)


    image = Image.open('me.JPEG')

    new_size = (1000, 1000)

    resized_image = image.resize(new_size)


    resized_image.save('resizedMe.jpg')

    print('Image was successfuly ghanged and saved!')