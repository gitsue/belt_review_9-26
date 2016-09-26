from django.shortcuts import render, redirect
from ..users.models import User
from .models import Poke
from django.db.models import Sum

# Create your views here.
def index(request):
	if "user_id" not in request.session:
		return redirect("login_page")

	print Poke.pokeMgr.all()

	context = {
		"curr_user": User.objects.get(id=request.session["user_id"]),
		"users": User.objects.exclude(id=request.session["user_id"]).annotate(total_count=Sum("pokee__count")),
		# "users_poked_you": Poke.pokeMgr.filter(pokee=request.session["user_id"])
	}

	return render(request, "pokes/index.html", context)

def create_poke(request, pokee_id):
	poker_id = request.session["user_id"]
	Poke.pokeMgr.add_poke(pokee_id, poker_id)
	return redirect('index')
