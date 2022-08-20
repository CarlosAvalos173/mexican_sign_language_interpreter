# base app for generating the dataset
# Authors: Agustin Zavala, Jose Avalos, Roberto Higuera, Jesus Quiñones


def generate_dataset():
    print("generating the dataset")
    pass


def train_model():
    print("training the model")
    pass


def main():
    option = input("1.- generate the dataset\n2.- train the model\n3.- exit\n>> ")

    while option != "3":
        if option == "1":
            generate_dataset()
        elif option == "2":
            train_model()
        else:
            print("invalid option")
        option = input("1.- generate the dataset\n2.- train the model\n3.- exit\n>> ")


if __name__ == "__main__":
    main()
