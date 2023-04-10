import csv


def save_to_csv(data):

    try:
        file = open('results.csv', 'a', encoding='UTF8', newline='')
        writer = csv.writer(file)
        print(data)
        writer.writerow(data)
        file.close()
        return True
    except Exception as e:
        print(f"exception: {e}")
        return False
