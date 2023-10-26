from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import cv2
from io import BytesIO


def get_image2text(processor, model):
    # cap = cv2.VideoCapture(0)
    # frame = cap.read()[1]
    # cv2.imwrite('Frame.png', frame)
    # cap.release()
    print('开始图像采集')
    # processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
    # model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")

    with open('Frame.png', 'rb') as fp:
        img_bytes = fp.read()  # 'b'二进制读取
    if not img_bytes.endswith(b'\xff\xd9'):
        img_bytes = img_bytes + b'\xff\xd9'
    image = Image.open(BytesIO(img_bytes))

    # image = Image.open('Frame.png')

    # show_image = cv2.imread('Frame.png')
    # cv2.imshow('Image', show_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print('图像处理中......')
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=30)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_caption
