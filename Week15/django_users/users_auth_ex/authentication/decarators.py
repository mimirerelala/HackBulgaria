from functools import wraps

def login_required(redirect_url='/'):
	def decorator(func):
		@wraps(func)
		def _wrapped_view(request, *args, **kwargs):
			#print decorator
			#print session
			#seession email form request
			#if false = redirect
			#use req.session.get('', False)

			return func(request. *args, **kwargs)

		return _wrapped_view

	return decorator