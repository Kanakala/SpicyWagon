try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import RestaurantForm, MenuForm, DishForm
from .models import Restaurant, Menu, Dish




def restaurant_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = RestaurantForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "restaurant_form.html", context)


def restaurant_detail(request, slug=None):
	
    instance = get_object_or_404(Restaurant, slug=slug)
    
    form = MenuForm()
    form1 = DishForm()
    
    if request.method=='POST':
        
        if 'Menu1' in request.POST:
            form = MenuForm(request.POST or None)
            
            if form.is_valid():
                #Restaurant_instance = Restaurant.objects.get( id = form.cleaned_data.get('restaurant_id') )
                menu = form.save(commit=False)
                menu.Restaurant = instance
                #Menu_Name = form.cleaned_data.get('Menu')
                menu.user = request.user
                #menu = Menu.objects.get_or_create(Restaurant=Restaurant_Name, Menu=Menu_Name, user=user)
                #menu_item = form.save(commit=False)
                #menu_item.save()
                menu.save()   
                return HttpResponseRedirect(instance.get_absolute_url())
            
        elif 'Dish1' in request.POST:
            form1 = DishForm(request.POST or None)        
            if form1.is_valid():
                dish = form1.save(commit=False)
                dish.user = request.user
                dish.Restaurant = instance
                dish.Menu = get_object_or_404(Menu, id=request.POST['menu_id'])
                dish.save()
                return HttpResponseRedirect(instance.get_absolute_url())

        #return HttpResponseRedirect(new_dish.content_object.get_absolute_url())
    else:
        form = MenuForm()
        form1 = DishForm()
    
    context = {
        "instance":instance,
		"menu_form" : form,
        "dish_form" : form1,
	}
	
    return render(request, "restaurant_detail.html", context)

def restaurant_list(request):
	queryset_list = Restaurant.objects.active() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Restaurant.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(Restaurant__icontains=query)|
				Q(user__username__icontains=query) |
				Q(user__email__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"Restaurant": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "restaurant_list.html", context)
	





def restaurant_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Restaurant, slug=slug)
	form = RestaurantForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"Restaurant": instance.Restaurant,
		"instance": instance,
		"form":form,
	}
	return render(request, "restaurant_form.html", context)



def restaurant_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Restaurant, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("restaurants:list")

def menu_delete(request, id):
    #obj = get_object_or_404(Comment, id=id)
    # obj = CommentFormmment.objects.get(id=id)
    try:
        obj = Menu.objects.get(id=id)
    except:
        raise Http404

    if obj.user != request.user:
        #messages.success(request, "You do not have permission to view this.")
        #raise Http404
        reponse = HttpResponse("You do not have permission to do this.")
        reponse.status_code = 403
        return reponse
        #return render(request, "confirm_delete.html", context, status_code=403)

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(parent_obj_url)
    context = {
        "object": obj
    }
    return render(request, "confirm_delete.html", context)

def menu_thread(request, id):
    #obj = Comment.objects.get(id=id)
    try:
        obj = Menu.objects.get(id=id)
    except:
        raise Http404

    if not obj.is_parent:
        obj = obj.parent

    content_object = obj.content_object # Post that the comment is on
    content_id = obj.content_object.id

    initial_data = {
            "content_type": obj.content_type,
            "object_id": obj.object_id
    }
    form = MenuForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get("Menu")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Menu.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()


        new_menu, created = Menu.objects.get_or_create(
                            user = request.user,
                            content_type= content_type,
                            object_id = obj_id,
                            Menu = content_data,
                            parent = parent_obj,
                        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


    context = {
        "menu": obj,
        "form": form,
    }
    return render(request, "menu_thread.html", context)
	
