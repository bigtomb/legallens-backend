from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Analysis
from .serializers import DocumentSerializer, AnalysisSerializer
from .utils import extract_text_from_file, process_text_with_chatgpt



class StoreAnalysis(generics.CreateAPIView):
    serializer_class = AnalysisSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class ProcessDocumentView(generics.CreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Validate input
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['document']
            file_path = file.temporary_file_path() if hasattr(file, 'temporary_file_path') else file
            text = extract_text_from_file(file_path)
            summary = process_text_with_chatgpt(text)

            return Response(summary, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
