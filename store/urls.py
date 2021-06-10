from django.urls import path

from .views import (homeView, productDetailView, allBrandsView, userDashboardView,
                    manageProfileView, wishlistView, campaignView, flashSaleView,
                    shopwiseProductView, localShopView, searchView, category_wise_product, brand_wise_product, user_registration, user_login, logoutView)


app_name = "store"
urlpatterns = [
    path("", homeView, name="home"),
    path("product/<str:slug>/", productDetailView, name="product-detail"),
    path("brands/", allBrandsView, name="brands"),
    path("dashboard/", userDashboardView, name="dashboard"),
    path("profile/", manageProfileView, name="profile"),
    path("wishlist/", wishlistView, name="wishlist"),
    path("campaigns/", campaignView, name="campaigns"),
    path("flash-sale/", flashSaleView, name="flash-sale"),
    path("shops/<int:id>/<str:title>/", shopwiseProductView, name="shopwise-product"),
    path("localshop/Mustaqeem-Localshop", localShopView, name="localshop"),
    path("search/", searchView, name="search"),
    path("category_wise_product/<int:id>/", category_wise_product, name="category_wise_product"),
    path("brand_wise_product/<int:id>/", brand_wise_product, name="brand_wise_product"),

    ## Login Registration ##

    path("user_registration/", user_registration, name="user_registration"),
    path("user_login/", user_login, name="user_login"),
    path('logout/', logoutView, name='logout'),
]
