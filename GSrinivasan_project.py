import pygame
from pygame.locals import *
import sys
import overlap


collision = False
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	def insert(self,data):
		if self.data:
			if sum(data)< sum(self.data):
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif sum(data) > sum(self.data):
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				self.data = data


	def increase_tree_values(self,node, delta):
		'''
		The function that updates the cooordinates of all the bounding boxes of the second object in line with the keyboard inputs.
		inputs: Node, [x,y,x,y]
		'''
		# increase the current node's value
		for i in range(4):
			node.data[i] += delta[i]		
		# recursively call function on left child, if it exists
		if node.left:
			self.increase_tree_values(node.left, delta)
		# recursively call function on right child, if it exists
		if node.right:
			self.increase_tree_values(node.right, delta)
		print(node.data)
		print(delta)


	def collision_check(self,le,ri): 
		'''
		This function checks if the rectangles/ bounding volumes are overlapping with each other. 
		input: Node1 and Node 2
		output: True/False
		'''
		if le or ri:
			l,r = le.data,ri.data
			if (l[0]>=r[2]) or (l[2]<=r[0]) or (l[3]<=r[1]) or (l[1]>=r[3]):
				collision = False
			else:
				print("Collision condition True")
				if l == [0,0,321,277]:
					print("Collision at Node A")
				elif l == [0,0,146,277]:
					print("Collision at Node B")
				elif l == [146,0,321,277]:
					print("Collision at Node C")
				elif l == [0,0,146,106]:
					print("Collision at Node D")
				elif l == [0,106,146,277]:
					print("Collision at Node E")
				elif l == [146,0,291,106]:
					print("Collision at Node F")
				elif l == [146,106,321,277]:
					print("Collision at Node G")
				
				collision = True
		return collision

	def BoundingVolumeParent(self,a,x):	
		'''
		Recurssive functions to check collisiion throughout the bounding volume test tree
		'''					
		b,c = a.left, a.right
		if b:
			if self.collision_check(b,x): 
				self.BoundingVolumeChild(b,x)
		if c:
			if self.collision_check(c,x):
				self.BoundingVolumeChild(c,x)
				
	def BoundingVolumeChild(self,b,x):
		'''
		Recurssive functions to check collisiion throughout the bounding volume test tree
		'''
		y,z = x.left, x.right
		if y:
			if self.collision_check(b,y):
				self.BoundingVolumeParent(b,y)
		if z:
			if self.collision_check(b,z):
				self.BoundingVolumeParent(b,z)
			

def main():
	"""
	Main function.
	Contains all the code related to visualization and starts the collision checking
	"""
	#initializes pygame
	pygame.init()
	
	#set up the display surface wrt the dimensions.
	display_surface = pygame.display.set_mode((800, 800))
	white = (255, 255, 255)
	green = (0, 255, 0)
	blue = (0, 0, 128)
	black = (0, 0, 0)
	red = (255, 0, 0)
	yellow=(255,255,0)

	#Hardcoded coordinates of the two polygons
	polytwo_points = [[446, 50], [591, 106],[591, 277],[446,277], [356, 177], [356, 86]]
	polyone_points = [(146, 0), (291, 106),(321, 277), (56, 277), (0, 106)]

	x,y = 0,0
	
	#BOunding volume of first polygon
	root = Node([0,0,321,277]) #Node A
	root.insert([0,0,146,277])  #Node B
	root.insert([146,0,321,277]) #Node C
	root.insert([0,0,146,106]) #Node D
	root.insert([0,106,146,277]) #Node E
	root.insert([146,0,291,106]) #Node F
	root.insert([146,106,321,277]) #Node G

	#Initial coordinates for the bounding box.
	Bv1 = [[351,45],[586,272]]
	Bv2 = [[351,45],[441,272]]
	Bv3 = [[441,45],[586,272]]

	#Bounding volume of second polygon
	root2 = Node([356,50,591,277]) #Node X
	root2.insert([356,50,446,277]) #Node Y	
	root2.insert([446,50,591,277]) #Node Z

	
	width = -1
	#Start visualization
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()        

			#Check for the keyboard event and move the polygon and the bounding boxes as required.
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT: 
					x = -10
				elif event.key == pygame.K_RIGHT: 
					x = 10
				elif event.key == pygame.K_UP: 
					y = -10
				elif event.key == pygame.K_DOWN: 
					y = 10

				#Display or hide the bounding boxes
				if event.key == pygame.K_LCTRL:
					width = 5
				elif event.key == pygame.K_LSHIFT:
					width =-1
				#Update the points to move the polygon and bounding boxes
				for point in polytwo_points:
					point[0] += x
					point[1] += y
				for point in Bv1:
					point[0] += x
					point[1] += y
				for point in Bv2:
					point[0] += x
					point[1] += y
				for point in Bv3:
					point[0] += x
					point[1] += y
				#Function called to change the coordinates of the second object in its tree wrt to amount moved
				root2.increase_tree_values(root2,[x,y,x,y])
				x,y=0,0

		display_surface.fill(white)
		
		#Drawing polygon one
		pygame.draw.polygon(display_surface, blue, polyone_points)
		#Drawing bounding boxes of polygon one
		pygame.draw.rect(display_surface,black,(0,0,327,287),width) #Node A
		pygame.draw.rect(display_surface,green,(0,0,149,287),width-2) #Node B
		pygame.draw.rect(display_surface,green,(143,0,175,287),width-2) #Node C
		#################################################################
		pygame.draw.rect(display_surface,red,(0,0,146,111),width-3) #Node D
		pygame.draw.rect(display_surface,red,(0,106,146,181),width-3) #Node E
		pygame.draw.rect(display_surface,red,(141,0,145,111),width-3)#Node F
		pygame.draw.rect(display_surface,red,(146,106,175,181),width-3) #Node G
		#################################################################
		
		#Drawing Polygon two
		pygame.draw.polygon(display_surface, red, polytwo_points)
		#Drawing bounding boxes of polygon two
		pygame.draw.rect(display_surface,yellow,(Bv1[0][0],Bv1[0][1],245,237),width) #Node X
		#################################################################
		pygame.draw.rect(display_surface,green,(Bv2[0][0],Bv2[0][1],95,237),width-3) #Node Y
		pygame.draw.rect(display_surface,blue,(Bv3[0][0],Bv3[0][1],150,237),width-3) #Node Z
		# #################################################################


		if root.collision_check(root,root2):
			root.BoundingVolumeParent(root,root2)
		# 
		
		# Draws the surface object to the screen. 
		pygame.display.update() 
		

if __name__ == "__main__":
	main()