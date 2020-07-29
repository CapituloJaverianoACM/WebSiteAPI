from django.shortcuts import render
from django.http import HttpResponse

from .serializers import (
    ActivitySerializer,
    ConfirmActivitySerializer,
    TutorialSerializer,
    ProjectSerializer
)

from ..people.serializers import MemberSerializer
from rest_framework.views import APIView
from .services import (
    get_activity,
    get_all_activities,
    create_activity_member,
    get_project,
    get_projects,
    get_tutorial,
    get_tutorials
)

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

# Create your views here.


class ActivityList(APIView):

    def get(self, request):
        activities_serializer = ActivitySerializer(
            get_all_activities(),
            many=True
        )
        return Response(
            activities_serializer.data,
            status=status.HTTP_200_OK
        )


class ActivityDetail(APIView):

    def get(self, request, id):
        activity = get_activity(id)
        activity_serializer = ActivitySerializer(activity)
        if activity_serializer:
            return Response(activity_serializer.data)
        else:
            errors = dict(message='La actividad no se ha encontrado')
            return Response(
                errors,
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, id):
        id_member = request.data.get("id")
        role = request.data.get("role")
        activity = create_activity_member(
            id_activity=id, id_member=id_member, role=role)
        activity_serializer = ActivitySerializer(activity)
        if activity_serializer:
            return Response(activity_serializer.data)
        else:
            errors = dict(
                message='No se pudo asociar el miembro a la actividad')
            return Response(
                errors,
                status=status.HTTP_404_NOT_FOUND
            )
    # TODO: Handle all info received from form
    # TODO: Save the many to many relationship in serializer


# TODO: find out what this view is for
class ConfirmActivityView(GenericAPIView):
    serializer_class = ConfirmActivitySerializer

    def post(self, request, uidb64=None, token=None):
        serializer_data = self.request.data
        serializer_data.update({
            'uidb64': uidb64,
            'token': token
        })
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        # TODO: Add logic to confirm the assistance
        """
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
        password = serializer.data.get('password1')
        user.set_password(password)
        user.save()
        """
        return Response('OK')


class TutorialList(APIView):

    def get(self, request):
        tutorial_serializer = TutorialSerializer(
            get_tutorials(),
            many=True
        )
        return Response(
            tutorial_serializer.data,
            status=status.HTTP_200_OK
        )


class TutorialDetail(APIView):

    def get(self, request, id):
        tutorial = get_tutorial(id=id)
        tutorial_serializer = ProjectSerializer(tutorial)
        return Response(
            tutorial_serializer.data,
            status=status.HTTP_200_OK
        )


class ProjectList(APIView):

    def get(self, request):
        project_serializer = ProjectSerializer(
            get_projects(),
            many=True
        )
        return Response(
            project_serializer.data,
            status=status.HTTP_200_OK
        )


class ProjectDetail(APIView):

    def get(self, request, id):
        project = get_project(id=id)
        project_serializer = ProjectSerializer(project)
        return Response(
            project_serializer.data,
            status=status.HTTP_200_OK
        )


def page_not_found(request, exception):
    return render(request=request, template_name='404.html', status=400)
