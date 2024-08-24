from django.urls import path
from BeautyApp import views
urlpatterns=[
            path("index_page/", views.index_page, name="index_page"),
            path("category_page/", views.category_page, name="category_page"),
            path("save_category/", views.save_category, name="save_category"),
            path("category_display/", views.category_display, name="category_display"),
            path("category_edit/<int:catid>/", views.category_edit, name="category_edit"),
            path("update_category/<int:catid>/", views.update_category, name="update_category"),
            path("category_delete/<int:catid>/", views.category_delete, name="category_delete"),
            path("service_page/", views.service_page, name="service_page"),
            path("save_service/", views.save_service, name="save_service"),
            path("service_display/", views.service_display, name="service_display"),
            path("service_edit/<int:sid>/", views.service_edit, name="service_edit"),
            path("update_service/<int:sid>/", views.update_service, name="update_service"),
            path("delete_service/<int:sid>/", views.delete_service, name="delete_service"),

# *******************************************************************************************
#HAIR CARE CATEGORY
            path("hairservice_page/", views.hairservice_page, name="hairservice_page"),
            path("save_hair_data/", views.save_hair_data, name="save_hair_data"),
            path("hair_care_display/", views.hair_care_display, name="hair_care_display"),
            path("hair_care_edit/<int:hcid>/", views.hair_care_edit, name="hair_care_edit"),
            path("update_Hair_service/<int:hcid>/", views.update_Hair_service, name="update_Hair_service"),
            path("hair_care_delete/<int:hcid>/", views.hair_care_delete, name="hair_care_delete"),

#SKIN CARE CATEGORY
            path("skinservice_page/", views.skinservice_page, name="skinservice_page"),
            path("save_skin_data/", views.save_skin_data, name="save_skin_data"),
            path("skin_care_display/", views.skin_care_display, name="skin_care_display"),
            path("skin_care_edit/<int:scid>/", views.skin_care_edit, name="skin_care_edit"),
            path("update_Skin_service/<int:scid>/", views.update_Skin_service, name="update_Skin_service"),
            path("skin_care_delete/<int:scid>/", views.skin_care_delete, name="skin_care_delete"),

#NAIL CARE CATEGORY
            path("nailservice_page/", views.nailservice_page, name="nailservice_page"),
            path("save_nail_data/", views.save_nail_data, name="save_nail_data"),
            path("nail_care_display/", views.nail_care_display, name="nail_care_display"),
            path("nail_care_edit/<int:ncid>/", views.nail_care_edit, name="nail_care_edit"),
            path("update_Nail_service/<int:ncid>/", views.update_Nail_service, name="update_Nail_service"),
            path("nail_care_delete/<int:ncid>/", views.nail_care_delete, name="nail_care_delete"),

#MAKEUP CATEGORY
            path("makeupservice_page/", views.makeupservice_page, name="makeupservice_page"),
            path("save_makeup_data/", views.save_makeup_data, name="save_makeup_data"),
            path("makeup_display/", views.makeup_display, name="makeup_display"),
            path("makeup_edit/<int:mkid>/", views.makeup_edit, name="makeup_edit"),
            path("update_makeup_service/<int:mkid>/", views.update_makeup_service, name="update_makeup_service"),
            path("makeup_delete/<int:mkid>/", views.makeup_delete, name="makeup_delete"),

#BODYCARE CATEGORY
            path("Body_care_service_page/", views.Body_care_service_page, name="Body_care_service_page"),
            path("save_Body_care_data/", views.save_Body_care_data, name="save_Body_care_data"),
            path("bodycare_display/", views.bodycare_display, name="bodycare_display"),
            path("bodycare_edit/<int:bcid>/", views.bodycare_edit, name="bodycare_edit"),
            path("update_bodycare_service/<int:bcid>/", views.update_bodycare_service, name="update_bodycare_service"),
            path("bodycare_delete/<int:bcid>/", views.bodycare_delete, name="bodycare_delete"),

#CONTACT DETAILS
            path("contact_display/", views.contact_display, name="contact_display"),
            path("contact_delete/<int:contid>/", views.contact_delete, name="contact_delete"),

]