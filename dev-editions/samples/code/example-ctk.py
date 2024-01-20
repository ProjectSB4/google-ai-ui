#fun thing to be an example
#help at https://customtkinter.tomschimansky.com/documentation/
import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
is_preparing = False
def prepare():
    main.destroy()
    print("Starting! Please wait!")
    print(f"Crash Reports: {enable_debug._check_state}")

main = ctk.CTk()
main.title(string="Course GUI")
main.geometry("600x400")
main.resizable(width=False, height=False)

pathbox = ctk.CTkEntry(main, placeholder_text="Insert Path to file.")
pathbox.place(relx=0.5, rely=0.15, anchor="center")

enable_debug = ctk.CTkCheckBox(main, text="Enable Crash Reports")
enable_debug.place(relx=0.5, rely=0.25, anchor="center")
launch_button = ctk.CTkButton(main, text="Launch", command=prepare)
launch_button.place(relx=0.5, rely=0.35, anchor="center")

main.mainloop()
