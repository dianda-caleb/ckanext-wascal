import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.types import Context, Schema, ValidatorFactory
from typing import Any, cast
import logging
log = logging.getLogger(__name__)

def get_user_list():
    context = {'model': toolkit.model, 'user': toolkit.c.user}
    data_dict = {}
    return toolkit.get_action('user_list')(context, data_dict)


class WascalPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers)
    
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "wascal")
    
    def get_helpers(self):
        country_list = ('AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA', 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA AND HERZEGOVINA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL', 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI', 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD', 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS', 'CONGO', 'CONGO, THE DEMOCRATIC REPUBLIC OF', 'COOK ISLANDS', 'COSTA RICA', "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'DENMARK', 'DJIBOUTI', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS', 'FAROE ISLANDS', 'FIJI', 'FINLAND', 'FRANCE', 'FRENCH GUIANA', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES', 'GABON', 'GAMBIA', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS', 'HONDURAS', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN, ISLAMIC REPUBLIC OF', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF", 'KOREA, REPUBLIC OF', 'KUWAIT', 'KYRGYZSTAN', "LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYAN ARAB JAMAHIRIYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO', 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA, REPUBLIC OF', 'MONACO', 'MONGOLIA', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES', 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND', 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PALESTINIAN TERRITORY, OCCUPIED', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR', 'RÃ‰UNION', 'ROMANIA', 'RUSSIAN FEDERATION', 'RWANDA', 'SAINT HELENA', 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS', 'SPAIN', 'SRI LANKA', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN', 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIAN ARAB REPUBLIC', 'TAIWAN, PROVINCE OF CHINA', 'TAJIKISTAN', 'TANZANIA, UNITED REPUBLIC OF', 'THAILAND', 'TIMOR', 'TOGO', 'TOKELAU', 'TONGA', 'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS', 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VIET NAM', 'VIRGIN ISLANDS, BRITISH', 'VIRGIN ISLANDS, U.S.', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZIMBABWE') 
        topics_options = ('Climate', 'Remote Sensing', 'Socio-economic Data', 'Soil', 'Topography', 'Vegetation', 'Weather Conditions', 'Base Data', 'Administrative Boundaries', 'Farming', 'Hydrology', 'Land Use')

        
        return {
            'country_options': country_list, 
            'topics_options': topics_options,
            'get_action': toolkit.get_action,
        }

    def create(self, data_dict):
        log.debug("Form data on create: %s", data_dict)
        return super(WascalPlugin, self).create(data_dict)


    def create_package_schema(self) -> Schema:
        schema = super(WascalPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema


    def update_package_schema(self) -> Schema:
        schema = super(WascalPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
    
    def _modify_package_schema(self, schema: Schema):
        schema.update({
            'custom_text': [toolkit.get_validator('ignore_missing'),
                            toolkit.get_converter('convert_to_extras')]
        })
        schema.update({
            'country_code': [
                toolkit.get_validator('ignore_missing'),
                cast(ValidatorFactory,
                     toolkit.get_converter('convert_to_tags'))('country_codes'),
            ]
        })
        return schema


    def show_package_schema(self):
        schema = super(WascalPlugin, self).show_package_schema()
        schema.update({
            'topic': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'country': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
            'data provider': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'data publisher': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'data funder': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'data owner': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'data author': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'data scientist': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'data disseminator': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'emma': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')]
        })
        return schema


    def is_fallback(self):
        return True


    def package_types(self):
        return []
