from django.shortcuts import get_object_or_404
from Restaurant.api.serializers import DishListSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .forms import PnrSearchForm, TrainSearchForm
from django.forms.formsets import formset_factory
from .models import PnrSearch, TrainSearch
import json
from urllib.request import urlopen
from datetime import datetime, timedelta
import datetime
from dateutil.parser import parse
from Restaurant.models import Restaurant, Menu, Dish, SubMenu
from django.template import RequestContext, Template, loader
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404




def index(request):
	form1 = PnrSearchForm()
	form2 = TrainSearchForm()
	if request.method=='POST':
		if 'pnr' in request.POST:
			form1 = PnrSearchForm(request.POST or None)
			if form1.is_valid():
				pnr_instance = form1.save(commit=False)
				pnr_instance.save()
				return HttpResponseRedirect(pnr_instance.get_absolute_url())
		elif 'train' in request.POST:
			form2 = TrainSearchForm(request.POST or None)
			if form2.is_valid():
				train_instance = form2.save(commit=False)
				train_instance.save()
				return HttpResponseRedirect(train_instance.get_absolute_url())
	else:
		form1 = PnrSearchForm()
		form2 = TrainSearchForm()
    
	context = {
		"form1" : form1,
		"form2" : form2,
	}			
	
	return render(request, "index.html", context)
	
def pnrform(request):
	if request.method == "POST" and request.is_ajax():
		form = PnrSearchForm(request.POST or None)
		if form.is_valid():
			pnr_instance = form.save(commit=False)
			pnr = form.cleaned_data.get("Pnr")
			pnr_instance.save()
			return HttpResponseRedirect(pnr_instance.get_absolute_url())
		else:
			form = PnrSearchForm()
			
		data = { "Pnr": Pnr,
		}
		
		context = {
		"form" : form,
	}		
		return JSONResponse(data)
		
	return render(request, "index.html", context)
			

class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        Dish = Dish.objects.all()
        serializer = DishListSerializer(queryset, many=True)
        return Response(serializer.data)
		
def restaurant_list(request):
	# restaurants = Restaurant.objects.all()
	# to_json = []
	# for restaurant in restaurants:
		# restaurant_dict = {}
		# restaurant_dict['Restaurant'] = restaurant.Restaurant
		# restaurant_dict['Area'] = restaurant.Area
		# to_json.append(restaurant_dict)
	# response_data = json.dumps(to_json)
	# c = RequestContext(request,{'result':response_data})
	# t = loader.get_template("restaurant_list.html")
	return render(request, "restaurant_list.html")
	
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data, renderer_context={'indent':4})
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
	
def restaurant_json(request):
	restaurants = Restaurant.objects.all()
	to_json = []
	for restaurant in restaurants:
		restaurant_dict = {}
		restaurant_dict['Restaurant'] = restaurant.Restaurant
		restaurant_dict['Area'] = restaurant.Area
		restaurant_dict['image_path'] = restaurant.image_path
		restaurant_dict['slug'] = restaurant.slug
		to_json.append(restaurant_dict)
	# data = serializers.serialize('json', restaurants)
	# struct = json.loads(data)
	#response_data = json.loads(struct['results'])
	final_json = {'results':to_json}
	return JSONResponse(final_json)
	
def dish_json(request, slug):
	restaurant = get_object_or_404(Restaurant, slug=slug)
	to_json = []
	restaurant_dict = {}
	restaurant_dict['Restaurant'] = restaurant.Restaurant
	restaurant_dict['slug'] = restaurant.slug
	menulist = Menu.objects.all().filter(Restaurant=restaurant.id).order_by('no')
	menus = Menu.objects.all().filter(Restaurant=restaurant.id).exclude(submenu_menu__isnull=True)
	menus_no_sub = Menu.objects.all().filter(Restaurant=restaurant.id).exclude(submenu_menu__isnull=False)
	restaurant_dict['Menus'] = []
	restaurant_dict['MenuList'] = [a.Menu for a in menulist ]
	for menu in menus_no_sub:
		menu_dict = {}
		menu_dict['Menu'] = menu.Menu
		menu_dict['SubMenus'] = 'null';
		menu_dict['No'] = menu.no
		restaurant_dict['Menus'].append(menu_dict)
		dishes = Dish.objects.all().filter(Menu=menu.id)
		menu_dict['Dishes'] = []
		for dish in dishes:
				dish_dict = {}
				dish_dict['Dish'] = dish.Dish
				dish_dict['Price'] = dish.Price
				dish_dict['image_path'] = dish.image_path
				menu_dict['Dishes'].append(dish_dict)
	for menu in menus:
		menu_dict = {}
		menu_dict['Menu'] = menu.Menu
		menu_dict['No'] = menu.no
		restaurant_dict['Menus'].append(menu_dict)
		submenus = SubMenu.objects.all().filter(Menu=menu.id)
		menu_dict['SubMenus'] = []
		for submenu in submenus:
			submenu_dict = {}
			submenu_dict['SubMenu'] = submenu.Sub_Menu
			submenu_dict['No'] = submenu.no
			menu_dict['SubMenus'].append(submenu_dict)
			dishes = Dish.objects.all().filter(Sub_Menu=submenu.id)
			submenu_dict['Dishes'] = []
			for dish in dishes:
				dish_dict = {}
				dish_dict['Dish'] = dish.Dish
				dish_dict['Price'] = dish.Price
				submenu_dict['Dishes'].append(dish_dict)
	to_json.append(restaurant_dict)
	final_json = {'results':to_json}
	return JSONResponse(final_json)	
	

# class OrderCreateView(CreateView):
    # model = Order
    # fields = ['Count', 'Dish_Price', 'Total_Amount',]
    # success_url = reverse_lazy('restaurant:detail')
    # OrderFormSet = formset_factory(OrderForm, formset=BaseOrderFormSet)
    # def get_context_data(self, **kwargs):
        # data = super(CartCreate, self).get_context_data(**kwargs)
        # if self.request.POST:
            # data['orders'] = OrderFormSet(self.request.POST)
        # else:
            # data['orders'] = OrderFormSet()
        # return data
    
    # def get(self, request, *args, **kwargs):
        # slug = kwargs.get('slug')
        # return super(OrderCreateView, self).get(request, *args, **kwargs)

    # def form_valid(self, form):
        # context = self.get_context_data()
        # orders = context['orders']
        # slug = self.slug
        # restaurant_instance = get_object_or_404(Restaurant, slug=slug)
        # with transaction.atomic():
            # self.object = form.save()

            # if orders.is_valid():
                # orders.instance = self.object
                # #orders.Restaurant = restaurant_instance
                # orders.user = request.user
                # #orders.Menu = get_object_or_404(Menu, id=request.POST['menu_id'])
                # orders.Dish = get_object_or_404(Dish, id=request.POST['dish_id'])
                # orders.save()
        # return super(OrderCreateView, self).form_valid(form)
    
# def Cart(request):
    # OrderFormSet = formset_factory(OrderForm, formset=BaseOrderFormSet)
    #link_data = [{'anchor': l.anchor, 'url': l.url}
                    #for l in user_links]
        
    # if request.method == 'POST':
        # order_formset = OrderFormSet(request.POST)
        
        # if order_formset.is_valid():
		

# def search(request):
	# form = SearchForm(request.POST or None)
	# if form.is_valid():
		# instance = form.save(commit=False)
		# instance.user = request.user
		# instance.save()
		# return HttpResponseRedirect(instance.get_absolute_url())
	# context = {
		# "form": form,
	# }
	# return render(request, "index.html", context)
	
# def restauran(request, id):
	# instance = get_object_or_404(Search, id=id)
	# date_time = instance.TimeStamp
	# t = date_time.timetuple()
	# y, m, d, h, min, sec, wd, yd, i = t
	# if instance.Pnr:
		# pnr_response = urlopen("http://api.railwayapi.com/pnr_status/pnr/instance.Pnr/apikey/3dacdecg/").read().decode('utf8')
		# pnr_obj = json.loads(pnr_response)
		# train_num = pnr_obj['train_num']
		# boarding = pnr_obj['from_station']['code']
		# destination = pnr_obj['reservation_upto']['code']
		# # dj = pnr_obj['doj']
		# # dj_tuple = tuple(dj)
		# # dj_index = [i for i,x in enumerate(dj_tuple) if x=='-']
		# # dj_year = ''.join(dj_tuple[dj_index[1]+1:])
		# # dj_month = ''.join(dj_tuple[dj_index[0]+1:dj_index[1]])
		# # dj_day = ''.join(dj_tuple[:dj_index[0]])
		# # doj = datetime.date(dj_year, dj_month, dj_day)
		# dot = datetime.date(int(pnr_obj['train_start_date']['year']), int(pnr_obj['train_start_date']['month']), int(pnr_obj['train_start_date']['day']))
		# train_response = urlopen("http://api.railwayapi.com/route/train/pnr_obj['train_num']/apikey/3dacdecg/").read().decode('utf8')
		# train_obj = json.loads(train_response)
		# x = train_obj['route']
		# train_route_total = [a['code'] for a in x]
		# boarding_index = [i for i,x in enumerate(train_route_total) if x==boarding]
		# destination_index = [i for i,x in enumerate(train_route_total) if x==destination]
		# train_route_updated = train_route_total[boarding_index[0]:destination_index[0]+1]
		# dos = datetime.date(y, m, d)
		# diff.days = dot - dos
		# req_time = diff.days*24*60 + int(b[0:2])-h)*60+(int(b[3:5])-min)+(int(a['day'])-1)*24*60
		# train_route_final_a = [z for z in train_route_updated for a in x if z == a['code'] and a['scharr'] == "Source" and (int(a['schdep'][0:2])-h)*60+(int(a['schdep'][3:5])-min)+(int(a['day'])-1+diff.days)*24*60>60]
		# train_route_final_b = [z for z in train_route_updated for a in x if z == a['code'] and (int(a['scharr'][0:2])-h)*60+(int(a['scharr'][3:5])-min)+(int(a['day'])-1+diff.days)*24*60>60 ]
		# train_route_final = train_route_final_a + train_route_final_b
		
	# elif instance.TrainDetails:
		# dt = instance.Date
		# dtp = parse(dte)
		# doj = dtp.date()
		# train = train_instance.TrainDetails
		# train_no = train[train.find("(")+1:train.find(")")]
		# train_response = urlopen("http://api.railwayapi.com/route/train/{}/apikey/3dacdecg/".format(train_no)).read().decode('utf8')
		# train_obj = json.loads(train_response)
		# x = train_obj['route']
		# train_route_total = [a['code'] for a in x]
		# boarding_index = [i for i,x in enumerate(train_route_total) if x==instance.Boarding]
		# #destination_index = [i for i,x in enumerate(train_route_total) if x==destination]
		# train_route_updated = train_route_total[boarding_index[0]:]
		
		# dos = datetime.date(y, m, d)
		# diff.days = dot - dos 
		# req_time = diff.days*24*60 + int(b[0:2])-h)*60+(int(b[3:5])-min)+(int(a['day'])-1)*24*60
		# train_route_final_a = [z for z in train_route_updated for a in x if z == a['code'] and a['scharr'] == "Source" and (int(a['schdep'][0:2])-h)*60+(int(a['schdep'][3:5])-min)+(int(a['day'])-1+diff.days)*24*60>60]
		# train_route_final_b = [z for z in train_route_updated for a in x if z == a['code'] and (int(a['scharr'][0:2])-h)*60+(int(a['scharr'][3:5])-min)+(int(a['day'])-1+diff.days)*24*60>60 ]
		# train_route_final = train_route_final_a + train_route_final_b
		
		# object_list = 
		
def dow(date):
	days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
	dayNumber=date.weekday()
	return days[dayNumber]
		

	
	
def pnr_restaurant_json(request, id):

	pnr_instance = get_object_or_404(PnrSearch, id=id)
	date_time = pnr_instance.TimeStamp
	t = date_time.timetuple()
	y, m, d, h, min, sec, wd, yd, i = t
	pnr_argument = pnr_instance.Pnr
	pnr_response = urlopen("http://api.railwayapi.com/pnr_status/pnr/{}/apikey/5e7ydvkg/".format(pnr_argument)).read().decode('utf8')
	pnr_obj = json.loads(pnr_response)
	train_num = pnr_obj['train_num']
	boarding = pnr_obj['from_station']['code']
	destination = pnr_obj['reservation_upto']['code']
	dot = datetime.date(int(pnr_obj['train_start_date']['year']), int(pnr_obj['train_start_date']['month']), int(pnr_obj['train_start_date']['day']))
	train_argument = pnr_obj['train_num']
	train_response = urlopen("http://api.railwayapi.com/route/train/{}/apikey/5e7ydvkg/".format(train_argument)).read().decode('utf8')
	train_obj = json.loads(train_response)
	x = train_obj['route']
	train_route_total = [a['code'] for a in x]
	boarding_index = [i for i,x in enumerate(train_route_total) if x==boarding]
	destination_index = [i for i,x in enumerate(train_route_total) if x==destination]
	train_route_updated = train_route_total[boarding_index[0]:destination_index[0]+1]
	dos = datetime.date(y, m, d)
	diff = dot - dos
	#req_time = diff.days*24*60 + int(b[0:2])-h)*60+(int(b[3:5])-min)+(int(a['day'])-1)*24*60
	train_route_final_a = [z for z in train_route_updated for a in x if z == a['code'] and a['scharr'] == "Source" and (int(a['schdep'][0:2])-h)*60+(int(a['schdep'][3:5])-min)+(int(a['day'])-1+diff.days)*24*60>60]
	train_route_final_b = [z for z in train_route_updated for a in x if z == a['code'] and (int(a['scharr'][0:2])-h)*60+(int(a['scharr'][3:5])-min)+(int(a['day'])-1+diff.days)*24*60>60 ]
	train_route_final = train_route_final_a + train_route_final_b
	restaurants = Restaurant.objects.all().filter(City_Code__in=train_route_final).order_by('City_Code')
	to_json = []
	for restaurant in restaurants:
		restaurant_dict = {}
		restaurant_dict['Restaurant'] = restaurant.Restaurant
		restaurant_dict['Area'] = restaurant.Area
		restaurant_dict['image_path'] = restaurant.image_path
		restaurant_dict['slug'] = restaurant.slug
		to_json.append(restaurant_dict)
	# data = serializers.serialize('json', restaurants)
	# struct = json.loads(data)
	#response_data = json.loads(struct['results'])
	final_json = {'results':to_json}
	return JSONResponse(final_json)
	
	
def train_restaurant_json(request, id):

	train_instance = get_object_or_404(TrainSearch, id=id)
	date_time = train_instance.TimeStamp
	t = date_time.timetuple()
	y, m, d, h, min, sec, wd, yd, i = t
	dos = datetime.date(y, m, d)
	dte = train_instance.Date
	dtp = parse(dte)
	doj = dtp.date()
	train = train_instance.TrainDetails
	train_no = train[train.find("(")+1:train.find(")")]
	train_response = urlopen("http://api.railwayapi.com/route/train/{}/apikey/5e7ydvkg/".format(train_no)).read().decode('utf8')
	train_obj = json.loads(train_response)
	x = train_obj['route']
	train_route_total = [a['code'] for a in x]
	boarding_main=train_instance.Boarding
	boarding = boarding_main[boarding_main.find("/")+2:]
	source_day = [a['day'] for a in x if a['code']==boarding]
	dot = doj - timedelta(days=source_day[0]-1)
	t_weekday = dow(dot)
	working_days = train_obj['train']['days']
	t_runs = [y['runs'] for y in working_days if y['day-code']==t_weekday]
	if t_runs[0] == 'Y':
		boarding_index = [i for i,x in enumerate(train_route_total) if x==boarding]
		#destination_index = [i for i,x in enumerate(train_route_total) if x==destination]
		train_route_updated = train_route_total[boarding_index[0]:]
		diff = doj - dos
		actual_diff = diff.days - source_day[0]
		#req_time = diff.days*24*60 + int(b[0:2])-h)*60+(int(b[3:5])-min)+(int(a['day'])-1)*24*60
		train_route_final_a = [z for z in train_route_updated for a in x if z == a['code'] and a['scharr'] == "Source" and (int(a['schdep'][0:2])-h)*60+(int(a['schdep'][3:5])-min)+(int(a['day'])+actual_diff)*24*60>60]
		train_route_final_b = [z for z in train_route_updated for a in x if z == a['code'] and (int(a['scharr'][0:2])-h)*60+(int(a['scharr'][3:5])-min)+(int(a['day'])+actual_diff)*24*60>60 ]
		print(train_route_final_b)
		train_route_final = train_route_final_a + train_route_final_b
		restaurants = list(Restaurant.objects.all().filter(City_Code__in=train_route_final))
		restaurants.sort(key=lambda t: train_route_final.index(t.City_Code))
		to_json = []
		for restaurant in restaurants:
			restaurant_dict = {}
			restaurant_dict['Restaurant'] = restaurant.Restaurant
			restaurant_dict['Area'] = restaurant.Area
			restaurant_dict['image_path'] = restaurant.image_path
			restaurant_dict['slug'] = restaurant.slug
			to_json.append(restaurant_dict)
	# data = serializers.serialize('json', restaurants)
	# struct = json.loads(data)
	#response_data = json.loads(struct['results'])
		final_json = {'results':to_json}
		return JSONResponse(final_json)
	
def pnr_restaurants(request, id):
	
	pnr_instance = get_object_or_404(PnrSearch, id=id)
		
		
			
	context= {
		'instance' : pnr_instance,
		}
		
	return render(request, "pnr_restaurant_list.html", context)
	
	
def train_restaurants(request, id):
	
	train_instance = get_object_or_404(TrainSearch, id=id)
		
		
	context={
		'instance' : train_instance,
		}
		
	return render(request, "train_restaurant_list.html", context)
	
		
		
