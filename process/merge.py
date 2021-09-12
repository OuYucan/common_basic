from common.utils.customer import MyFile


if __name__ == "__main__":
    dirname = r"D:\DataSource\Bilibili_data - 副本"
    mf = MyFile()
    df = mf.concat_same_dir(dirname,suffix="xlsx")
    df.to_excel("../resource/excel/merge.xlsx", index=False)
    print('end')