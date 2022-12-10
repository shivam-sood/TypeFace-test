 
#  Since Input format is not specified I am assuming the following:(Input taken from using input() function)
# Input Format:
# M, N
# Pixel11 Pixel12 Pixel13 ... Pixel1N
# Pixel21 Pixel22 Pixel23 ... Pixel2N
# ..
# PixelM1 PixelM2 PixelM3 ... PixelMN

# Example Input:
"""
3 3
1 0 0
1 1 0
1 1 1
"""
# Output is a list of bounding boxes with each bounding box represented as a list of 4 elements where 1st element is the x coordinate(column number, one-indexed) of the center of the bounding box, 2nd element is the y coordinate(row number) of the center of the bounding box, 3rd element is the width of the bounding box and 4th element is the height of the bounding box.
# Top left pixel is 1,1   
# Bottom right pixel is N, M

input_matrix = []
row_num,col_num = map(int,input().split())
for i in range(int(row_num)):
    input_matrix.append(list(map(int,input().split())))

visited = [[False for i in range(col_num)] for j in range(row_num)]

def dfs(i,j, bounding_box):
    global input_matrix, visited, row_num, col_num
    if i < 0 or j < 0 or i >= row_num or j >= col_num:
        return
    if(visited[i][j]):
        return
    visited[i][j] = True
    if input_matrix[i][j] == 0:
        return
    bounding_box[0] = min(bounding_box[0], i)
    bounding_box[1] = min(bounding_box[1], j)
    bounding_box[2] = max(bounding_box[2], i)
    bounding_box[3] = max(bounding_box[3], j)
    dfs(i-1,j, bounding_box)
    dfs(i+1,j, bounding_box)
    dfs(i,j-1, bounding_box)
    dfs(i,j+1, bounding_box)
    return
bounding_boxes = []
for i in range(row_num):
    for j in range(col_num):
        if visited[i][j] == False and input_matrix[i][j] == 1:
            bounding_box_range = [row_num, col_num, 0, 0]
            dfs(i,j, bounding_box_range)
            actual_bounding_box = [1 + bounding_box_range[1] + (bounding_box_range[3] - bounding_box_range[1])//2,1 + bounding_box_range[0] + (bounding_box_range[2] - bounding_box_range[0])//2,  bounding_box_range[3] - bounding_box_range[1] + 1,bounding_box_range[2] - bounding_box_range[0] + 1]
            bounding_boxes.append(actual_bounding_box)
            
print(bounding_boxes)