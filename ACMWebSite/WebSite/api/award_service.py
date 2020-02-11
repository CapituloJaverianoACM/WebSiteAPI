from ACMWebSite.WebSite.models import Award


def get_awards():
	return Award.objects.all()
