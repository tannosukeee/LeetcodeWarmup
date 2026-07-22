class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")
crazy_in_love.next = formation
formation.next = texas_hold_em
formation.prev = crazy_in_love
texas_hold_em.prev = formation