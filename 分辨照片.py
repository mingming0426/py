import os
import cv2
from PIL import Image
import face_recognition
import paramiko
from smb.SMBConnection import SMBConnection

# 把输入路径中的图片文件找出，并返回包含所有图片文件名的数组
def list_files(startpath):
    wzlj = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if is_image_file(file):
                wzlj.append(os.path.join(root, file))

    print("找到了 {} 个图片文件".format(len(wzlj)))
    return wzlj


# 调用fr库进行人脸识别
def face(img):
    image = face_recognition.load_image_file(img)
    print("正在识别图片：" + img)
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) > 0:
        print(img + "找到了 {} 张脸.".format(len(face_locations)))

        # for face_location in face_locations:
        #     # Print the location of each face in this image
        #     top, right, bottom, left = face_location
        #     print(
        #         "脸的位置在 上: {}, 左: {}, 下: {}, 右: {}".format(top, left, bottom,
        #                                                            right))
        #
        #     # You can access the actual face itself like this:
        #     face_image = image[top:bottom, left:right]
        #     pil_image = Image.fromarray(face_image)
        #     pil_image.show()
        return True
    else:
        return False


def faceCV2(img):
    print("正在CV2识别图片：" + img)
    # 读取测试图片
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    # 将原彩色图转换成灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(r'E:\\codes\\conf\\haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.17, minNeighbors=7)

    if len(faces) > 0:
        print(img + "找到了 {} 张脸.".format(len(faces)))
        return True
    else:
        return False


# 将输入的绝对路径的文件，名字前面加A
def changeFileNmae(file_path):
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 分割文件路径和文件名
        directory, filename = os.path.split(file_path)
        # 构建新的文件名
        new_filename = "A" + filename
        # 构建新的文件路径
        new_file_path = os.path.join(directory, new_filename)

        # 重命名文件
        os.rename(file_path, new_file_path)
        print(f"文件名修改: {file_path} -> {new_file_path}")
    else:
        print(f"没找到文件: {file_path}")


def is_image_file(file_path):
    # 图片扩展名的列表
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif']

    # 获取文件的扩展名
    file_extension = os.path.splitext(file_path)[1].lower()

    # 检查扩展名是否在图片扩展名的列表中
    return file_extension in image_extensions


def do_Files(startpath):
    # 找到文件夹中的所有文件
    plist = list_files(startpath)
    # 逐个文件调用人脸识别程序识别
    for i in plist:
        if face(i):
            # 把有人脸的图片，将文件名前面加上A
            changeFileNmae(i)


def ssh_do_files(nasStartpath, localTempPath):
    # 定义NAS设备的连接信息
    nas_ip = '192.168.27.77'  # NAS设备的IP地址
    nas_username = 'winefox'  # 登录NAS的用户名
    nas_password = 'tt101009'  # 登录NAS的密码
    # 创建SFTP客户端
    ssh = paramiko.SSHClient()
    ssh.connect(nas_ip, username=nas_username, password=nas_password)
    sftp = ssh.open_sftp()
    # 连接到NAS设备


    # 定义要操作的NAS上的目录路径
    for filename in sftp.listdir(nasStartpath):
        local_file_path = os.path.join(localTempPath, filename)
        # 获取文件绝对路径
        file_path = nasStartpath + '/' + filename
        # 下载文件
        sftp.get(file_path, local_file_path)
        if face(local_file_path):
            print(file_path)
            # 把有人脸的图片，将文件名前面加上A
            # 重命名文件
            # sftp.rename(file_path, "A"+file_path)

    # 关闭连接
    sftp.close()


# 主程序
startPath = "E:\\codes\\testFiles"
do_Files(startPath)

# sshStartpath = "\\Newnas\photo\湉湉13Y"
# localTempPath = "E:\\codes\\testFiles"
# ssh_do_files(sshStartpath, localTempPath)
