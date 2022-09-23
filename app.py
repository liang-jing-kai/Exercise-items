'''
import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("居住证模板1.png") # 导入我们需要添加水印的图片
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blank_img = np.zeros(shape=(RGB_img.shape[0],RGB_img.shape[1],3), dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
# 添加水印的文字内容
cv2.putText(blank_img,text='Learn Python',org=(40, 90),
            fontFace=font,fontScale= 2,
            color=(255,0,0),thickness=10,lineType=cv2.LINE_4)

blended = cv2.addWeighted(src1=RGB_img, alpha=0.7,
                          src2=blank_img, beta=1, gamma = 2)
plt.imshow(blended)
'''
import xlwings as xw
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

app = xw.App(visible=False, add_book=False)
wb = app.books.open('py_mian\\tian.xlsx') # 打开Excel文件
sheet = wb.sheets[0]  # 选择第0个表单，也可以使用wb.sheets['sheet1']指定sheet的名字
# 将A1到A2的值，读取到a列表中
name_list = sheet.range('A2:A200').value
Gender_list = sheet.range('B2:B200').value
nation_list = sheet.range('C2:C200').value
sfz_nb_list = sheet.range('D2:D200').value
huji_list = sheet.range('E2:E200').value
xz_dz1_list = sheet.range('I2:I200').value
xz_dz2_list = sheet.range('J2:J200').value
yxq1_list = sheet.range('K2:K200').value
yxq2_list = sheet.range('L2:L200').value

xz_dz2_list = [x or '' for x in xz_dz2_list]
# print(xz_dz2_list)


for Name,Gender,nation,sfz_nb,huji,xz_dz1,xz_dz2,yxq1,yxq2 in zip(name_list,Gender_list,nation_list,sfz_nb_list,huji_list,xz_dz1_list,xz_dz2_list,yxq1_list,yxq2_list):
    im = Image.open('居住证模板1.png')
    draw = ImageDraw.Draw(im)
    # Name = "陈梓欣"
    # Gender = '女'
    # nation = '汉族'
    # sfz_nb = '440881199108131067'
    # huji = '广东省遂溪县'
    # xz_dz = '广东省深圳市宝安区沙井街道新桥样下五区\n五巷5020房'
    # yxq1 = '2019年05月15日'
    # yxq2 = '2020年05月15日'
    # 判断NoneType
    if xz_dz2_list == 'NoneType':
        xz_dz2_list = ' '
    # 设置字体、字体大小等等
    font = ImageFont.truetype('py_mian\\jzz_ziti.TTF', 26)

    # 添加文字(x,y)
    # 姓名1
    draw.text((640, 730), Name, fill="#000000",font=font)
    # 性别2
    draw.text((640, 775), Gender, fill="#000000",font=font)
    # 民族3
    draw.text((770, 775), nation, fill="#000000",font=font)
    # 身份证4
    draw.text((640, 825), sfz_nb, fill="#000000",font=font)
    # 户籍地5
    draw.text((640, 873), huji, fill="#000000",font=font)
    # 现居住地址6
    draw.text((640, 925), xz_dz1, fill="#545141",font=font)
    draw.text((640, 950), xz_dz2, fill="#545141",font=font)
    # 有效期（前）7
    draw.text((640, 980), str(yxq1), fill="#545141",font=font)
    # 有效期（后）8
    draw.text((880, 980), str(yxq2), fill="#545141",font=font)
    # im.show()



    # from PIL import Image
    # #创建底图
    # target = Image.new('RGBA', (300, 300), (0, 0, 0, 0))

    #打开头像
    nike_image = Image.open("new_photo\\"+Name+".png")
    nike_image.convert("RGBA")
    nike_image = nike_image.resize((162, 200))
    # #打开装饰
    # hnu_image = Image.open("cat.jpg")
    # # 分离透明通道
    # r,g,b=hnu_image.split()
    # # 将头像贴到底图

    im.paste(nike_image, (965,703),mask=nike_image)
    #
    # #将装饰贴到底图
    # hnu_image.convert("RGBA")
    # target.paste(hnu_image,(0,0))
    # im = im.convert("RGB")
    # 预览图片
    # im.show()
    # 保存图片
    im.save('new_certificate\\'+Name+'居住证.png')