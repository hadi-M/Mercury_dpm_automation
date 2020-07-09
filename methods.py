from ipdb import set_trace as st
import itertools
import pandas as pd
import numpy
import os


def read_U0_epsilon0_files():
    with open("grid_U_0.txt", "r") as file_obj:
        U0 = file_obj.read()
    U0_list = U0.split("\n")

    with open("grid_epsilon_0.txt", "r") as file_obj:
        epsilon0 = file_obj.read()
    epsilon0_list = epsilon0.split("\n")

    return U0_list, epsilon0_list


def create_and_write_csv_if_not_exist(U0_list, epsilon0_list, file_name):
    if file_name not in os.listdir():
        # st()
        cartesian = list(itertools.product(*[U0_list, epsilon0_list, ["0"], ["0"], ["NO"]]))
        df = pd.DataFrame(cartesian, columns=["U_0", "epsilon_0", "u_0", "v_y", "Done?"])
        df.to_csv(file_name)

    # return df


def add_single_row_one_file(df):
    # st()
    files_content_dict = df[df["v_y"] == "0"].iloc[0].drop("v_y").to_dict()

    for key, value in files_content_dict.items():
        file_name = "single_" + key + ".txt"
        with open(file_name, "w") as file_obj:
            file_obj.write(value)
    

def get_next_U0_epsilon0(file_name):
        # st()
        df = pd.read_csv(file_name)
        not_calculated_rows = df[df["Done?"] == "NO"]
        is_all_calculated = (len(not_calculated_rows) == 0)
        if is_all_calculated:
            return None, True
        else:
            next_to_calculate = not_calculated_rows.iloc[0]
            return next_to_calculate[["U_0", "epsilon_0"]], False


if __name__ == "__main__":
    U0_list, epsilon0_list = read_U0_epsilon0_files()
    df = create_and_write_csv_if_not_exist(U0_list, epsilon0_list, file_name)
    add_single_row_one_file(df)
    print(df)