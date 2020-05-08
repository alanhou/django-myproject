from django.conf import settings


def get_multilingual_field_names(field_name):
  lang_code_underscored = settings.LANGUAGE_CODE.replace("-", "_")
  field_names = [f"{field_name}_{lang_code_underscored}"]
  for lang_code, lang_name in settings.LANGUAGES:
    if lang_code != settings.LANGUAGE_CODE:
      lang_code_underscored = lang_code.replace("-", "_")
      field_names.append(
        f"{field_name}_{lang_code_underscored}"
      )
  return field_names