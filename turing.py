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
        if len(rule) == 3 and rule[1] in ('<', '.', '>'):
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
                if current_symbol not in self.rules:
                    return 'Error'
                rule = self.rules[current_symbol][state-1]
                
                if rule is not None:
                    sub_line[position] = rule[0]
                    match(rule[1]):
                        case '<':
                            if position == 0:
                                sub_line.insert(0, ' ')
                            else:
                                position -= 1
                        case '>':
                            if position == len(sub_line) - 1:
                                sub_line.append(' ')
                            position += 1
                        case '.':
                            state = 0
                            break
                        
                    state = int(rule[2])
                else:
                    return 'Error'
                
            return sub_line
        return 'Error'
        