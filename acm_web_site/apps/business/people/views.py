from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from acm_web_site.apps.business.people.api import team_service
from acm_web_site.apps.business.people.serializer.member_serializer import MemberSerializer
from acm_web_site.apps.business.people.serializer.team_serializer import TeamSerializer
from acm_web_site.apps.business.web_site.models import Member
from rest_framework.response import Response
from rest_framework import status, viewsets


class TeamList(APIView):

	def get(self, request):
		teams_serializer = TeamSerializer(
			team_service.get_teams(),
			many=True
		)
		return Response(
			teams_serializer.data,
			status=status.HTTP_200_OK
		)


class MemberViewSet(viewsets.ViewSet):

	def get_queryset(self, filter=None, exclude=None, order_by=None):
		members = Member.objects.all()
		is_staff = self.request.query_params.get('isStaff', None)

		filter = filter or dict()

		if is_staff is not None:
			filter.update(dict(is_staff=is_staff))

		if exclude is not None and isinstance(exclude, dict):
			members = members.exclude(**exclude)
		if filter is not None and isinstance(filter, dict):
			members = members.filter(**filter)
		if order_by is not None and isinstance(order_by, list):
			members = members.order_by(*order_by)
		return members

	def list(self, request):
		member_serializers = MemberSerializer(
			self.get_queryset(),
			many=True
		)
		return Response(
			member_serializers.data,
			status=status.HTTP_200_OK
		)

	def create(self, request):
		member_serializer = MemberSerializer(data=self.request.data)
		if member_serializer.is_valid():
			member_serializer.create(member_serializer.data)
			return Response(
				member_serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			member_serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)


members = MemberViewSet.as_view(dict(get='list'))
join_us = MemberViewSet.as_view(dict(post='create'))