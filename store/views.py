from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (Category, Banner, SubCategory, Product, Shop, Campaign, Offer, Brand,
                    WishList, )
# Pagination module
from django.core.paginator import Paginator
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def homeView(request):
    campaigns, offers, shops = None, None, None
    categories = Category.objects.filter(parent=None).order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    shop_obj = Shop.objects.all()
    campaign_obj = Campaign.objects.all()
    offer_obj = Offer.objects.all()
    brands = Brand.objects.all().order_by("-id")

    if len(shop_obj) > 0:
        shops = Shop.objects.all().order_by("-id")[:6]
    if len(campaign_obj) > 0:
        campaigns = Campaign.objects.all().order_by("-id")[0]
    if len(offer_obj) > 0:
        offers = Offer.objects.all().order_by("-id")[0]

    banners, local_grocery_images, products, show_categories = None, None, None, None
    subcategories = SubCategory.objects.all()
    product_obj = Product.objects.all()
    show_category_obj = Category.objects.all()
    all_products = Product.objects.all().order_by("-id")

    if len(Banner.objects.all()) > 0:
        banners = Banner.objects.all().order_by("-id")[:6]
    if len(product_obj) > 0:
        products = Product.objects.all().order_by("-id")[:8]
    if len(show_category_obj) > 0:
        show_categories = Category.objects.all()[:6]

    context = {
        "categories": categories,
        "main_navbarCat": main_navbarCat,
        "shops": shops,
        "banners": banners,
        "subcategories": subcategories,
        "products": products,
        "show_categories": show_categories,
        "campaigns": campaigns,
        "offers": offers,
        "all_products": all_products,
        "brands": brands
    }
    return render(request, 'store/home.html', context)

## Login Registration View

def user_registration(request):
    categories = Category.objects.all().order_by("-id")
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:user_login')
    context = {'form': form, "categories": categories}
    return render(request, 'store/registration.html', context)


def user_login(request):
    categories = Category.objects.all().order_by("-id")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("store:home")

    context = {"categories": categories}
    return render(request, 'store/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('store:home')


def productDetailView(request, slug):
    categories = Category.objects.all().order_by("-id")
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return HttpResponse("Product Not Found!")

    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()

    context = {
        "product": product,
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories
    }
    return render(request, "store/product_details.html", context)

def category_wise_product(request, id):
    cat_obj = Category.objects.filter(parent=None).order_by("-id")

    prd_obj = Product.objects.filter(category_id = id)

    context = {'cat_obj': cat_obj, 'prd_obj': prd_obj}

    return render(request, 'store/category_wise.html', context)





def allBrandsView(request):
    categories = Category.objects.all().order_by("-id")
    brands = Brand.objects.all()
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()

    context = {
        "brands": brands,
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories
    }
    return render(request, "store/all_brands.html", context)


def userDashboardView(request):
    categories = Category.objects.all().order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()

    context = {
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories,
        # "order_items": order_items
    }
    return render(request, "store/user_dashboard.html", context)


def manageProfileView(request):
    categories = Category.objects.all().order_by("-id")
    if request.user.is_authenticated:
        main_navbarCat = Category.objects.all().order_by("-id")[:6]
        subcategories = SubCategory.objects.all()

        context = {
            "main_navbarCat": main_navbarCat,
            "categories": categories,
            "subcategories": subcategories,
        }
        return render(request, "store/manage_profile.html", context)
    else:
        return redirect("store:home")


def wishlistView(request):
    categories = Category.objects.all().order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()
    if request.user.is_authenticated:
        all_products = WishList.objects.filter(user=request.user, isFavorite=True)
    else:
        return redirect("store:home")

    context = {
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories,
        "all_products": all_products
    }
    return render(request, "store/wishlist.html", context)





def brand_wise_product(request, id):
    categories = Category.objects.all().order_by("-id")
    brand_obj = Brand.objects.all()
    prd_obj = Product.objects.filter(brand_id=id)

    context = {'brand_obj': brand_obj, 'prd_obj': prd_obj, "categories": categories}

    return render(request, 'store/brand_wise.html', context)


def campaignView(request):
    categories = Category.objects.all().order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()
    campaigns = Campaign.objects.all()
    products = Product.objects.all().order_by("-id")

    context = {
        "campaigns": campaigns,
        "products": products,
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories,
    }
    return render(request, "store/campaigns.html", context)


def flashSaleView(request):
    categories = Category.objects.all().order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()
    offers = Offer.objects.all()
    products = Product.objects.all().order_by("-id")

    context = {
        "offers": offers,
        "products": products,
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories,
    }
    return render(request, "store/flash_sale.html", context)


def shopwiseProductView(request, id, title):
    products = []
    categories = Category.objects.all().order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()

    try:
        shop = Shop.objects.get(id=id, title=title)
    except Shop.DoesNotExist:
        return HttpResponse("Shop not found!")
    else:
        products_obj = Product.objects.all().order_by("-id")
        # Appending all the products of the shop
        for item in products_obj:
            if str(item.shop) == shop.title:
                products.append(item)

        # Pagination
        paginator = Paginator(products, 20)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


    context = {
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories,
        "shop": shop,
        "products": products,
        "page_obj": page_obj
    }
    return render(request, "store/shopwise_product.html", context)


def localShopView(request):
    products = []
    categories = Category.objects.all().order_by("-id")
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    subcategories = SubCategory.objects.all()

    try:
        shop = Shop.objects.get(title="Mustaqeem Localshop")
    except Shop.DoesNotExist:
        return HttpResponse("Shop not found!")
    else:
        products_obj = Product.objects.all().order_by("-id")
        # Appending all the products of the shop
        for item in products_obj:
            if str(item.shop) == shop.title:
                products.append(item)

        # Pagination
        paginator = Paginator(products, 20)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


    context = {
        "main_navbarCat": main_navbarCat,
        "categories": categories,
        "subcategories": subcategories,
        "shop": shop,
        "products": products,
        "page_obj": page_obj
    }
    return render(request, "store/shopwise_product.html", context)


def searchView(request):
    main_navbarCat = Category.objects.all().order_by("-id")[:6]
    categories = Category.objects.all().order_by("-id")
    subcategories = SubCategory.objects.all()

    if  request.method == "GET":
        query = request.GET.get("query")

        if query is None:
            return redirect("store:home")

        products = Product.objects.filter(title__icontains=query).order_by("-id")

        # Pagination
        paginator = Paginator(products, 20)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'products': products,
            "page_obj": page_obj,
            "main_navbarCat": main_navbarCat,
            "categories": categories,
            "subcategories": subcategories,
        }
        return render(request, 'store/search.html', context)





