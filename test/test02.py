import os

# dirname = r"D:\FFOutput"
dirname = r"G:\金庸有酒我有杯_mp3"
List = os.listdir(dirname)
for i in List:
    abs_path = os.path.join(dirname, i)
    i = i[5:]
    i = i.replace("》：", "_",)
    new = os.path.join(dirname, i)
    os.rename(abs_path, new)
    # new_name = input(i[:-4]+" 更改: ")
    # if len(new_name)>3:
    #     new = os.path.join(dirname, new_name+".mp3")
    #     os.rename(abs_path, new)
    #     print(new)

