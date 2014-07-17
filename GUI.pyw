import Tkinter as tk
import otppy


def update_otp():
	text=""
	trefr=999
	for service in otps:
		totp=service[1].TOTP()
		text=text+service[0]+" : "+totp[0]+"\n"
		trefrx = totp[1]+1
		if  trefrx < trefr : trefr = trefrx
	txt.set(text[:-1])
	if trefr < 6: w.config(fg="red")
	else:
		w.config(fg="LightBlue")
		trefr = trefr - 5
	mainwin.after(trefr*1000, update_otp)

f = open('user.dat', 'rb')
otps=[]
for line in f:
	data=line.rstrip('\n').split(",")
	otps.append([data[0],otppy.fromb32(data[1],data[2],int(data[3]))])
f.close()

mainwin = tk.Tk()
mainwin.title("Fast OTP")
mainwin.resizable(width=False,height=False)
txt = tk.StringVar()
w = tk.Label(mainwin, textvariable=txt, font=("Arial", 22), bg="grey20", borderwidth=30, padx=10)
w.pack()
update_otp()
mainwin.mainloop()

