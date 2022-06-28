import tkinter as tk
from turing import Turing_machine


tm = Turing_machine()

def machine_execute():
    for i, symbol in enumerate([entry.get() for entry in alphabet]):
        if symbol and len(symbol) == 1:
            tm.add_symbol(symbol, 10)
            for j in range(10):
                rule = cells[i%10+j*10].get()
                tm.add_rule(symbol, i, rule)
            
    answer = tm.execute(list(e.get()), 0)
    print(answer)
        
    result.config(text = answer)


window = tk.Tk()
window.title('Turing machine emulator')


line_frame = tk.Frame(window, bg='#222222')

e = tk.Entry(line_frame, bg='#353535', border=1, highlightcolor='#353535')
result = tk.Label(line_frame, bg='#454545', border=1)
execute = tk.Button(line_frame, text='Execute', command=machine_execute)

e.pack(fill='x')
result.pack(fill='x')
execute.pack(fill='x')

line_frame.grid(row=0)

rules_frame = tk.Frame(window, bg='#252525')

cells = [] * 10
alphabet = [] * 10

tk.Label(rules_frame, width=3, text=f'ABC').grid(row=0, column=0)

for i in range(10):
    tk.Label(rules_frame, width=3, text=f'Q{i+1}').grid(row=i+1, column=0)
    
    alphabet.append(cell:=tk.Entry(rules_frame, width=3))
    cell.grid(row=0, column=i+1)
    
    for j in range(10):
        cells.append(cell:=tk.Entry(rules_frame, width=3))
        cell.grid(row=i+1, column=j+1)

rules_frame.grid(row=1)

window.mainloop()