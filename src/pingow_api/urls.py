from django.conf.urls import url
from django.contrib import admin

from .views import (
	position_update,
	send_review,
	get_recommendation_for_shop,
	get_recommendation_for_product,
	init_trip_with_shop,
	init_trip_with_shop_and_product,
	get_shop_asst,
	api_post,
	customer_profile_create,
	db_view_customer,
	db_view_customer_trans,
	test,
	)

from pingow_api.db_access import views as dbv

urlpatterns = [
	url(r'^position/$', position_update),
	url(r'^send_review/$', send_review),
	url(r'^get_recommendation_for_shop/$', get_recommendation_for_shop),
	url(r'^get_recommendation_for_product/$', get_recommendation_for_product),
	url(r'^init_trip_with_shop/$', init_trip_with_shop),
	url(r'^init_trip_with_shop_and_product/$', init_trip_with_shop_and_product),
	url(r'^get_shop_asst/$', get_shop_asst),
	url(r'^api_post/$', api_post),
	#webaccess for database table
	url(r'^db_access/table/customer/$', db_view_customer),
	url(r'^db_access/table/customer_trans/$', db_view_customer_trans),
	url(r'^db_access/customer/create/$', customer_profile_create),

	#json access
	url(r'^db_access/json/db_customer/$',dbv.db_customer_json),
	url(r'^db_access/json/db_shop/$',dbv.db_shop_json),
	url(r'^db_access/json/db_beacon/$',dbv.db_beacon_json),
	url(r'^db_access/json/db_beacon_relationship/$',dbv.db_beacon_relationship_json),
	url(r'^db_access/json/db_assistance/$',dbv.db_assistance_json),
	url(r'^db_access/json/db_crowd/$',dbv.db_crowd_json),
	url(r'^db_access/json/db_assistance_avail/$',dbv.db_assistance_avail_json),
	url(r'^db_access/json/db_shop_subcat_reference/$',dbv.db_shop_subcat_reference_json),
	url(r'^db_access/json/db_sub_category/$',dbv.db_sub_category_json),
	url(r'^db_access/json/db_customer_transaction/$',dbv.db_customer_transaction_json),

    # url(r'^posts/$', "<appname>.views.<function_name>"),
	url(r'^test/$', test),

]
