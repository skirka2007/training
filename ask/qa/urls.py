from qa.views import test

urlpatterns = [
	#any URL	
	url(r'.', test, name='test'),
]


