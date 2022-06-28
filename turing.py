class Turing_machine:
    rules: dict
    
    def __init__(self):
        self.rules = dict()
    
    def add_symbol(self, symbol, states):
        if symbol not in self.rules:
            self.rules[symbol] = [None] * states
            
    def remove_symbol(self, symbol):
        if symbol in self.rules:
            self.rules.pop(symbol)
            
    def add_rule(self, symbol, state, rule):
        if rule and rule[1] in ('<', '.', '>'):
            self.rules[symbol][state] = rule
            return rule
        return None
    
    def remove_rule(self, symbol, state):
        if symbol in self.rules:
            self.rules[symbol][state] = None
    
    def execute(self, line, start_pos):
        if isinstance(line, list):
            position = start_pos
            state = 1
            sub_line = line.copy()
            
            while(state != 0):
                current_symbol = sub_line[position]
                rule = self.rules[current_symbol][state-1]
                print(sub_line)
                print(f'{rule=} {current_symbol=}')
                
                if rule is not None:
                    sub_line[position] = rule[0]
                    match(rule[1]):
                        case '<':
                            if position != 0:
                                position -= 1
                                continue
                            sub_line.insert(0, ' ')
                        case '>':
                            if position != len(sub_line) - 1:
                                position += 1
                                continue
                            sub_line.append(' ')
                        case '.':
                            state = 0
                            break
                        
                    state = int(rule[2])
                
            return sub_line
        return None
        