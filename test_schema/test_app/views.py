from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from test_app.models import *

def main(request):
	"""Main listing."""
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)

	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	print request.tenant.schema_name
	return render_to_response("list.html", dict(posts=posts, user=request.user),context_instance = RequestContext(request))
