
"""
Use:
./automation.py T_min T_max
"""

import pyautogui
import methods as me
from ipdb import set_trace as st
import sys
# print(pyautogui.position())
# pyautogui.hotkey('alt', 'tab')
# pyautogui.hotkey('winleft', '2')
# pyautogui.click(673, 138)


def event_loop(file_name):
    
    next_row, is_all_calculated = me.get_next_U0_epsilon0(file_name)
    next_U0 = next_row["U_0"]
    next_epsilon0 = next_row["epsilon_0"]
    st()
    if is_all_calculated:
        return 0

    # me.read_U0_epsilon0_files()
    # me.create_and_write_csv_if_not_exist()
    me.add_first_0_row_single_files()
    me.make_and_run_tutorial_code()
    me.copy_files_and_run_fstatistics()
    me.run_matlab_code()
    me.save_matlab_image()


def main():
    file_name = "data.csv"
    U0_list, epsilon0_list = me.read_U0_epsilon0_files()
    me.create_and_write_csv_if_not_exist(U0_list, epsilon0_list, file_name)
    # st()
    T_max = sys.ar
    T_min = 
    next_U0, next_epsilon0 = me.get_next_U0_epsilon0(file_name)
    while True:
        event_loop(file_name)
        add_data_to_csv()


main()