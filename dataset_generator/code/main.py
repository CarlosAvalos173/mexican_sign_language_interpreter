# base app for generating the dataset
# Authors: Agustin Zavala, Jose Avalos, Roberto Higuera, Jesus Quiñones

import os
import shutil
from modules.data_loader import load_data_numpy
from modules.neural_network_training import train_nn


def copy_original_dataset() -> None:
    for folder in os.listdir("dataset_generator/original_dataset/data"):
        # create folder if it doesn't exist
        if not os.path.exists("dataset_generator/dataset/" + folder):
            os.mkdir("dataset_generator/dataset/" + folder)
        number_of_existing_files = len(
            os.listdir(f"dataset_generator/dataset/{folder}")
        )
        for file in os.listdir(f"dataset_generator/original_dataset/data/{folder}"):
            number_of_existing_files += 1
            shutil.copyfile(
                src=f"dataset_generator/original_dataset/data/{folder}/{file}",
                dst=f"dataset_generator/dataset/{folder}/{number_of_existing_files}.csv",
            )


def generate_dataset() -> None:
    print("generating the dataset")
    shutil.rmtree("dataset_generator/dataset")
    os.mkdir("dataset_generator\dataset")

    # check if videos folder exists
    if os.path.exists("dataset_generator\\videos"):
        print("Generating txt from videos")

    if os.path.exists("dataset_generator\original_dataset\data"):
        print("Copying original dataset")
        copy_original_dataset()

    x_train, y_train = load_data_numpy("dataset_generator/dataset")


def save_tflite_model() -> None:
    import tensorflow as tf

    converter = tf.lite.TFLiteConverter.from_keras_model(
        tf.keras.models.load_model("dataset_generator\\best_model.h5")
    )
    tflite_model = converter.convert()

    with open("dataset_generator\\model.tflite", "wb") as f:
        f.write(tflite_model)


def main() -> None:
    option = input("1.- generate the dataset\n2.- train the model\n3.- exit\n>> ")

    while option != "3":
        if option == "1":
            generate_dataset()
        elif option == "2":
            train_nn()
            save_tflite_model()
        else:
            print("invalid option")
        option = input("1.- generate the dataset\n2.- train the model\n3.- exit\n>> ")


if __name__ == "__main__":
    main()
