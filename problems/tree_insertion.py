class TreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None
	

class BinarySearchTree :
	def __init__(self) :
		self.root = None
	
	# insert a element
	def addNode(self, data) :
		#  Create a new node
		node = TreeNode(data)
		if (self.root == None) :
			#  When adds a first node in bst
			self.root = node
		else :
			find = self.root
			#  Add new node to proper position
			while (find != None) :
				if (find.data >= data) :
					if (find.left == None) :
						#  When left child empty
						#  So add new node here
						find.left = node
						return
					else :
						#  Otherwise
						#  Visit left sub-tree
						find = find.left
					
				else :
					if (find.right == None) :
						#  When right child empty
						#  So add new node here
						find.right = node
						return
					else :
						#  Visit right sub-tree
						find = find.right
					
				
			
		
	
	#  Display preorder
	def preorder(self, node) :
		if (node != None) :
			#  Display node value
			print(" ", node.data, end = " ")
			#  Visit to left subtree
			self.preorder(node.left)
			#  Visit to right subtree
			self.preorder(node.right)
		
	
	def inorder(self, node) :
		if (node != None) :
			#  Visit to left subtree
			self.inorder(node.left)
			#  Display node value
			print(" ", node.data, end = " ")
			#  Visit to right subtree
			self.inorder(node.right)
		
	
	def postorder(self, node) :
		if (node != None) :
			#  Visit to left subtree
			self.postorder(node.left)
			#  Visit to right subtree
			self.postorder(node.right)
			#  Display node value
			print(" ", node.data, end = " ")
		
	

def main() :
	tree = BinarySearchTree()
	#         10
	#        / \
	#       /   \
	#      4     15
	#     / \   /
	#    3   5 12
	#    -------------
	#    Build binary search tree
	tree.addNode(10)
	tree.addNode(4)
	tree.addNode(3)
	tree.addNode(5)
	tree.addNode(15)
	tree.addNode(12)
	#  Display tree nodes
	print("Preorder ")
	tree.preorder(tree.root)
	print("\nInorder ")
	tree.inorder(tree.root)
	print("\nPostorder ")
	tree.postorder(tree.root)

if __name__ == "__main__": main()