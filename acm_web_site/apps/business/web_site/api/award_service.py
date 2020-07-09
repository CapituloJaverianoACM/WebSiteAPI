from acm_web_site.apps.business.web_site.models import Award


def get_awards():
	return Award.objects.all()
