from django.conf import settings
from django.db import models
from django.db.models import Manager


class MetaData(models.Model):
    woo_id = models.IntegerField()
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Base_Line_Items(models.Model):
    woo_id = models.IntegerField()
    name = models.IntegerField()
    product_id = models.IntegerField()
    variation_id = models.IntegerField()
    quantity = models.IntegerField()
    tax_class = models.CharField(max_length=25, blank=True, null=True)
    subtotal = models.CharField(max_length=25, blank=True, null=True)
    subtotal_tax = models.CharField(max_length=25, blank=True, null=True)
    total = models.CharField(max_length=25, blank=True, null=True)
    total_tax = models.CharField(max_length=25, blank=True, null=True)
    # taxes = models.
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    sku = models.CharField(max_length=25, blank=True, null=True)
    price = models.CharField(max_length=25, blank=True, null=True)


class BaseModel(models.Model):
    woo_id = models.IntegerField()
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_modified_gmt = models.DateTimeField()


class BaseModel_1(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    slug = models.CharField(max_length=25, blank=True, null=True)


class Base_billing_Shipping(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=25, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    postcode = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)


class Billing(Base_billing_Shipping):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Shipping(Base_billing_Shipping):
    pass


class Customer(BaseModel):
    email = models.EmailField()
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    is_paying_customer = models.BooleanField()
    avatar_url = models.URLField()
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)


class Shipping_Lines(models.Model):
    woo_id = models.IntegerField()
    method_title = models.CharField(max_length=25, blank=True, null=True)
    method_id = models.CharField(max_length=25, blank=True, null=True)
    total = models.CharField(max_length=25, blank=True, null=True)
    total_tax = models.CharField(max_length=25, blank=True, null=True)
    # taxes = models.
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)


class Fee_Lines(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    tax_class = models.CharField(max_length=25, blank=True, null=True)
    tax_status = models.CharField(max_length=25, blank=True, null=True)
    total = models.CharField(max_length=25, blank=True, null=True)
    total_tax = models.CharField(max_length=25, blank=True, null=True)
    # taxes = models.
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)


class Coupon_Lines(models.Model):
    woo_id = models.IntegerField()
    code = models.CharField(max_length=25, blank=True, null=True)
    discount = models.CharField(max_length=25, blank=True, null=True)
    discount_tax = models.CharField(max_length=25, blank=True, null=True)
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)


class Refunds(models.Model):
    woo_id = models.IntegerField()
    reason = models.CharField(max_length=25, blank=True, null=True)
    total = models.CharField(max_length=25, blank=True, null=True)


class Orders(BaseModel):
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    number = models.CharField(max_length=25, blank=True, null=True)
    order_key = models.CharField(max_length=25, blank=True, null=True)
    created_via = models.CharField(max_length=25, blank=True, null=True)
    version = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=25, choices=settings.ORDER_STATUS, default='pending')
    # currency = models.
    discount_total = models.CharField(max_length=25, blank=True, null=True)
    discount_tax = models.CharField(max_length=25, blank=True, null=True)
    shipping_total = models.CharField(max_length=25, blank=True, null=True)
    shipping_tax = models.CharField(max_length=25, blank=True, null=True)
    cart_tax = models.CharField(max_length=25, blank=True, null=True)
    total = models.CharField(max_length=25, blank=True, null=True)
    total_tax = models.CharField(max_length=25, blank=True, null=True)
    prices_include_tax = models.BooleanField()
    customer_id = models.IntegerField(default='0')
    customer_ip_address = models.GenericIPAddressField()
    customer_user_agent = models.CharField(max_length=25, blank=True, null=True)
    customer_note = models.CharField(max_length=25, blank=True, null=True)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=25, blank=True, null=True)
    payment_method_title = models.CharField(max_length=25, blank=True, null=True)
    transaction_id = models.CharField(max_length=25, blank=True, null=True)
    date_paid = models.DateTimeField()
    date_paid_gmt = models.DateTimeField()
    date_completed = models.DateTimeField()
    date_completed_gmt = models.DateTimeField()
    cart_hash = models.CharField(max_length=25, blank=True, null=True)
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    line_items = models.ForeignKey(Base_Line_Items, on_delete=models.CASCADE)
    # tax_lines = models.
    shipping_lines = models.ForeignKey(Shipping_Lines, on_delete=models.CASCADE)
    fee_lines = models.ForeignKey(Fee_Lines, on_delete=models.CASCADE)
    coupon_lines = models.ForeignKey(Coupon_Lines, on_delete=models.CASCADE)
    refunds = models.ForeignKey(Refunds, on_delete=models.CASCADE)
    set_paid = models.BooleanField(default=False)


class Order_Note(models.Model):
    woo_id = models.IntegerField()
    author = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    note = models.CharField(max_length=50, blank=True, null=True)
    customer_note = models.BooleanField(default=False)
    added_by_user = models.BooleanField(default=False)


class Line_Items_1(Base_Line_Items):
    refund_total = models.IntegerField()


class Order_Refund(models.Model):
    woo_id = models.IntegerField()
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    amount = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)
    refunded_by = models.IntegerField()
    refunded_payment = models.BooleanField()
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    line_items = models.ForeignKey(Line_Items_1, on_delete=models.CASCADE)
    api_refund = models.BooleanField(default=True)


class Downloads(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    file = models.FileField()


class Dimensions(models.Model):
    length = models.CharField(max_length=25, blank=True, null=True)
    width = models.CharField(max_length=25, blank=True, null=True)
    height = models.CharField(max_length=25, blank=True, null=True)


class Categories(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    slug = models.CharField(max_length=25, blank=True, null=True)


class Tags(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    slug = models.CharField(max_length=25, blank=True, null=True)


# use image field
class Image(BaseModel):
    src = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    alt = models.CharField(max_length=50, blank=True, null=True)


class Attributes(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    position = models.IntegerField()
    visible = models.BooleanField(default=False)
    variation = models.BooleanField(default=False)
    # options = models.


class Default_Attributes(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=25, blank=True, null=True)
    option = models.CharField(max_length=25, blank=True, null=True)


class Product(BaseModel):
    name = models.CharField(max_length=25, blank=True, null=True)
    slug = models.CharField(max_length=25, blank=True, null=True)
    permalink = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=25, choices=settings.TYPE_KIND, default='simple')
    status = models.CharField(max_length=25, choices=settings.STATUS_PRODUCT, default='publish')
    featured = models.BooleanField(default=False)
    catalog_visibility = models.CharField(max_length=25, choices=settings.CATALOG_VISIBILITY_PRODUCT, default='visible')
    description = models.TextField(max_length=300, blank=True, null=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=25, blank=True, null=True)
    price = models.CharField(max_length=25, blank=True, null=True)
    regular_price = models.CharField(max_length=25, blank=True, null=True)
    sale_price = models.CharField(max_length=25, blank=True, null=True)
    date_on_sale_from = models.DateTimeField()
    date_on_sale_from_gmt = models.DateTimeField()
    date_on_sale_to = models.DateTimeField()
    date_on_sale_to_gmt = models.DateTimeField()
    price_html = models.CharField(max_length=50, blank=True, null=True)
    on_sale = models.BooleanField()
    purchasable = models.BooleanField()
    total_sales = models.IntegerField()
    virtual = models.BooleanField(default=False)
    downloadable = models.BooleanField(default=False)
    downloads = models.ForeignKey(Downloads, on_delete=models.CASCADE)
    download_limit = models.IntegerField(default=-1)
    download_expiry = models.IntegerField(default=-1)
    external_url = models.URLField()
    button_text = models.CharField(max_length=25, blank=True, null=True)
    tax_status = models.CharField(max_length=25, choices=settings.TAX_STATUS_PRODUCT, default='taxable')
    tax_class = models.CharField(max_length=25, blank=True, null=True)
    manage_stock = models.BooleanField(default=False)
    stock_quantity = models.IntegerField()
    stock_status = models.CharField(max_length=25, choices=settings.STOCK_STATUS_PRODUCT, default='instock')
    backorders = models.CharField(max_length=25, choices=settings.BACKORDERS_PRODUCT, default='no')
    backorders_allowed = models.BooleanField()
    backordered = models.BooleanField()
    sold_individually = models.BooleanField(default=False)
    weight = models.CharField(max_length=25, blank=True, null=True)
    dimensions = models.ForeignKey(Dimensions, on_delete=models.CASCADE)
    shipping_required = models.BooleanField()
    shipping_taxable = models.BooleanField()
    shipping_class = models.CharField(max_length=25, blank=True, null=True)
    shipping_class_id = models.IntegerField()
    reviews_allowed = models.BooleanField(default=True)
    average_rating = models.CharField(max_length=25, blank=True, null=True)
    rating_count: int = models.IntegerField()
    # related_ids = models.
    # upsell_ids = models.
    # cross_sell_ids = models.
    parent_id = models.IntegerField()
    purchase_note = models.CharField(max_length=25, blank=True, null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    default_attributes = models.ForeignKey(Default_Attributes, on_delete=models.CASCADE)
    # variations = models.
    # grouped_products = models.
    menu_order = models.IntegerField()
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    product_variation = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    line_itemss = models.ManyToManyField(Orders, through='Line_Items')


class Product_Category(BaseModel_1):
    parent = models.IntegerField()
    description = models.CharField(max_length=25, blank=True, null=True)
    display = models.CharField(max_length=25, choices=settings.DISPLAY_PRODUCT_CATEGORY, default='default')
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    menu_order = models.IntegerField()
    count = models.IntegerField()


class Coupons(BaseModel):
    code = models.CharField(max_length=25, blank=True, null=True)
    amount = models.CharField(max_length=25, blank=True, null=True)
    discount_type = models.CharField(max_length=25, choices=settings.DISCOUNT_TYPE_COUPONS, default='fixed_cart')
    description = models.TextField(max_length=150, blank=True, null=True)
    date_expires = models.CharField(max_length=25, blank=True, null=True)
    date_expires_gmt = models.CharField(max_length=25, blank=True, null=True)
    usage_count = models.IntegerField(blank=True, null=True)
    individual_use = models.BooleanField(default=False)
    product_ids = models.ManyToManyField(Product, related_name='coupons_product_ids')
    excluded_product_ids = models.ManyToManyField(Product, related_name='coupons_excluded_product_ids')
    usage_limit = models.IntegerField()
    usage_limit_per_user = models.IntegerField()
    limit_usage_to_x_items = models.IntegerField()
    free_shipping = models.BooleanField(default=False)
    product_categories: Manager = models.ManyToManyField(Product_Category, related_name='coupons_product_categories')
    excluded_product_categories: Manager = models.ManyToManyField(Product_Category,
                                                                  related_name='coupons_excluded_product_categories')
    exclude_sale_items = models.BooleanField(default=False)
    minimum_amount = models.CharField(max_length=50, blank=True, null=True)
    maximum_amount = models.CharField(max_length=50, blank=True, null=True)
    # email_restrictions = models.
    # used_by = models.
    meta_data = models.ForeignKey(MetaData, on_delete=models.CASCADE)


class Line_Items(Base_Line_Items):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='line_items_order')
    product_field = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='line_items_product')


# class Product_Variation(Product):
    # woo_id = models.IntegerField()
    # date_created = models.DateTimeField()
    # date_created_gmt = models.DateTimeField()
    # date_modified = models.DateTimeField()
    # date_modified_gmt = models.DateTimeField()
    # status = models.CharField(max_length=25, choices=settings.STATUS_PRODUCT_VARIATION, default='publish')


class Product_Attribute(BaseModel_1):
    type = models.CharField(max_length=25, blank=True, null=True)
    order_by = models.CharField(max_length=25, choices=settings.ORDER_BY_PRODUCT_ATTRIBUTE, default='menu_order')
    has_archives = models.BooleanField()


class Product_Attribute_term(BaseModel_1):
    description = models.CharField(max_length=25, blank=True, null=True)
    menu_order = models.IntegerField()
    count = models.IntegerField()


class Product_Shipping_class(models.Model):
    description = models.CharField(max_length=25, blank=True, null=True)
    count = models.IntegerField()
    product_tag = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)


class Product_Review(models.Model):
    woo_id = models.IntegerField()
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    product_id = models.IntegerField()
    status = models.CharField(max_length=25, choices=settings.STATUS_PRODUCT_REVIEW, default='approved')
    reviewer = models.CharField(max_length=25, blank=True, null=True)
    reviewer_email = models.EmailField()
    review = models.CharField(max_length=25, blank=True, null=True)
    rating = models.IntegerField()
    verified = models.BooleanField()
