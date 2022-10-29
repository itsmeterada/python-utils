import tkinter
import subprocess
import os
import sys

class Application(tkinter.Frame):
  def __init__(self, root):
    super().__init__(root, width=260, height=180, 
    borderwidth=0, highlightthickness=0, relief='groove')
    self.root = root
    root.bind('<Key>', self.key_handler)
    self.cmd = 'adb shell input keyevent '
    self.ipaddr = '192.168.2.105'
    self.pack()
    self.pack_propagate(0)
    self.create_widgets()

  def create_widgets(self):
    # FireTV adb ip address
    ip_label = tkinter.Label(self, text='FireTV IP:')
    ip_label.grid(row=0, column=0, sticky='w')
    self.ip_entry = tkinter.Entry(self, width=15)
    self.ip_entry.grid(row=0, column=1, sticky='w')
    self.ip_entry.insert(0, self.ipaddr)
    connect = tkinter.Button(self, text='Connect', command=self.connect_handler)
    connect.grid(row=0, column=2, sticky='w')

    back_btn = tkinter.Button(self, text='Back', command=self.back_btn_handler)
    back_btn.grid(row=1, column=0, sticky='ew')
    up_btn = tkinter.Button(self, text=' Up ', command=self.up_btn_handler)
    up_btn.grid(row=1, column=1, sticky='ew')
    menu_btn = tkinter.Button(self, text='Menu', command=self.menu_btn_handler)
    menu_btn.grid(row=1, column=2, sticky='ew')
    left_btn = tkinter.Button(self, text='Left', command=self.left_btn_handler)
    left_btn.grid(row=2, column=0, sticky='ew')
    enter_btn = tkinter.Button(self, text='Enter', command=self.enter_btn_handler)
    enter_btn.grid(row=2, column=1, sticky='ew')
    right_btn = tkinter.Button(self, text='Right', command=self.right_btn_handler)
    right_btn.grid(row=2, column=2, sticky='ew')
    home_btn = tkinter.Button(self, text='Home', command=self.home_btn_handler)
    home_btn.grid(row=3, column=0, sticky='ew')
    down_btn = tkinter.Button(self, text='Down', command=self.down_btn_handler)
    down_btn.grid(row=3, column=1, sticky='ew')
    play_btn = tkinter.Button(self, text='Play/Pause', command=self.play_btn_handler)
    play_btn.grid(row=3, column=2, sticky='ew')
    volup_btn = tkinter.Button(self, text='Vol Up', command=self.volup_btn_handler, bg='grey')
    volup_btn.grid(row=4, column=1, sticky='ew')
    voldown_btn = tkinter.Button(self, text='Vol Down', command=self.voldown_btn_handler, bg='grey')
    voldown_btn.grid(row=5, column=1, sticky='ew')
    prev_btn = tkinter.Button(self, text='Prev', command=self.prev_btn_handler)
    prev_btn.grid(row=4, column=0, sticky='ew')
    next_btn = tkinter.Button(self, text='Next', command=self.next_btn_handler)
    next_btn.grid(row=4, column=2, sticky='ew')
    mute_btn = tkinter.Button(self, text='Mute', command=self.mute_btn_handler, bg='grey')
    mute_btn.grid(row=5, column=0, sticky='ew')
    wakeup_btn = tkinter.Button(self, text='WakeUp', command=self.wakeup_btn_handler)
    wakeup_btn.grid(row=5, column=2, sticky='ew')

  def connect_handler(self):
    # Call subprocess synchronously to ensure the connection is established.
    subprocess.run('adb kill-server', shell=True, stdout=subprocess.PIPE)
    subprocess.run('adb start-server', shell=True, stdout=subprocess.PIPE)
    subprocess.run('adb connect ' + self.ip_entry.get(), shell=True)

  def back_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_BACK', shell=True)
  def up_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_DPAD_UP', shell=True)
  def menu_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_MENU', shell=True)
  def left_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_DPAD_LEFT', shell=True)
  def right_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_DPAD_RIGHT', shell=True)
  def down_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_DPAD_DOWN', shell=True)
  def enter_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_DPAD_CENTER', shell=True)
  def play_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_MEDIA_PLAY_PAUSE', shell=True)
  def home_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_HOME', shell=True)
  def volup_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_VOLUME_UP', shell=True)
  def voldown_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_VOLUME_DOWN', shell=True)
  def prev_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_MEDIA_PREVIOUS', shell=True)
  def next_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_MEDIA_NEXT', shell=True)
  def mute_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_VOLUME_MUTE', shell=True)
  def wakeup_btn_handler(self): subprocess.Popen(self.cmd + 'KEYCODE_WAKEUP', shell=True)

  def key_handler(self, e):
    key = e.keysym
    print(key)
    if (key == 'BackSpace'): self.back_btn_handler()
    if (key == 'Up'): self.up_btn_handler()
    if (key == 'Down'): self.down_btn_handler()
    if (key == 'Left'): self.left_btn_handler()
    if (key == 'Right'): self.right_btn_handler()
    if (key == 'Return'): self.enter_btn_handler()
    if (key == 'space'): self.play_btn_handler()
    if (key == 'Escape'): self.home_btn_handler()
    if (key == 'Tab'): self.menu_btn_handler()
    if (key == 'Home'): self.volup_btn_handler()
    if (key == 'End'): self.voldown_btn_handler()
    if (key == 'Prior'): self.prev_btn_handler()
    if (key == 'Next'): self.next_btn_handler()
    if (key == 'Insert'): self.mute_btn_handler()
    if (key == 'Delete'): self.wakeup_btn_handler()

def main():
  my_env = os.environ.copy()
  args = sys.argv
  project_name = os.getcwd()
  project_dir = os.path.split(project_name)[1]
  root = tkinter.Tk()
  root.title('FireTV Controller')
  # root.geometry('300x200')
  app = Application(root)
  root.mainloop()

if __name__ == '__main__':
  main()
