# ckanext-wascal

![Tests](https://github.com/dianda-caleb/ckanext-wascal/actions/workflows/test.yml/badge.svg)


**Tailor-made CKAN extension for a WASCAL data portal** (West African Science Service Centre on Climate Change and Adapted Land Use) — a regional research network covering several West African countries.

## 🎯 Context

WASCAL federates research data on climate and land use across multiple countries (Burkina Faso, Benin, Ghana, Senegal, Mali, Niger, etc.). The generic CKAN data portal did not natively allow to:
- Classify datasets by **country** and **scientific topic** (hydrology, climate, remote sensing, soil, vegetation...),
- Present a visual identity unique to the WASCAL network,
- Adapt data submission forms to the specific needs of the network's researchers.

## 🛠️ What the extension does

- **Dataset schema customization** (`plugin.py`) — addition of selection fields for the dataset's country of origin and thematic category, using controlled value lists.
- **Dedicated visual theme** (`templates/`, `assets/`) — customized homepages, headers, and dataset views, featuring country-specific imagery (flags) and thematic icons (e.g., hydrology, agriculture, climate).
- **Enhanced faceted filtering** (`templates/snippets/facet_list.html`) — search by country and theme within the catalog.
- **Integration with `ckanext-scheming`** for declarative metadata schema definition.


```
ckanext/wascal/
├── plugin.py                  # CKAN Plugin: dataset schema, template helpers
├── templates/
│   ├── home/index.html         # Customized homepage
│   ├── package/                # Dataset views and search pages
│   └── scheming/                # Integration with ckanext-scheming
├── public/
│   ├── flags/                   # Flags of the WASCAL network countries
│   └── data_topics/             # Icons per scientific topic
└── tests/
    └── test_plugin.py
```


## ⚙️ Installation

```bash
pip install -e git+https://github.com/dianda-caleb/ckanext-wascal.git#egg=ckanext-wascal
```

In `ckan.ini`:
```ini
ckan.plugins = ... scheming_datasets wascal
```

## 🧪 Tests

```bash
pytest --ckan-ini=test.ini
```

## 📄 License

See [LICENSE](LICENSE) (AGPL-3.0).


---------------------------------------------------


# Version Française


# ckanext-wascal

**Extension CKAN sur mesure pour un portail de données WASCAL** (West African Science Service Centre on Climate Change and Adapted Land Use) — un réseau de recherche régional couvrant plusieurs pays d'Afrique de l'Ouest.

## 🎯 Contexte

WASCAL fédère des données de recherche sur le climat et l'usage des terres à travers plusieurs pays (Burkina Faso, Bénin, Ghana, Sénégal, Mali, Niger, etc.). Le portail de données générique CKAN ne permettait pas nativement de :
- classer les jeux de données par **pays** et par **thématique scientifique** (hydrologie, climat, télédétection, sol, végétation...),
- présenter une identité visuelle propre au réseau WASCAL,
- adapter les formulaires de dépôt de données aux besoins spécifiques des chercheurs du réseau.

## 🛠️ Ce que fait l'extension

- **Personnalisation du schéma de dataset** (`plugin.py`) — ajout de champs de sélection pour le pays d'origine et la thématique du jeu de données, avec listes de valeurs contrôlées
- **Thème visuel dédié** (`templates/`, `assets/`) — pages d'accueil, en-tête et fiches datasets personnalisés, illustrés par pays (drapeaux) et par thématique (icônes hydrologie, agriculture, climat...)
- **Filtrage à facettes enrichi** (`templates/snippets/facet_list.html`) — recherche par pays et par thématique dans le catalogue
- **Intégration avec `ckanext-scheming`** pour la définition déclarative du schéma de métadonnées

```
ckanext/wascal/
├── plugin.py                  # Plugin CKAN : schéma de dataset, helpers de template
├── templates/
│   ├── home/index.html         # Page d'accueil personnalisée
│   ├── package/                # Fiches et recherche de jeux de données
│   └── scheming/                # Intégration avec ckanext-scheming
├── public/
│   ├── flags/                   # Drapeaux des pays du réseau WASCAL
│   └── data_topics/             # Icônes par thématique scientifique
└── tests/
    └── test_plugin.py
```

## ⚙️ Installation

```bash
pip install -e git+https://github.com/dianda-caleb/ckanext-wascal.git#egg=ckanext-wascal
```

Dans `ckan.ini` :
```ini
ckan.plugins = ... scheming_datasets wascal
```

## 🧪 Tests

```bash
pytest --ckan-ini=test.ini
```

## 📄 Licence

Voir [LICENSE](LICENSE) (AGPL-3.0).
