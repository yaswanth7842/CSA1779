class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_terminal(self):
        return not self.children

    def evaluate(self):
        return self.value

    def generate_children(self):
        return self.children

def minimax(node, depth, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        max_eval = float("-inf")
        for child in node.generate_children():
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for child in node.generate_children():
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Example usage
def main():
    root_value = int(input("Enter the value for the root node: "))
    root = Node(root_value)

    num_children = int(input("Enter the number of children for the root node: "))
    for _ in range(num_children):
        child_value = int(input("Enter the value for a child node: "))
        root.children.append(Node(child_value))

    depth = int(input("Enter the depth for the minimax search: "))
    best_score = minimax(root, depth, True)
    print("Best score:", best_score)

if __name__ == "__main__":
    main()
