while True:
    x = str(input('prefer to metric calcuting or impercial: '))

    if x == 'metric':

        w = float(input("enter your weight float form and kilogram format: "))
        h = float(input("enter your height float form and meter format: "))

        total_metric_bmi = w / h ** 2

        print(f'your total metric bmi is {total_metric_bmi}')

        if total_metric_bmi < 18.5:
            print("your bmi  fall within the underweight range.")
        elif 18.5 < total_metric_bmi < 24.9:
            print("falls within the normal or Healthy Weight range.")
        else:
            print("falls within the overweight range.")

    elif x == 'impercial':
        w = float(input("enter your weight float form and kilogram format: "))
        h = float(input("enter your height float form and meter format: "))

        new_w = w * 2.20462 / 1
        new_h = h * 39.3701 / 1

        total_impercial_bmi = new_w * 703 / new_h ** 2

        print(f'your total impercial bmi is {total_impercial_bmi}')
        if total_metric_bmi < 18.5:
            print("your bmi  fall within the underweight range.")
        elif 18.5 < total_metric_bmi < 24.9:
            print("falls within the normal or Healthy Weight range.")
        else:
            print("falls within the overweight range.")

    else:
        print('somethin went wrong! try again!')

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue

    else:
        print("Goodbye")
        break
