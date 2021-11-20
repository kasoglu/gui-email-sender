from tkinter import *
import smtplib

BACKGROUND_COLOR = "#ffe082"
FONT = ("Times New Roman", 20, "italic")


# ====================== E-MAIL SENDER SECTION ====================#

def send_email():
    # Replace with your email address and password
    my_email = "your@email.com"
    password = "password"

    topic = subject.get()
    to = reciever.get()
    text = message.get("1.0", END)

    # Replace with your mail address SMTP server. Unless it will not work.
    # Gmail: smtp.gmail.com
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{to}",
            msg=f"Subject:{topic}\n\n {text}"
        )
    connection.close()

# ====================== GUI SETUP SECTION ====================#

window = Tk()
window.title("GUI E-Mail Sender")
# window.geometry("650x500")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)


canvas = Canvas(width=128, height=128, highlightthickness=0, bg=BACKGROUND_COLOR)
logo = PhotoImage(file="logo.png")
canvas.create_image(64, 64, image=logo)
canvas.grid(column=2, row=1, rowspan=2)

reciever_label = Label(text="To:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
reciever_label.grid(column=0, row=1)

reciever = Entry(width=30, highlightthickness=0)
reciever.focus()
reciever.grid(column=1, row=1)

subject_label = Label(text="Subject:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
subject_label.grid(column=0, row=2)

subject = Entry(width=30, highlightthickness=0)
subject.grid(column=1, row=2)

message_label = Label(text="Message:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
message_label.grid(column=0, row=3)

message = Text(height=15, width=60)
message.grid(column=0, row=4, columnspan=2)

send_button = Button(text="Send", highlightthickness=0, padx=30, pady=5, command=send_email)
send_button.grid(column=2, row=5)



window.mainloop()
