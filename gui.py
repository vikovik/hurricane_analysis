import tkinter as tk
from tkinter import messagebox
from script import *
from variables import *

hurricanes = {}

def clear_text():
    result_text.delete("1.0", "end")

def on_option_change(*args):
    clear_text()

def exit_program():
    root.destroy()
    return 

def perform_action():
    selected_option = option_var.get()

    global hurricanes
    global updated_damages
    global areas_affected_count

    if selected_option == "1":
        updated_damages = damages_update(damages)
        result_text.delete("1.0", "end")
        result_text.insert("end", updated_damages)

    elif selected_option == "2":
        hurricanes = hurricanes_table(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
        result_text.delete("1.0", "end")

        for key, value in hurricanes.items():
            result_text.insert("end", f"\nHurricane: {key}\nValues: {value}\n")

    elif selected_option == "3":
        hurricanes_year = hurricanes_by_year(hurricanes)
        result_text.delete("1.0", "end")

        for key, value in hurricanes_year.items():
            result_text.insert("end", f"\nYear: {key}\nHurricanes: {value}\n")

    elif selected_option == "4":
        areas_affected_count = counting_damaged_areas(hurricanes)
        result_text.delete("1.0", "end")

        for key, value in areas_affected_count.items():
            result_text.insert("end", f"\nArea: {key}\nNumber of Hurricanes: {value}\n")

    elif selected_option == "5":
        max_hurricane, most_affected_area = max_hurricane_count(areas_affected_count)
        result_text.delete("1.0", "end")
        result_text.insert("end", f"\nMost Affected Area: {most_affected_area}\nNumber of Hurricanes: {max_hurricane}")

    elif selected_option == "6":
        deadliest_hurricane, max_deaths = deadliest_hurricane_count(hurricanes)
        result_text.delete("1.0", "end")
        result_text.insert("end", f"\nDeadliest Hurricane: {deadliest_hurricane}\nNumber of Deaths: {max_deaths}")

    elif selected_option == "7":
        rated_hurricanes = hurricanes_mortality_scale(hurricanes)
        result_text.delete("1.0", "end")

        for key, value in rated_hurricanes.items():
            result_text.insert("end", f"\nRating: {key}\nHurricanes: {value}\n")

    elif selected_option == "8":
        max_damage_hurricane, max_damage = calculate_max_damage(hurricanes)
        result_text.delete("1.0", "end")
        result_text.insert("end", f"\nMost Damaging Hurricane: {max_damage_hurricane}\nTotal Cost: {max_damage}")

    elif selected_option == "9":
        rated_hurricanes_damage = hurricane_damage_scale(hurricanes)
        result_text.delete("1.0", "end")

        for key, value in rated_hurricanes_damage.items():
            result_text.insert("end", f"\nRating: {key}\nHurricanes: {value}\n")
            
    else:
        messagebox.showerror("Error", "Invalid option selected")

root = tk.Tk()
root.title("Hurricane Analysis")

tk.Label(root, text="Select an option:\n").grid(row = 0, columnspan = 2)

option_var = tk.StringVar()
option_var.set("1")

options = [("Standardize Recorder Hurricanes Damages", "1"), 
           ("Create a Table of Hurricanes", "2"), 
           ("Organize Hurricanes by Year", "3"), 
           ("Count Damaged Areas", "4"),
           ("Find Most Affected Area and the Number of Hurricanes", "5"), 
           ("Calculate Deadliest Hurricane", "6"), 
           ("Rate Hurricanes by Mortality", "7"), 
           ("Calculate Hurricane Maximum Damage", "8"), 
           ("Rate Hurricanes by Damage", "9")]

for i, (text, value) in enumerate(options, start = 1):
    tk.Radiobutton(root, text=text, variable = option_var, value = value, command = on_option_change).grid(row = i, columnspan = 2)

perform_button = tk.Button(root, text = "Perform Action", command = perform_action, bg="green", fg="white")
perform_button.grid(row = 10, column = 0, columnspan = 2)

exit_button = tk.Button(root, text = "Exit Program", command = exit_program, bg="red", fg="white")
exit_button.grid(row = 11, column = 0, columnspan = 2)

result_text = tk.Text(root, height=20, width=100)
result_text.grid(row = 12, columnspan = 2)

on_option_change()

root.mainloop()