# Trabalho de Automatos para Teoria de Computação #
# Felipe Lima
# 30/05/2018
# Faculdade Ruy Barbosa

class Automato:
    def __init__(self, nstates):
        self.transitions = [{} for i in range(nstates)]
        self.accept_states = [False] * nstates

    def register(self, source_state, char, target_state):
        self.transitions[source_state][char] = target_state

    def register_accept(self, state):
        self.accept_states[state] = True

    def accept(self, input):
        state = 0
        try:
            for char in input:
                state = self.transitions[state][char]
            return self.accept_states[state]
        except KeyError:
            return False
        
automato = Automato(2)
automato.register(0, 'a', 1)
automato.register(0, 'b', 1)
automato.register(0, 'c', 1)
automato.register(1, 'x', 1)
automato.register_accept(1)

print automato.accept('ax')
print automato.accept('bxxx')
print automato.accept('abxxx')
print automato.accept('dx')