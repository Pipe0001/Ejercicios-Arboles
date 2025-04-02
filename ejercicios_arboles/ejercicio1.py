from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.left: 'Node' | None = None
        self.right: 'Node' | None = None

class BinarySearchTree:
    def __init__(self, root=None, key=lambda x: x):
        self.root: Node | None = root
        self.key = key
        self._size: int = 0

    def insert(self, data: Any):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        self._size += 1

    def _insert(self, node: Node, data: Any):
        if self.key(data) < self.key(node.data):
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
        if self.key(node.data) == goal:
            return True
        if self.key(goal) < self.key(node.data):
            return self._search(node.left, goal)
        return self._search(node.right, goal)

    def is_empty(self) -> bool:
        return self.root is None

    def __len__(self) -> int:
        return self._size

class DecisionTree:
    def __init__(self, data):
        self.data = data

    def diagnose(self):
        node = self.data
        while "pregunta" in node:
            answer = input(f"{node['pregunta']} (sí/no): ").strip().lower()
            if answer == "sí":
                node = node.get("si", {})
            elif answer == "no":
                node = node.get("no", {})
            else:
                print("Por favor, responde 'sí' o 'no'.")
        print(f"Diagnóstico: {node.get('diagnostico', 'Sin diagnóstico claro')}")
        return node.get('diagnostico', 'Sin diagnóstico claro')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.data
        if "si" in node:
            self.postorder_traversal(node["si"])
        if "no" in node:
            self.postorder_traversal(node["no"])
        print(node.get("diagnostico", node.get("pregunta", "")))

# Estructura del árbol de decisiones
medical_tree = {
    "pregunta": "¿Tiene fiebre?",
    "si": {
        "pregunta": "¿Tiene tos seca?",
        "si": {
            "pregunta": "¿Tiene dificultad para respirar?",
            "si": {"diagnostico": "Covid-19"},
            "no": {
                "pregunta": "¿Tiene dolor muscular?",
                "si": {"diagnostico": "Influenza"},
                "no": {"diagnostico": "Gripe leve"}
            }
        },
        "no": {
            "pregunta": "¿Tiene dolor de garganta?",
            "si": {
                "pregunta": "¿Tiene ganglios inflamados?",
                "si": {"diagnostico": "Faringitis"},
                "no": {"diagnostico": "Resfriado común"}
            },
            "no": {
                "pregunta": "¿Tiene sarpullido?",
                "si": {"diagnostico": "Sarampión"},
                "no": {"diagnostico": "Fiebre sin causa conocida"}
            }
        }
    },
    "no": {
        "pregunta": "¿Tiene estornudos?",
        "si": {
            "pregunta": "¿Tiene ojos llorosos?",
            "si": {
                "pregunta": "¿Es temporada de polen?",
                "si": {"diagnostico": "Alergia estacional"},
                "no": {"diagnostico": "Irritación ocular"}
            },
            "no": {
                "pregunta": "¿Tiene mucosidad clara?",
                "si": {"diagnostico": "Rinitis alérgica"},
                "no": {"diagnostico": "Resfriado leve"}
            }
        },
        "no": {
            "pregunta": "¿Siente fatiga constante?",
            "si": {
                "pregunta": "¿Tiene dificultad para concentrarse?",
                "si": {"diagnostico": "Fatiga crónica"},
                "no": {"diagnostico": "Falta de sueño"}
            },
            "no": {
                "pregunta": "¿Tiene dolor abdominal?",
                "si": {
                    "pregunta": "¿Ha tenido diarrea?",
                    "si": {"diagnostico": "Gastroenteritis"},
                    "no": {"diagnostico": "Indigestión"}
                },
                "no": {"diagnostico": "Sin diagnóstico claro"}
            }
        }
    }
}

# Crear árboles
tree = DecisionTree(medical_tree)
bst = BinarySearchTree()

# Diagnóstico usando el árbol de decisiones
tree.diagnose()

# Recorrido postorden
tree.postorder_traversal()
