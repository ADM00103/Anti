import requests

services = [
 'autheasypayua', 'ionua', 'sloncreditua', 'backzecreditcomua', 'ontaxicomua',
 'ukloncomua_two', 'partner_uklo_two', 'alloua', 'n17459yclientscom', 'passporttwitchtv_two',
 'apiiconjob_co_two', 'ggbetru', 'durexrubackendprod', 'wwwdnsshopru_two', 'almatyinstashopkz', 'gdz_ruwork',
 'smotrimru', 'wwwriglaru', 'wwwriglaru', 'apteka_one', 'loymaxivoinru', 'amurfarmaru', 'kulinaristamarket', 'aptekamagnitu', 'autodozvon',
 'htvplatform24tv', 'apilike_videocom', 'x80aaiccccwa6aik', 'mydrom_ru', 'x80aaiccccwa6aik', 'harabaru', 'zaimbistrodengi', 'passrutuberu', 'mobileapiqiwicom',
 'medicina360ru', 'apieldoradoua_two', 'x80aaiccccwa6aik', 'wwwutairru', 'aistaxi', 'wowworks2',
'farmacia24', 'carte', 'delivio', 'www360', 'turbosms', 'smsint2', 'dtrparts', 'eshko',
 'alfalife', 'alpari', 'api_prime', 'apteka', 'artonline', 'avtobzvon', 'bamperby', 'bartokyo',
  'beeline_kz', 'beltelecom', 'benzuber', 'bluefin', 'boosty', 'buzzolls', 'cabinet_wi_fi', 'callmyphone',
   'carsmile', 'chibbis', 'cian', 'cinema5', 'citilink', 'citrus', 'city24', 'cleversite', 'cloudmailru',
    'comfy_ua', 'creditter', 'delitime', 'derevenskoe', 'dgtl', 'dianet', 'dns_shop', 'e_vse', 'easypay',
     'edame', 'edostav', 'eldorado', 'esk_ural', 'etm', 'farpost', 'finam', 'findclone', 'fixprice', 'flipkart',
      'foodband', 'foxtrot', 'friendsclub', 'gazprom', 'getmancar', 'ginzadelivery', 'gnevskii', 'grabtaxi', 'grinica',
       'groshi', 'gurutaxi', 'hatimaki', 'helsi', 'hmara', 'icq', 'icqcom', 'id_ykt', 'ievaphone', 'imgur', 'indriver',
        'ingos', 'invitro', 'iqlab', 'ivi', 'iwant', 'izi', 'kant', 'karusel', 'kaspi', 'kasta', 'kfc', 'kilovkusa',
         'kinolab', 'koronapay', 'krista', 'kvivstart', 'lenta', 'levin', 'limetaxi', 'loany', 'logistic', 'macdonal',
          'makarolls', 'makimaki', 'menuau', 'menzacafe', 'mistercash', 'mngogomenu', 'mobileplanet', 'modulbank',
           'molbulak', 'moneymanu', 'monobank', 'moscow', 'mospizza', 'moyo', 'mtstv', 'multiplex', 'mygames', 'nb99',
            'niyama', 'nl', 'nncard', 'pravdop', 'planeta_tc', 'widgetsbinotelcom', 'freefoodcomua', 'call2friends',
             'wwwhyundai_vostokru', 'perevozimvse', 'an_telecom', 'notecash', 'nova', 'oauth_av', 'ok', 'okean', 'oldi',
              'ollis', 'online_sbis', 'onlineua', 'oyorooms', 'ozon', 'panda99', 'panpizza', 'pikru', 'pirogin', 'pizza46',
               'pizza_33', 'pizzakaz', 'pizzasinizza', 'planetak', 'plink_tech', 'pliskov', 'pomodoro', 'privatebank',
                'prosushi', 'protovar', 'qbbox', 'qiwi', 'qlean', 'raiffeisen', 'rbt', 'remontnik', 'rendesvouz', 'richfamely',
                 'rieltor', 'rutaxi', 'rutaxi_ru', 'rutube', 'samaraetagi', 'sayoris', 'sedi', 'shafa', 'shopandshow', 'signalis',
                  'sipnet', 'smartomato', 'smartspace', 'sms4', 'smsint', 'sovest', 'sportmasterua', 'sravni', 'startpizza', 'studio',
                   'suandi', 'sumaster', 'sunlignt', 'sushifuji', 'sushigour', 'sushiprof', 'sushiroll', 'bigd_host', 'cian',
                    'sushiwokru', 'bettery_ru', 'pass_media', 'sushivesla', 'syzran', 'tabasko', 'tabris', 'tanuki', 'tarantionofamely',
                     'taxi310', 'taziritm', 'tehnosvit', 'tele2', 'telegram', 'thehive', 'tiktok', 'tinder', 'tinkoff', 'topladeba',
                      'topshop', 'tvoaapteka', 'zaymer', 'twitch', 'ubepmsmorg', 'ubki', 'uklon', 'ulabka', 'uralsib', 'uteka', 'utrair',
                       'vezitaxi', 'viza', 'vks', 'vladimirvilkinetru', 'vodafone', 'api_sushisellru', 'sergiopizza', 'unicom24',
                        'zoloto585_2', 'mymodulbank', 'tvmtsru', 'wwwtanukiru', 'cashucom', 'apizenkyio', 'sbguestsushiboxorg',
                         'apipapajohnsru', 'pizzaboxru', 'burgerking', 'kakvkusno_ru', 'igooodsru', 'starboxvrn', 'rollserv',
                          'igooods_two', 'zoopt_two', 'yobidoyobi', 'sberfood', 'lbelkacaru_two', 'broniboyru', 'yakitoriyaru',
                           'antisushiru', 'newtelnet', 'ulyanovsk', 'retailkbkbappru', 'loyalty_apidixyru', 'utkonos',
                            'appsmapisportmasterru', 'apidetmirru', 'apizakazakaru', 'autoriacom', 'wwwyakabooua', 'biuaapiv',
                             'kharkovestate', 'ieltorua', 'hh_ru', 'phonetua', 'uslugiru', 'docservisinua', 'mylugacomcom',
                              'mybankby', 'qlean_two', 'taxi7788', 'ibpsbankru', 'wwwvprokru', 'authorization_front_api',
                               'apimarkethomecredit', 'onlinehomecreditru', 'mvideo_two_or_one', 'apistartru', 'admineurogroshicomua',
                                'moneycasecomua', 'admintopcreditua', 'admin1groshivsimcom', 'perifyskorozvonru', 'nalog', 'baptekaru',
                                 'webbank', 'disk_apimegafonru', 'x80aaiccccwa6aik', 'wifimetro', 'work', 'wowworks', 'yandexeda',
                                  'yapochink', 'youla', 'zaminka', 'zoopt', 'salampay', 'taxi3040', 'vsk', 'taxi3040', 'apteka24ua', 'anc']




