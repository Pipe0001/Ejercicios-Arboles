import pickle
from typing import Any

# Clases de Nodo y Árbol Binario de Búsqueda
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self._size = 0

    def insert(self, data: Any):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        self._size += 1

    def _insert(self, node: Node, data: Any):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def search(self, goal: Any) -> bool:
        return self._search(self.root, goal)

    def _search(self, node: Node, goal: Any) -> bool:
        if node is None:
            return False
        if node.data == goal:
            return True
        if goal < node.data:
            return self._search(node.left, goal)
        return self._search(node.right, goal)

    def __len__(self) -> int:
        return self._size


# Clases para el juego de adivinanza
class DecisionNode:
    def __init__(self, question=None, yes=None, no=None, adivinanza=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.adivinanza = adivinanza


class GuessingGame:
    def __init__(self, root: DecisionNode):
        self.root = root

    def pre_order_traversal(self, node=None):
        """Recorrido en preorden para mostrar todas las preguntas."""
        if node is None:
            node = self.root
        if node.question:
            print(node.question)
        if node.yes:
            self.pre_order_traversal(node.yes)
        if node.no:
            self.pre_order_traversal(node.no)

    def play_game(self):
        """Jugar al juego interactivo con el árbol de decisiones."""
        self._play_game(self.root)

    def _play_game(self, node):
        if node.adivinanza:  # Si es una hoja con una adivinanza
            answer = input(f"¿Estás pensando en {node.adivinanza}? (sí/no): ").strip().lower()
            if answer == "sí":
                print("¡Adiviné!")
            else:
                print("No adiviné. Ayúdame a mejorar.")
                self.update_tree(node)
        else:
            answer = input(f"{node.question} (sí/no): ").strip().lower()
            if answer == "sí":
                self._play_game(node.yes)
            else:
                self._play_game(node.no)

    def update_tree(self, failed_node):
        """Permitir al usuario agregar una nueva pregunta y adivinanza al árbol."""
        object_thought = input("¿Qué objeto estabas pensando? ").strip()
        new_question = input(f"¿Qué pregunta me ayudaría a diferenciar a {failed_node.adivinanza} de {object_thought}? ").strip()
        answer_to_new_question = input(f"Si la respuesta es 'sí', ¿a qué objeto se refiere? ").strip()
        
        new_yes_node = DecisionNode(adivinanza=object_thought)
        new_no_node = DecisionNode(adivinanza=failed_node.adivinanza)
        
        failed_node.question = new_question
        failed_node.yes = new_yes_node
        failed_node.no = new_no_node
        failed_node.adivinanza = None

    def save_tree(self, filename="game_tree.pkl"):
        """Guardar el árbol actualizado en un archivo."""
        with open(filename, 'wb') as file:
            pickle.dump(self.root, file)

    @staticmethod
    def load_tree(filename="game_tree.pkl"):
        """Cargar el árbol desde un archivo."""
        with open(filename, 'rb') as file:
            return pickle.load(file)


# Crear el árbol de preguntas basado en tu ejemplo
root = DecisionNode(
    question="¿Es un ser vivo?",
    yes=DecisionNode(
        question="¿Es un animal?",
        yes=DecisionNode(
            question="¿Vuela?",
            yes=DecisionNode(
                question="¿Tiene plumas?",
                yes=DecisionNode(adivinanza="Un loro"),
                no=DecisionNode(adivinanza="Un murciélago")
            ),
            no=DecisionNode(
                question="¿Es doméstico?",
                yes=DecisionNode(adivinanza="Un perro"),
                no=DecisionNode(adivinanza="Un tigre")
            )
        ),
        no=DecisionNode(
            question="¿Tiene raíces?",
            yes=DecisionNode(
                question="¿Da frutos comestibles?",
                yes=DecisionNode(adivinanza="Un manzano"),
                no=DecisionNode(adivinanza="Un pino")
            ),
            no=DecisionNode(adivinanza="Un hongo")
        )
    ),
    no=DecisionNode(
        question="¿Se puede usar para comunicarse?",
        yes=DecisionNode(
            question="¿Tiene pantalla?",
            yes=DecisionNode(adivinanza="Un teléfono móvil"),
            no=DecisionNode(adivinanza="Un walkie-talkie")
        ),
        no=DecisionNode(
            question="¿Es un alimento?",
            yes=DecisionNode(
                question="¿Es dulce?",
                yes=DecisionNode(adivinanza="Un pastel"),
                no=DecisionNode(adivinanza="Una pizza")
            ),
            no=DecisionNode(
                question="¿Tiene ruedas?",
                yes=DecisionNode(
                    question="¿Se usa para transporte personal?",
                    yes=DecisionNode(adivinanza="Una bicicleta"),
                    no=DecisionNode(adivinanza="Un camión")
                ),
                no=DecisionNode(adivinanza="Una roca")
            )
        )
    )
)

# Crear el juego con el árbol de decisiones
game = GuessingGame(root)

# Jugar el juego
game.play_game()

# Guardar el árbol actualizado
game.save_tree()

# Mostrar recorrido preorden del árbol
game.pre_order_traversal()
