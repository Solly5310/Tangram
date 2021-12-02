import sys
import numpy as np
import math

import collections

class TangramPiecesError(Exception):
    pass


import numpy as np
import math


angle_list = []

list_test = []
list_clockwise_test=[]
dict_shape = {}
direction = 0
degree_check = 0



shape_list_1 = []
area_list = []
big_shape = []
big_shape_dict={}

def gradient_finder(x,x_1):
    gradient = (x_1[1]-x[1])/(x_1[0]-x[0])
    return gradient

def getYIntercept(x,x_1):
    m = gradient_finder(x, x_1)
    b = x[1]-m*x[0]
    return int(b),int(m)


def area_calc(coord):
    coord = np.array(coord)
    coord = coord.reshape(-1,2)

    x = coord[:,0]
    y = coord[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return int(area)
def reorder(lst, pos):
    return lst[pos:] + lst[:pos]


def angle_finder(point_1,point_2,point_3):
    a = np.array(point_1)
    b = np.array(point_2)
    c = np.array(point_3)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

def available_coloured_pieces(file,shape_list,shape_list_title):
    for x in file:
        if '<svg' in x or 'M' not in x:
            continue
        elif '</svg' in x or 'M' not in x:
            break
        else:
            shape_list.append(x)
    for y in range(len(shape_list)):
        shape_list_title.append(shape_list[y][shape_list[y].find('fill=')+6:-4])
        shape_list[y] = shape_list[y][shape_list[y].index("M")+2:shape_list[y].index("z")-1]
        shape_list[y] = shape_list[y].split(" L ")
        for z in range(len(shape_list[y])):
            shape_list[y][z] = shape_list[y][z].strip()
            shape_list[y][z]=shape_list[y][z].split(' ')
            for c in range(2):
                shape_list[y][z][c] = int(shape_list[y][z][c])
    return shape_list, shape_list_title


def shape_check(shape_list_1, shape_list_2, shape_list_title_1, shape_list_title_2):
    if len(shape_list_1)!= len(shape_list_2):
        return False
    count=0
    for x in range(len(shape_list_1)):
        colour_type = shape_list_title_1[x]
        for z in range(len(shape_list_title_2)):
            if colour_type == shape_list_title_2[z]:
                count+=1
                p = compare_shapes(shape_list_1[x],shape_list_2[z])
                if p == False:
                    return False
    if count != len(shape_list_1):
        return False
    return True

def are_valid(list_test):
    for c in list_test:
        contains_duplicates = any(c.count(element) > 1 for element in c)
        if len(c)<3:
            raise TangramPiecesError("At least one piece is invalid")
        elif contains_duplicates:
            raise TangramPiecesError("At least one piece is invalid")
        degree_check = (len(c) - 2) * 180
        point_left_top_most = sorted(c)[0]
        point_position = c.index(point_left_top_most)
        c=reorder(c, point_position)
        c = c[:] + c[0:2]
        for x in range(len(c)-2):
            angle_list.append(angle_finder(c[x],c[x+1],c[x+2]))
            if angle_list[x] >= 180:
                raise TangramPiecesError("At least one piece is invalid")
        if int(round(sum(angle_list))) != degree_check:
            raise TangramPiecesError("At least one piece is invalid")
        angle_list.clear()
    return True

def compare_shapes(shape_list_1, shape_list_2):
    if len(shape_list_1) != len(shape_list_2):
        return False
    shape_list_1 = shape_list_1[:] + shape_list_1[:1]
    shape_list_2 = shape_list_2[:] + shape_list_2[:1]
    distance_list_1 = []
    distance_list_2 = []
    if len(shape_list_1) != len(shape_list_1):
        return False
    for coord in range(len(shape_list_1)-1):
        distance_list_1.append(
            int(math.sqrt(((shape_list_1[coord][0] - shape_list_1[coord + 1][0]) ** 2) +
                          ((shape_list_1[coord][1] - shape_list_1[coord + 1][1]) ** 2))))
        distance_list_2.append(
            int(math.sqrt(((shape_list_2[coord][0] - shape_list_2[coord + 1][0]) ** 2) +
                          ((shape_list_2[coord][1] - shape_list_2[coord + 1][1]) ** 2))))
    if collections.Counter(distance_list_1) != collections.Counter(distance_list_2):
        return False
    angle_list_1 = []
    angle_list_2 = []
    shape_list_1 = shape_list_1[:] + shape_list_1[1:2]
    shape_list_2 = shape_list_2[:] + shape_list_2[1:2]
    for x in range(len(shape_list_1) - 2):
        angle_list_1.append(angle_finder(shape_list_1[x], shape_list_1[x + 1], shape_list_1[x + 2]))
        angle_list_2.append(angle_finder(shape_list_2[x], shape_list_2[x + 1], shape_list_2[x + 2]))
    if collections.Counter(distance_list_1) != collections.Counter(distance_list_2):
        return False







def area_check(shape_list, big_shape):
    for x in shape_list:
        area_list.append(area_calc(x))
    sum_area_list = int(round(sum(area_list)))
    area_big_shape = area_calc(big_shape)
    if sum_area_list != area_big_shape:
        return False
    return


def shape_edge_finder(big_shape, shape_range_dict,default=True):
    points_list = []
    point_list_revised = []
    if default:
        big_shape = big_shape[0]
    big_shape = big_shape[:]+big_shape[0:1]
    for y in range(len(big_shape)-1):
        if big_shape[y][0] == big_shape[y+1][0]:
            if big_shape[y][1]<big_shape[y+1][1]:
                for y_point in range(big_shape[y][1], big_shape[y + 1][1] + 1):
                    points_list.append([big_shape[y][0],y_point])
            elif big_shape[y][1] > big_shape[y + 1][1]:
                 for y_point in range(big_shape[y+1][1], big_shape[y][1] + 1):
                     points_list.append([big_shape[y][0], y_point])
        elif big_shape[y][1] == big_shape[y+1][1]:
            points_list.append(big_shape[y])
            points_list.append(big_shape[y+1])
        else:
            gradient_list=getYIntercept(big_shape[y],big_shape[y+1])
            if big_shape[y][0] < big_shape[y + 1][0]:
                for x in range(big_shape[y][0], big_shape[y + 1][0] + 1):
                    points_list.append([x, (gradient_list[1]*x+gradient_list[0])])
            elif big_shape[y][0] > big_shape[y + 1][0]:
                for x in range(big_shape[y + 1][0], big_shape[y][0] + 1):
                    points_list.append([x, (gradient_list[1] * x + gradient_list[0])])
    for i in points_list:
        if i not in point_list_revised:
            point_list_revised.append(i)
    point_list_revised = sorted(point_list_revised, key = lambda x: (-x[1], x[0] ))
    for i in range(len(point_list_revised)-1):
        if point_list_revised[i][1]==point_list_revised[i+1][1]:
            if point_list_revised[i][1] in shape_range_dict.keys():
                shape_range_dict[point_list_revised[i][1]] += point_list_revised[i][0], point_list_revised[i + 1][0]
            else:
                shape_range_dict[point_list_revised[i][1]]=point_list_revised[i][0],point_list_revised[i+1][0]
    for i in range(len(point_list_revised)):
            if point_list_revised[i][1] not in shape_range_dict.keys():
                shape_range_dict[point_list_revised[i][1]] = point_list_revised[i][0]
    return shape_range_dict,point_list_revised

def shape_checker_edges(shape_list, big_shape_dict,default=True):
    point_count=0
    for shape in shape_list:
        if default:
            for shape_point in shape:
                if shape_point[1] in big_shape_dict.keys():
                    if type(big_shape_dict[shape_point[1]]) != int:
                        if len(big_shape_dict[shape_point[1]]) >=2:
                            if big_shape_dict[shape_point[1]][0]<=shape_point[0]<=big_shape_dict[shape_point[1]][-1]:
                                point_count +=1
                    elif type(big_shape_dict[shape_point[1]]) == int:
                        if big_shape_dict[shape_point[1]] == shape_point[0]:
                            point_count +=1
        else:
            if shape[1] in big_shape_dict.keys():
                if type(big_shape_dict[shape[1]]) != int:
                    if big_shape_dict[shape[1]][0]<shape[0]<big_shape_dict[shape[1]][-1]:
                        return False
        if default:
            if point_count != len(shape):
                return False
            else:
                point_count = 0


def small_shape_checker(shape_list):
    for z in shape_list:
        shape_list_dict={}
        shape_edge_finder(z,shape_list_dict,False)
        for y in shape_list:
            if z==y:
                continue
            else:
                shape_checker_edges(y,shape_list_dict,False)


class TangramShape:

    def __init__(self, file_name):
        self.tangram_shape_list = []
        self.tangram_shape_list_title = []
        self.tangram_dict = {}
        shape_name = file_name
        self.file_name = open(shape_name)
        available_coloured_pieces(self.file_name, self.tangram_shape_list, self.tangram_shape_list_title)

    def has_as_solution(self, comparison_class):
        check = area_check(comparison_class.tangram_shape_list, self.tangram_shape_list)
        if check is False:
            return False
        shape_edge_finder(self.tangram_shape_list, self.tangram_dict)
        check = shape_checker_edges(comparison_class.tangram_shape_list, self.tangram_dict)
        if check is False:
            return False
        check = small_shape_checker(comparison_class.tangram_shape_list)
        if check is False:
            return False
        else:
            return True

    def are_identical_to(self, comparison_class):
        self.outcome = shape_check(self.tangram_shape_list, comparison_class.tangram_shape_list,self.tangram_shape_list_title, comparison_class.tangram_shape_list_title)
        return self.outcome

class TangramPieces(TangramShape):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.is_valid = are_valid(self.tangram_shape_list)

