from .pagemodels.products.base import Product
from .pagemodels.products.general import GeneralProduct
from .pagemodels.products.software import SoftwareProduct
from .pagemodels.product_update import Update
from .pagemodels.product_category import BuyersGuideProductCategory
from .pagemodels.privacy import ProductPrivacyPolicyLink

from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(Product)
class ProductTR(TranslationOptions):
    fields = (
        'name',
        'company',
        'blurb',
        'uses_encryption_helptext',
        'security_updates_helptext',
        'strong_password_helptext',
        'manage_vulnerabilities_helptext',
        'privacy_policy_helptext',
        'share_data_helptext',
        'how_does_it_share',
        'user_friendly_privacy_policy_helptext',
        'worst_case',
    )


@register(GeneralProduct)
class GeneralProductTR(TranslationOptions):
    fields = (
        'delete_data_helptext',
        'child_rules_helptext',
        'collects_biometrics_helptext',
    )


@register(SoftwareProduct)
class SoftwareProductTR(TranslationOptions):
    fields = (
        'handles_recordings_how',
        'recording_alert_helptext',
        'signup_methods_helptext',
        'medical_privacy_compliant_helptext',
        'host_controls',
        'easy_to_learn_and_use_helptext',
    )


@register(BuyersGuideProductCategory)
class BuyersGuideProductCategoryTR(TranslationOptions):
    fields = (
        'name',
        'description',
    )


@register(ProductPrivacyPolicyLink)
class ProductPrivacyPolicyLinkTR(TranslationOptions):
    fields = (
        'label',
    )


@register(Update)
class UpdateTR(TranslationOptions):
    fields = (
        'title',
        'snippet',
    )
