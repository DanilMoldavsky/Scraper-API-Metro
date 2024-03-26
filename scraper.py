import requests
import json

def scrape_alcohol(size:int=30):
    cookies = {
        'metroStoreId': '10',
        '_slid_server': '6602c8f8baa0c756f0079b1b',
        'manual_input_tooltip': '1',
        'metro_api_session': 'ei2wVQx4CQ47TOFIhJSqrfjBCLwOwuyxcEnDkaw0',
        'metro_user_id': '3d833bb0f466ddddd698c1ae731ad41b',
        '_slid': '6602c8f8baa0c756f0079b1b',
        '_slfs': '1711458581054',
        '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1711465781%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1711465781',
        '_ga': 'GA1.1.408892245.1711458584',
        '_ym_uid': '1711458584209173533',
        '_ym_d': '1711458584',
        'tmr_lvid': '188bb80127be35a10f4e9cc1957a3df5',
        'tmr_lvidTS': '1711458584876',
        '_gcl_au': '1.1.1833441498.1711458585',
        'mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e7ae18a197c7f-0e6f7fdd80e389-26001b51-144000-18e7ae18a197c7f%22%2C%22%24device_id%22%3A%20%2218e7ae18a197c7f-0e6f7fdd80e389-26001b51-144000-18e7ae18a197c7f%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
        'mp_88875cfb7a649ab6e6e310368f37a563_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e7ae18a1d7c83-01e75ae3aa4a7a-26001b51-144000-18e7ae18a1d7c83%22%2C%22%24device_id%22%3A%20%2218e7ae18a1d7c83-01e75ae3aa4a7a-26001b51-144000-18e7ae18a1d7c83%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
        '_ym_isad': '1',
        'uxs_uid': '1e271160-eb72-11ee-a6db-a3e525a8cb7f',
        'mindboxDeviceUUID': 'efef14e6-832b-4699-bf8d-d743924846b4',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22efef14e6-832b-4699-bf8d-d743924846b4%22%7D',
        '_slsession': '68944495-2D00-4933-89BF-3896FD016B75',
        'name_highlight': '1',
        '_ga_VHKD93V3FV': 'GS1.1.1711462955.2.1.1711463030.0.0.0',
    }

    headers = {
        'authority': 'api.metro-cc.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'metroStoreId=10; _slid_server=6602c8f8baa0c756f0079b1b; manual_input_tooltip=1; metro_api_session=ei2wVQx4CQ47TOFIhJSqrfjBCLwOwuyxcEnDkaw0; metro_user_id=3d833bb0f466ddddd698c1ae731ad41b; _slid=6602c8f8baa0c756f0079b1b; _slfs=1711458581054; _slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1711465781%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1711465781; _ga=GA1.1.408892245.1711458584; _ym_uid=1711458584209173533; _ym_d=1711458584; tmr_lvid=188bb80127be35a10f4e9cc1957a3df5; tmr_lvidTS=1711458584876; _gcl_au=1.1.1833441498.1711458585; mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e7ae18a197c7f-0e6f7fdd80e389-26001b51-144000-18e7ae18a197c7f%22%2C%22%24device_id%22%3A%20%2218e7ae18a197c7f-0e6f7fdd80e389-26001b51-144000-18e7ae18a197c7f%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; mp_88875cfb7a649ab6e6e310368f37a563_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e7ae18a1d7c83-01e75ae3aa4a7a-26001b51-144000-18e7ae18a1d7c83%22%2C%22%24device_id%22%3A%20%2218e7ae18a1d7c83-01e75ae3aa4a7a-26001b51-144000-18e7ae18a1d7c83%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ym_isad=1; uxs_uid=1e271160-eb72-11ee-a6db-a3e525a8cb7f; mindboxDeviceUUID=efef14e6-832b-4699-bf8d-d743924846b4; directCrm-session=%7B%22deviceGuid%22%3A%22efef14e6-832b-4699-bf8d-d743924846b4%22%7D; _slsession=68944495-2D00-4933-89BF-3896FD016B75; name_highlight=1; _ga_VHKD93V3FV=GS1.1.1711462955.2.1.1711463030.0.0.0',
        'origin': 'https://online.metro-cc.ru',
        'referer': 'https://online.metro-cc.ru/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    json_data = {
        'query': '\n  query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\n    category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {\n      id\n      name\n      slug\n      id\n      parent_id\n      meta {\n        description\n        h1\n        title\n        keywords\n      }\n      disclaimer\n      description {\n        top\n        main\n        bottom\n      }\n#      treeBranch {\n#        id\n#        name\n#        slug\n#        children {\n#          category_type\n#          id\n#          name\n#          slug\n#          children {\n#            category_type\n#            id\n#            name\n#            slug\n#            children {\n#              category_type\n#              id\n#              name\n#              slug\n#              children {\n#                category_type\n#                id\n#                name\n#                slug\n#              }\n#            }\n#          }\n#        }\n#      }\n      breadcrumbs {\n        category_type\n        id\n        name\n        parent_id\n        parent_slug\n        slug\n      }\n      promo_banners {\n        id\n        image\n        name\n        category_ids\n        virtual_ids\n        type\n        sort_order\n        url\n        is_target_blank\n        analytics {\n          name\n          category\n          brand\n          type\n          start_date\n          end_date\n        }\n      }\n\n\n      dynamic_categories(from: 0, size: 9999) {\n        slug\n        name\n        id\n        category_type\n        dynamic_product_settings {\n          attribute_id\n          max_value\n          min_value\n          slugs\n          type\n        }\n      }\n      filters {\n        facets {\n          key\n          total\n          filter {\n            id\n            hru_filter_slug\n            is_hru_filter\n            name\n            display_title\n            is_list\n            is_main\n            text_filter\n            is_range\n            category_id\n            category_name\n            values {\n              slug\n              text\n              total\n            }\n          }\n        }\n      }\n      total\n      prices {\n        max\n        min\n      }\n      pricesFiltered {\n        max\n        min\n      }\n      products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters)  {\n        health_warning\n        limited_sale_qty\n        id\n        slug\n        name\n        name_highlight\n        article\n        main_article\n        main_article_slug\n        is_target\n        category_id\n        url\n        images\n        pick_up\n        rating\n        icons {\n          id\n          badge_bg_colors\n          rkn_icon\n          caption\n          image\n          type\n          is_only_for_sales\n          stores\n          caption_settings {\n            colors\n            text\n          }\n          stores\n          sort\n          image_png\n          image_svg\n          description\n          end_date\n          start_date\n          status\n        }\n        manufacturer {\n          id\n          image\n          name\n        }\n        packing {\n          size\n          type\n          pack_factors {\n            instamart\n          }\n        }\n        stocks {\n          value\n          text\n          eshop_availability\n          scale\n          prices_per_unit {\n            old_price\n            offline {\n              price\n              old_price\n              type\n              offline_discount\n              offline_promo\n            }\n            price\n            is_promo\n            levels {\n              count\n              price\n            }\n            online_levels {\n              count\n              price\n              discount\n            }\n            discount\n          }\n          prices {\n            price\n            is_promo\n            old_price\n            offline {\n              old_price\n              price\n              type\n              offline_discount\n              offline_promo\n            }\n            levels {\n              count\n              price\n            }\n            online_levels {\n              count\n              price\n              discount\n            }\n            discount\n          }\n        }\n      }\n    }\n  }\n',
        'variables': {
            'storeId': 10,
            'sort': 'default',
            'size': size,
            'from': 0,
            'filters': [
                {
                    'field': 'main_article',
                    'value': '0',
                },
            ],
            'attributes': [],
            'in_stock': False,
            'eshop_order': False,
            'allStocks': False,
            'slug': 'krepkiy-alkogol',
        },
    }

    response = requests.post('https://api.metro-cc.ru/products-api/graph', cookies=cookies, headers=headers, json=json_data)
    print(response.status_code)
    
    return response.json()
    

def valid_products(products:json):
    pass


def main():
    response = scrape_alcohol(100)
    products = []
    result = {
        'products': products
    }
    
    # with open('data.json', 'w', encoding='utf-8') as file:
    #     json.dump(response, file, indent=4, ensure_ascii=False)
    
    # with open('data.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)
        
    #     print(len(data['data']['category']['products']))
    #     print(data['data']['category']['products'])

if __name__ == '__main__':
    main()