from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins

from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def create(self, request, *args, **kwargs):
        response = {
            "url": request.get_full_path(),
            "version": request.version,
            "message": "",
            "errors": []
        }
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid()
        if not is_valid:
            errors = []
            for col, err in serializer.errors.items():
                errors.append({col: f"{err}"})
            response["message"] = "Failed to create the workout entry!"
            response["errors"]  = errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response["message"] =  "Successfully created the workout entry!"
        print(f"API Version: {request.version}")
        return Response(response, status=status.HTTP_200_OK, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print(f"API Version: {request.version}")
        response = {
            "url": request.get_full_path(),
            "version": request.version,
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        print(f"API Version: {request.version}")
        return super().retrieve(request, *args, **kwargs)

