import tkinter as tk

from turing import Turing_machine


tm = Turing_machine()

# Метод подготавливает данные для обработки скриптом
def machine_execute():
    for i, symbol in enumerate([entry.get() for entry in alphabet]):
        if symbol and len(symbol) == 1:
            tm.add_symbol(symbol, 10)
            for j in range(10):
                rule = cells[j][i].get()
                print(f'for {symbol=} {rule=}')
                tm.add_rule(symbol, j, rule)
            
    answer = ''.join(tm.execute(list(e.get()), 0)).strip()
    
    for symbol in tm.rules.copy():
        tm.remove_symbol(symbol)
        
    result.config(text = answer)


# Создание окна приложения
window = tk.Tk()
window.title('Turing machine emulator')

# Создание верхнего фрейма
line_frame = tk.Frame(window, bg='#222222')

e = tk.Entry(line_frame, bg='#353535', border=1, highlightcolor='#353535')
result = tk.Label(line_frame, bg='#454545', border=1)
execute = tk.Button(line_frame, text='Execute', command=machine_execute)

e.pack(fill='x')
result.pack(fill='x')
execute.pack(fill='x')

line_frame.grid(row=0)

# Создание фрейма под таблицу
rules_frame = tk.Frame(window, bg='#252525')

validate_less_than_2 = window.register(lambda x: len(x) < 2)
validate_rule = window.register(lambda x: len(x) < 4)

cells = [None] * 10
alphabet = list()

tk.Label(rules_frame, width=3, text=f'ABC').grid(row=0, column=0)

for i in range(10):
    tk.Label(rules_frame, width=3, text=f'Q{i+1}').grid(row=i+1, column=0)
    
    alphabet.append(cell:=tk.Entry(
        rules_frame, 
        width=3, 
        validate="key", 
        validatecommand=(validate_less_than_2, '%P')
        ))
    cell.grid(row=0, column=i+1)
    
    cells[i] = list()
    
    for j in range(10):
        cells[i].append(cell:=tk.Entry(
            rules_frame,
            width=3,
            validate="key", 
            validatecommand=(validate_rule, '%P')
        ))
        cell.grid(row=i+1, column=j+1)

rules_frame.grid(row=1)

window.mainloop()