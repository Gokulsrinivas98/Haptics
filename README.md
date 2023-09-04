# Bounding Volume Hierarchy based Collision detection in two dimensions

## Description:
The project aims to find if two polygons are colliding with each other using Bounding Volume Hierarchy. The
polygons are two dimensional and the entire calculation is done on x and y axes.
Following Assumptions are considered:
- The bounding volumes are hard coded.
- The vertices of the polygons are also hard coded. 

## Objects, data structures, and algorithms used.
### Polygon Generation:
<details>
<summary>:eyes: Show Details</summary>
The vertices of the polygons are user provided. These coordinates are then used by pygame to draw the
polygons. This is done in an infinite loop block, that keeps constantly checking for a keyboard input. When the
keyboard inputs UP,DOWN, LEFT and RIGHT happen, the calls are used to store the changes in coordinates of
the second polygon. These change in coordinate list then used to update the coordinates in the root of the second
polygon’s binary tree.
  </details>
  
### Bounding Volume Hierarchy:
<details>
<summary>:eyes: Show Details</summary>
Since the bounding volumes are hard coded, the bounding volume hierarchy is manually created with the top
left and bottom right coordinates of individual bounding volumes. A 3 level bounding volume hierarchy was
created for the blue polygon and a two level bounding volume hierarchy was created for the red polygon.
</details>

### Bounding Volume Test Tree:
<details>
<summary>:eyes: Show Details</summary>
Running time simultaneous recursive traversal of the two BVHs results in a bounding volume test tree. The tree
obtained is as follows. The tree is then traversed in a Depth First Search method to find the colliding leaf nodes.
</details>

### Collision Check:
<details>
<summary>:eyes: Show Details</summary>
A simple function that checks if two rectangles are overlapping each other. If they are then it will return True.
Else False. Here the two rectangles are the bounding boxes of the polygons, say D and Y. 
</details>

## Output
![App Screenshot](haptics.GIF)
