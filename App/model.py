"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog={
        'videos': None,
        'id_': None,
        'countries': None,
        'categories': None,
        'cat-id': None}

    catalog['videos'] = lt.newList('SINGLE_LINKED', compareViews)

    catalog['countries'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction= compareMapCountries)

    catalog['id_'] = mp.newMap(maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapVideosIds)
    
    catalog['cat-id'] = mp.newMap(40,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapVideosIds)
    
    catalog['categories'] = mp.newMap(40,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction= compareMapVideosIds)
    return catalog
# Funciones para agregar informacion al catalogo

def addVideo (catalog, video):
    pais = video ['country']
    existe = mp.contains(catalog['id'], video['video_id'])

    if existe:
        entry = mp.get(catalog['id'], video['video_id'])
        v_id = me.getValue(entry)
    else:
        mp.put(catalog['id'], video['video_id'], video)
        v_id = mp.get(catalog['id'], video['video_id'])
    lt.addLast(catalog['videos'], video)
    addVideoPais(catalog, pais, video)
    vid_cat = video['category_id']
    existe = mp.contains(catalog['id_'], vid_cat)

    if existe:
        entry = mp.get(catalog['id_'], vid_cat)
        lst = me.getKey(entry)
    else:
        lst = lt.newList('SINGLE_LINKED', compareLikes)
        mp.put(catalog['id_'], vid_cat, lst)
    
    lt.addLast(lst, video)

def addVideoPais(catalog, pais, video):
    countries = catalog['countries']
    existe = mp.contains(countries, pais)

    if existe:
        entry = mp.get(countries, pais)
        country = me.getValue(entry)
    else:
        country = newCountry(pais)
        mp.put(countries, pais, country)
    lt.addLast(country['videos'], video)

def newCountry(pais):
    country = {'name': "", "videos": None}
    country['name'] =pais
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def addCat(catalog, category):
    cat = newCat(category['name'], category['id'])
    mp.put(catalog['categories'], cat['name'], cat ['id'])

def newCat(name, id):
    cat = {'name': '', 'id': ''}
    cat ['name'] = name
    cat ['id'] = id
    return cat

def getVideosByCountry(catalog, country):
    existe = mp.contains(catalog['countries'], country)
    if exist:
        entry = lt.get(catalog['countries'], country)
        country1 = me.getValue(entry)
    else: 
        country1 = "No existe dicho Pais"
    return country1

def getCat(catalog, category):
    exist = mp.contains(catalog['categories'], category)

    if exist:
        cati = mp.get(catalog['categories'], category)
        cat_id = me.getValue(cati)
    else:
        cat_id = 0
    
    return cat_id

def getVideosByCatLikes(catalog, category):
    vid_cat = getCat(catalog, category)
    if vid_cat != 0:
        exist = mp.contains(catalog['video_category'], vid_cat)
        if exist:
            entry = mp.get(catalog{'video_categry'}, vid_cat)
            li = me.getValue(entry)
     
    return li   





# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
