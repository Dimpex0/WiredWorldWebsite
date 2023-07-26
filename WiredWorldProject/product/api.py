from rest_framework import generics as rest_views
from rest_framework import serializers

from WiredWorldProject.product.models import Product, Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = SubCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductListApiView(rest_views.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
