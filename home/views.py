from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import numpy as np
import cv2
# from tensorflow.keras.models import load_model
# from core.settings import model
# Dictionary of letter mappings

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Handle(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        file_obj = request.FILES['image']
        nparr = np.frombuffer(file_obj.read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        try:
            from paddleocr import PaddleOCR

            # Khởi tạo đối tượng OCR
            ocr = PaddleOCR(lang="en")
            # Thực hiện OCR
            result = ocr.ocr(img)
            # Xử lý và vẽ các hộp bao quanh văn bản
            predicted_label=""
            for line in result:
                # print(line[0])
                for i in line:
                    # print("?")
                    box=i[0]
                    # predicted_label+=i[1][0]
                    print("ahihi: ",box)
                    print(i[1][0])
                    predicted_label+=i[1][0]+"\n"

            return Response({'prediction': predicted_label}, status=200)
        except Exception:
            print(Exception)
            return Response({'prediction': "null"}, status=200)