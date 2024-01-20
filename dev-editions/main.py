import customtkinter as ctk
import os
import shutil
import webbrowser
import time
from customtkinter import StringVar, filedialog
import google.generativeai as genai
import json
from pathlib import Path
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
main = ctk.CTk()
main.title(string="Google AI GUI")
main.geometry("600x600")
main.resizable(width=False, height=False)
api_key = ''
fvv = StringVar()
fvv2 = StringVar()

#check for api_key_file
api_key_file = open("apikey.txt", "r+")
line = api_key_file.readline().strip()
if not line:
    print("""No API Key detected. Please insert one now. You can get one at:
          https://makersuite.google.com/app/apikey
          Copy and paste the key into this terminal and press enter.""")
    api_key_input = input("Insert your API Key: ")
    api_key_file.write(api_key_input)
    api_key = api_key_input   
else:
    print("[DEBUG] API KEY FOUND")
    api_key = line
api_key_file.close()
print(f"[DEBUG] API_KEY = {api_key}")
#check and read saftey-gemini.txt
def saftey_error():
    print("""OH NO!
          Your "Saftey-gemini.txt" file is gone or not working!
          Type "R" to reset the file.""")
    se_enter_input = input()
    if se_enter_input == "R":
        print("BEGINNING SAFTEY FILE RESET")
    else:
        exit()
    try:
        os.remove("saftey-gemini.txt")
        print("CAUSE FOUND! FILE INCORRECT")
    except FileNotFoundError:
        print("CAUSE FOUND! FILE NON-EXISTANT")
    with open('saftey-gemini.txt', 'w') as sesf:
        sesf.write("""[
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]""")
    sesf.close()
    print("ALL DONE! Please re-open the application to proceed.")
    time.sleep(3)
    exit()
def saftey_error_palm():
    print("""OH NO!
          Your "Saftey-palm.txt" file is gone or not working!
          Type "R" to reset the file.""")
    se_enter_input = input()
    if se_enter_input == "R":
        print("BEGINNING SAFTEY FILE RESET")
    else:
        exit()
    try:
        os.remove("saftey-palm.txt")
        print("CAUSE FOUND! FILE INCORRECT")
    except FileNotFoundError:
        print("CAUSE FOUND! FILE NON-EXISTANT")
    with open('saftey-palm.txt', 'w') as sesf:
        sesf.write("""[{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_MEDIUM_AND_ABOVE"}]""")
    sesf.close()
    print("ALL DONE! Please re-open the application to proceed.")
    time.sleep(3)
    exit()
try:
    with open('saftey-gemini.txt', 'r') as f:
        saftey_gemini = json.load(f)
except FileNotFoundError:
    print("[DEBUG] SE-FNFE")
    saftey_error()
if not saftey_gemini:
    saftey_error()
    print("[DEBUG] SE-SE-FALSE")
else:
    print("GEMINI", saftey_gemini)
try:
   with open("saftey-palm.txt", "r") as saftey_file_p:
       saftey_palm = json.load(saftey_file_p)
except FileNotFoundError:
   print("[DEBUG] SE-FNFE")
   saftey_error_palm()
if not saftey_palm:
   print("[DEBUG] SE-SE-FALSE")
   saftey_error_palm()
else:
   print("PALM", saftey_palm)
#wipe tmp
for filename in os.listdir('tmp'):
    if os.path.isfile(os.path.join('tmp', filename)):
        os.remove(os.path.join('tmp', filename))
def update_model(choice):
    print("[DEBUG] modelchoose dropdown clicked", choice)
    temlabel.place(relx=0.5, rely=0.30, anchor="center")
    temslider.place(relx=0.5, rely=0.35, anchor="center")
    tpl.place(relx=0.5, rely=0.40, anchor="center")
    tps.place(relx=0.5, rely=0.45, anchor="center")
    tkl.place(relx=0.4, rely=0.51, anchor="center")
    tke.place(relx=0.6, rely=0.51, anchor="center")
    oll.place(relx=0.4, rely=0.56, anchor="center")
    ole.place(relx=0.6, rely=0.56, anchor="center")
    ssl.place(relx=0.4, rely=0.61, anchor="center")
    sse.place(relx=0.6, rely=0.61, anchor="center")
    respond.place(relx=0.5, rely=0.77, anchor="center")
    ai.place(relx=0.25, rely=0.77, anchor="center")
    ac.place(relx=0.75, rely=0.77, anchor="center")
    if choice == "PaLM 2 (Legacy)":
        print("[DEBUG] PaLM Options Updater Test")
        mos_palmonly_label.place(relx=0.5, rely=0.67, anchor="center")
        mos_palmonly.place(relx=0.5, rely=0.72, anchor="center")
        mos_palmonly.set(1.0)
        update_moslabel(1.0)
        temslider.set(0.7)
        update_temlabel(0.7)
        tps.set(0.9)
        update_tpl(0.9)
        tke.delete(0, "end")
        tke.insert(0, "40")
        ole.delete(0, "end")
        ole.insert(0, "1024")
        ai.configure(state="disabled")
        respond.configure(state="normal")
    elif choice == "Gemini Pro":
        temslider.set(0.9)
        update_temlabel(0.9)
        tps.set(1)
        update_tpl(1)
        tke.delete(0, "end")
        tke.insert(0, "1")
        ole.delete(0, "end")
        ole.insert(0, "2048")
        mos_palmonly_label.place(relx=0.5, rely=-0.67, anchor="center")
        mos_palmonly.place(relx=0.5, rely=-0.72, anchor="center")
        ai.configure(state="disabled")
        respond.configure(state="normal")
    elif choice == "Gemini Pro Vision":
        temslider.set(0.4)
        update_temlabel(0.4)
        tps.set(1)
        update_tpl(1)
        tke.delete(0, "end")
        tke.insert(0, "32")
        ole.delete(0, "end")
        ole.insert(0, "4096")
        mos_palmonly_label.place(relx=0.5, rely=-0.67, anchor="center")
        mos_palmonly.place(relx=0.5, rely=-0.72, anchor="center")
        ai.configure(state="enabled")
        respond.configure(state="disabled")
def update_temlabel(temp):
    temlabel.configure(text=f"Tempature: {temp}")

def update_moslabel(outputs):
    mos_palmonly_label.configure(text=f"Max Outputs: {outputs}")

def update_tpl(P):
    tpl.configure(text=f"Top P: {P}")

def validate_int1(S):
    try:
        int(S)
        return True
    except ValueError:
        if S == "":
            return True
        return False
def validate_int2(S):
    try:
        int(S)
        return True
    except ValueError:
        if S == "":
            return True
        return False
def aic():
   image = filedialog.askopenfilename(initialdir = f"C:/Users/{os.getlogin()}/Downloads", title = "Select a File", filetypes = [("PNG files", "*.png*")])
   shutil.copy(image, f"C:/Users/{os.getlogin()}/AppData/Local/ProjectSB4/google-ai-ui/tmp/")
   respond.configure(state="normal")
def ghc():
    webbrowser.open("https://github.com/ProjectSB4/google-ai-ui/wiki/Help-Hub")
def vgc():
    webbrowser.open("https://github.com/ProjectSB4/google-ai-ui/tree/main")
def respond():
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": temslider.get(),
        "top_p": tps.get(),
        "top_k": int(tke.get()),
        "max_output_tokens": int(ole.get()),
        "stop_sequences": [
            sse.get(),
        ],
    }
    if not sse.get() == "":
        print("[DEBUG] R-SSE-TRUE")
        defaults = {
        'model': 'models/text-bison-001',
        'temperature': temslider.get(),
        'candidate_count': int(mos_palmonly.get()),
        'top_k': int(tke.get()),
        'top_p': tps.get(),
        'stop_sequences': [sse.get()],
        'max_output_tokens': int(ole.get()),
        'safety_settings': saftey_palm,
        }
    else:
        print("[DEBUG] R-SSE-FALSE")
        defaults = {
        'model': 'models/text-bison-001',
        'temperature': temslider.get(),
        'candidate_count': int(mos_palmonly.get()),
        'top_k': int(tke.get()),
        'top_p': tps.get(),
        'max_output_tokens': int(ole.get()),
        'safety_settings': saftey_palm,
        }
    gemini = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=saftey_gemini)
    vision = genai.GenerativeModel(model_name="gemini-pro-vision", generation_config=generation_config, safety_settings=saftey_gemini)
    prompt = f"""{prompt_box.get()}"""
    if modelchoose.get() == "Gemini Pro":
        #os.system("cls")
        gr = gemini.generate_content(prompt)
        try:
            print(gr.text)
            answerboxfill(gr.text)
        except:
            error(gr.prompt_feedback)
    elif modelchoose.get() == "PaLM 2 (Legacy)":
        #os.system("cls")
        pr = genai.generate_text(
            **defaults,
            prompt=prompt
        )
        try:
            print(pr.result)
            answerboxfill(pr.result)
        except:
            error(pr.prompt_feedback)
    elif modelchoose.get() == "Gemini Pro Vision":
        if not (img := Path("tmp/image.png")).exists():
            print("PLEASE MAKE SURE THE IMAGE IS NAMED image.png and that it exists")
            main.destroy()
            time.sleep(5)
            exit()
        image_parts = [
            {
                "mime_type": "image/png",
                "data": Path("tmp/image.png").read_bytes()
            }
        ]
        prompt_parts = [
            prompt_box.get(),
            image_parts[0],
        ]
        vr = vision.generate_content(prompt_parts)
        try:
            print(vr.text)
            answerboxfill(vr.text)
        except:
            error(vr.prompt_feedback)
def answerboxfill(fill):
    answer_box.configure(state="normal")
    answer_box.delete(0, "end")
    answer_box.insert(0, fill)
    answer_box.configure(state="disabled")
def error(message):
    main.destroy()
    ctk.set_appearance_mode("light")
    errormain = ctk.CTk()
    errormain.title(string="Google-AI-UI ERROR")
    errormain.geometry("400x600")
    errormain.resizable(width=False, height=False)
    errorlabel = ctk.CTkLabel(errormain, text=f"{message} \n Please check the Help Hub for assistance.")
    errorlabel.pack()
    def errorview():
        webbrowser.open("https://github.com/ProjectSB4/google-ai-ui/wiki/Help-Hub")
        exit()
    errorbutton = ctk.CTkButton(errormain, text="Go Now", command=errorview)
    errorbutton.pack()
    errormain.mainloop()
def viewsafteyins():
    webbrowser.open("https://github.com/ProjectSB4/google-ai-ui/wiki/Edit-Safety-Settings")
title = ctk.CTkLabel(main, text="Google AI GUI", fg_color="transparent")
title.place(relx=0.5, rely=0.05, anchor="center")

modelchoose = ctk.CTkComboBox(main, values=["Gemini Pro", "Gemini Pro Vision", "PaLM 2 (Legacy)"], command=update_model, state="readonly")
modelchoose.set("Select a model")
modelchoose.place(relx=0.5, rely=0.15, anchor="center")

temlabel = ctk.CTkLabel(main, text="Tempature: 0.5", fg_color="transparent")
temlabel.place(relx=0.5, rely=-0.30, anchor="center")

temslider = ctk.CTkSlider(main, from_=0, to=1, command=update_temlabel)
temslider.place(relx=0.5, rely=-0.35, anchor="center")

tpl = ctk.CTkLabel(main, text="Top P: 0.5", fg_color="transparent")
tpl.place(relx=0.5, rely=-0.40, anchor="center")

tps = ctk.CTkSlider(main, from_=0, to=1, command=update_tpl)
tps.place(relx=0.5, rely=-0.45, anchor="center")

tkl = ctk.CTkLabel(main, text="Top K - Not 0", fg_color="transparent")
tkl.place(relx=0.5, rely=-0.51, anchor="center")

tke = ctk.CTkEntry(main, textvariable=fvv)
tke.place(relx=0.5, rely=-0.51, anchor="center")
tke.configure(validate="key", validatecommand=(tke.register(validate_int1), '%P'))

oll = ctk.CTkLabel(main, text="Output Length", fg_color="transparent")
oll.place(relx=0.5, rely=-0.56, anchor="center")

ole = ctk.CTkEntry(main, textvariable=fvv2)
ole.place(relx=0.5, rely=-0.56, anchor="center")
ole.configure(validate="key", validatecommand=(ole.register(validate_int2), '%P'))

ssl = ctk.CTkLabel(main, text="Stop Sequence", fg_color="transparent")
ssl.place(relx=0.5, rely=-0.61, anchor="center")

sse = ctk.CTkEntry(main)
sse.place(relx=0.5, rely=-0.61, anchor="center")

mos_palmonly_label = ctk.CTkLabel(main, text="Maximum Output: 0.5", fg_color="transparent")
mos_palmonly_label.place(relx=0.5, rely=-0.67, anchor="center")

mos_palmonly = ctk.CTkSlider(main, from_=1, to=8, command=update_moslabel, number_of_steps=7)
mos_palmonly.place(relx=0.5, rely=-0.72, anchor="center")

respond = ctk.CTkButton(main, text="Respond", command=respond)
respond.place(relx=0.5, rely=-0.77, anchor="center")

se = ctk.CTkButton(main, text="Edit Saftey Settings", fg_color="#b55100", hover_color="#b50000", command=viewsafteyins)
se.place(relx=0.88, rely=0.03, anchor="center")

ai = ctk.CTkButton(main, text="Add Image", command=aic)
ai.place(relx=0.25, rely=-0.77, anchor="center")
ai.configure(state="disabled")

ac = ctk.CTkButton(main, text="Get Help", command=ghc)
ac.place(relx=0.75, rely=-0.77, anchor="center")

vg = ctk.CTkButton(main, text="View GitHub", command=vgc)
vg.place(relx=0.12, rely=0.03, anchor="center")

prompt_box = ctk.CTkEntry(main, 590, 50)
prompt_box.place(relx=0.5, rely=0.85, anchor="center")
answer_box = ctk.CTkEntry(main, 590, 50, state="disabled")
answer_box.place(relx=0.5, rely=0.95, anchor="center")
main.mainloop()
