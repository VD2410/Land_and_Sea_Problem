import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--name",default="sample.txt",
    help="path to name file")
args = vars(ap.parse_args())
name = args["name"]


data_map = open(name,'r')
num_list = list()

rectangle = []
for i in data_map:

    num = i.split()
    num_list = list()


    for n in num:

        # print(float(n))

        num_list.append((float(n))) 

    if len(num_list)<4:

        num_of_rectangle = num_list

        continue

    rectangle.append(num_list)



# print(rectangle)

min_containing = []

for rect1 in rectangle:

    containing = []
    i=0
    for rect2 in rectangle:
        if rect1[0]<rect2[0] and rect1[1]<rect2[1] and rect1[2]<rect2[2] and rect1[3]<rect2[3]:
            containing.append(i)
        i=i+1
    # result.append(containing)

    areas = []

    # print(containing)


    for x in containing:

        area = (rectangle[x][2] - rectangle[x][0]) * (rectangle[x][3] - rectangle[x][1])
        areas.append(area)

    if len(areas)>=1:

        # print(min(areas))

        # print(containing[areas.index(min(areas))])

        min_containing.append(containing[areas.index(min(areas))])

    else:

        min_containing.append(-1)


# print(min_containing)
depth=[]
i = 0
for num in min_containing:
    val = 0


    if min_containing[i] == -1:
        depth.append(val)
    else:
        val = val + 1
        num = min_containing[i]
        while min_containing[num] != -1:
            val = val+1
            num = min_containing[num]

        depth.append(val)

    i = i+1

print(len([i for i in depth if i%2==0])," areas are found to be land" )