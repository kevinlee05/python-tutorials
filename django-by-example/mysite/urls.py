from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^images/', include('images.urls', namespace='images')),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog') ),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps },
        name='django.contrib.sitemaps.views.sitemap'),
    url(_(r'^cart/'), include('cart.urls', namespace='cart')),
    url(_(r'^orders/'), include('orders.urls', namespace='orders')),
    url(_(r'^payment/'), include('payment.urls', namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(_(r'^coupons/'), include('coupons.urls', namespace='coupons')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^', include('shop.urls', namespace='shop')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)