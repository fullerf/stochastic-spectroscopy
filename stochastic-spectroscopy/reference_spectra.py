# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
from scipy.interpolate import UnivariateSpline

__all__ = ['ferro_spline', 'ferri_spline']

# digitized using WebPlotDigitizer
# from figure 2a, of 
# `X‐ray Spectroscopic Study of Solvent Effects on the Ferrous and
# Ferric Hexacyanide Anions`
ferro_cyanide_reference = np.array(
    [
        [7.095, 0.0], #added by me
        [7.100, 0.0], #added by me
        [7.105, 0.0], #added by me
        [7.106, 0.0], #added by me
        [7.107, 0.0], #added by me
        [7.108, 0.0], #added by me
        [7.109, 0.0], #added by me
        [7.109769204980843, -0.0005164529015979635],
        [7.110969300766284, -0.0005164529015979635],
        [7.112169396551724, 0.0007081963452861828],
        [7.113314942528736, 0.013553406223717479],
        [7.114460488505747, 0.02819476833091228],
        [7.115406018518518, 0.030167814339781218],
        [7.115769683908046, 0.06384566862910002],
        [7.117419815613027, 0.10294939944280901],
        [7.118497174329502, 0.09895228037311732],
        [7.119697270114942, 0.1132398549201008],
        [7.120897365900383, 0.1363721184723603],
        [7.122097461685824, 0.14276750898386736],
        [7.123297557471264, 0.1639947625965288],
        [7.12417035440613, 0.19915580319596282],
        [7.1247158524904215, 0.23477948906644253],
        [7.125108611111111, 0.27459419680403685],
        [7.125414090038314, 0.31171467619848614],
        [7.125588649425287, 0.34624071348472096],
        [7.125850488505747, 0.3835607653490327],
        [7.12602504789272, 0.42008252733389395],
        [7.126243247126436, 0.45750236543313716],
        [7.126515996168582, 0.5058986893748247],
        [7.126734195402299, 0.5560412724278105],
        [7.126897844827586, 0.5996977502102607],
        [7.127072404214559, 0.6410092514718251],
        [7.127170593869732, 0.6812729972666106],
        [7.127334243295019, 0.7179444386038688],
        [7.127443342911877, 0.7591062605130362],
        [7.127661542145594, 0.8178554063288478],
        [7.127552442528735, 0.7867969407064761],
        [7.1278251915708815, 0.8706173780487805],
        [7.1279342911877395, 0.9087856129100085],
        [7.127988840996168, 0.9414656048500141],
        [7.128097940613027, 0.9783865117746006],
        [7.128207040229885, 1.0163052810485],
        [7.128343414750958, 1.0547229814970565],
        [7.128452514367816, 1.094388009882254],
        [7.128561613984674, 1.134427236648444],
        [7.128643438697318, 1.175963256938604],
        [7.128752538314176, 1.2128841638631904],
        [7.128861637931034, 1.2483082772638072],
        [7.128992557471264, 1.2948086627417998],
        [7.129210756704981, 1.3448015664423887],
        [7.129298036398467, 1.388009006167648],
        [7.1297126149425285, 1.48],
        [7.130770881226053, 1.4042242693439866],
        [7.1309345306513405, 1.3675528280067284],
        [7.131109090038314, 1.327139402859546],
        [7.131305469348659, 1.278044575273339],
        [7.131452753831417, 1.2395769817073172],
        [7.13158912835249, 1.203903402719372],
        [7.131698227969348, 1.172470738716008],
        [7.131807327586206, 1.132556244743482],
        [7.132003706896551, 1.0882511564339783],
        [7.132189176245211, 1.0365119936220915],
        [7.132352825670498, 0.9851220826324643],
        [7.132549204980843, 0.9457564129520606],
        [7.132723764367816, 0.8987570962994114],
        [7.132871048850575, 0.8616366169049622],
        [7.133116522988505, 0.8238425804247267],
        [7.133334722222222, 0.7838033536585366],
#         [7.133771120689655, 0.2644160008410428],
        [7.1335965613026815, 0.7460841568544996],
        [7.13383658045977, 0.7092630361648445],
        [7.134262068965517, 0.676408418313709],
#         [7.134971216475096, 0.2644160008410428],
        [7.134753017241379, 0.6377163057190917],
        [7.135625814176245, 0.5975205959935774],
#         [7.136116762452107, 0.2644160008410428],
        [7.1368259099616855, 0.5840494542778498],
        [7.137916906130268, 0.6058512346976919],
        [7.138680603448275, 0.6404105340622372],
        [7.139226101532567, 0.673938708999159],
        [7.139717049808429, 0.7108346693650126],
        [7.1401534482758615, 0.7471319123212784],
        [7.1405898467432944, 0.7879195358494533],
        [7.140971695402299, 0.8242167788057191],
        [7.141298994252874, 0.8576451675077096],
        [7.141626293103448, 0.8880799691617607],
        [7.142008141762452, 0.9252503416736754],
        [7.142444540229885, 0.9664121635828428],
        [7.142880938697318, 1.0045803984440707],
        [7.143317337164751, 1.037135657590412],
        [7.143808285440613, 1.0720857863751052],
        [7.144408333333333, 1.1043666333753857],
        [7.145172030651341, 1.1372337245058874],
        [7.146208477011494, 1.1683432171802126],
        [7.147408572796935, 1.1966462219970946],
        [7.1486086685823755, 1.215696321393073],
        [7.149808764367816, 1.221139206934781],
        [7.151008860153256, 1.2118863015138772],
        [7.152208955938697, 1.1977347991054363],
        [7.153324196466581, 1.177792671245678],
        [7.154124260323542, 1.1573364930847585],
        [7.1552637452107275, 1.141673078025843],
        [7.156463840996168, 1.1158193717027296],
        [7.157663936781609, 1.0881967275785611],
        [7.15886403256705, 1.0643841033335883],
        [7.160064128352491, 1.0363532427937916],
        [7.1612642241379305, 1.011996329994648],
        [7.162464319923371, 0.9845097580090221],
        [7.163664415708812, 0.9593364123786222],
        [7.164864511494253, 0.9385173751815888],
        [7.166064607279694, 0.9227330071106354],
        [7.1672647030651335, 0.9087175768407371],
        [7.168464798850574, 0.9021861141906874],
        [7.169555795019157, 0.9000543173535184],
        [7.130055555555556, 1.4804878048780488],
        [7.129611111111111, 1.453048780487805],
        [7.1305555555555555, 1.4454268292682928],
        [7.113722222222222, 0.026219512195121863],
        [7.114111111111111, 0.036890243902439],
        [7.115055555555555, 0.015548780487804947],
        [7.115944444444445, 0.08719512195121948],
        [7.116388888888888, 0.11158536585365852],
    ]
)
ferro_sort = np.argsort(ferro_cyanide_reference[:,0])
ferro_cyanide_reference = ferro_cyanide_reference[ferro_sort,:]
ferro_spline = UnivariateSpline(ferro_cyanide_reference[:,0], ferro_cyanide_reference[:,1])
ferro_spline.set_smoothing_factor(0.0001)
smooth_ferro_spline = UnivariateSpline(ferro_cyanide_reference[:,0], ferro_cyanide_reference[:,1])
smooth_ferro_spline.set_smoothing_factor(1e-2)

# +
# digitized using WebPlotDigitizer
# from figure 4a, of 
# `X‐ray Spectroscopic Study of Solvent Effects on the Ferrous and
# Ferric Hexacyanide Anions`

ferri_cyanide_reference = np.array([
[7.105, 0.0], #added by me
[7.106, 0.0], #added by me
[7.107, 0.0], #added by me
[7.108, 0.0], #added by me
[7.109, 0.0], #added by me
[7.109558914647689, -0.0003532465836775245],
[7.110776643591469, 0.010844049235102515],
[7.111994372535251, 0.006911542385623637],
[7.113212101479032, 0.004644701884943592],
[7.1144298304228135, 0.020561385691987732],
[7.115647559366595, 0.010521435563578763],
[7.116699234363496, 0.014090693470370397],
[7.1173634501510135, 0.05414572524165129],
[7.117861611991652, 0.09497045360947354],
[7.118747233041674, 0.11409219695839856],
[7.119964961985455, 0.1066895518822546],
[7.121182690929237, 0.10886448831170603],
[7.122400419873018, 0.1367184476184775],
[7.123618148816799, 0.15582765859405345],
[7.124669823813702, 0.17926345784850195],
[7.125334039601218, 0.21416533435318574],
[7.12577685012623, 0.25002985378576836],
[7.126230730914366, 0.2891767062349977],
[7.126496417229373, 0.32481888047707375],
[7.126717822491878, 0.3622186156449554],
[7.126939227754384, 0.4049623636819011],
[7.12716063301689, 0.45114154856324484],
[7.127404178805646, 0.5004499626334837],
[7.127650887526724, 0.5544042766992578],
[7.127824848804407, 0.6095282938637996],
[7.128068394593163, 0.677235380811816],
[7.127990902751287, 0.6335700855879128],
[7.128267659329419, 0.7293701583816735],
[7.128406037618484, 0.7724987547168894],
[7.128489064591924, 0.8132119101497538],
[7.128599767223177, 0.8483255315458198],
[7.128738145512243, 0.8854739230037498],
[7.1288488481434955, 0.9270767028836793],
[7.128931875116936, 0.9724976791773856],
[7.129042577748188, 1.0121918830326493],
[7.1291809560372545, 1.0495947512938681],
[7.129291658668508, 1.0938695376083294],
[7.12940236129976, 1.1369991783079914],
[7.1294853882732, 1.1816567241918314],
[7.129596090904452, 1.2198240672273624],
[7.129706793535705, 1.2559555958365833],
[7.129817496166958, 1.2931050316589592],
[7.129955874456024, 1.332798191149777],
[7.130066577087277, 1.370583818980375],
[7.130304587744471, 1.4234805648498745],
[7.13058, 1.4653810035163437],
[7.130979873795113, 1.4976605181964002],
[7.131671765240443, 1.4380868371156856],
[7.131810143529509, 1.4034727700461853],
[7.132031548792015, 1.3602033585715296],
[7.132186532475769, 1.3125594525549773],
[7.1323359810279605, 1.27316080383787],
[7.132474359317026, 1.2319303398828616],
[7.1326736240532815, 1.1888653453423936],
[7.132806467210785, 1.1403061583255583],
[7.13300573194704, 1.0951035586374647],
[7.133138575104543, 1.048300261563322],
[7.133337839840799, 1.00622772655568],
# [7.1338027908920605, 0.27009669948701487],
[7.133514964050803, 0.9570561242278386],
[7.133664412602994, 0.9184972489615841],
[7.1339134935233135, 0.874972316319194],
[7.134134898785819, 0.8360290105004473],
[7.134356304048325, 0.7955588438619681],
[7.134621990363332, 0.7557740936092554],
# [7.135020519835842, 0.2699119419223337],
[7.134854465888963, 0.7211055803399815],
[7.135297276413974, 0.6810087739908692],
[7.135795438254611, 0.6406045067489188],
# [7.13612754614837, 0.26987016734450253],
[7.136570356673381, 0.6042359770348019],
[7.13767738298591, 0.5851778449748468],
[7.138784409298438, 0.6022862646550218],
[7.139614679032834, 0.6382209885864598],
[7.1401681921890985, 0.67090037052015],
[7.1406110027141105, 0.7056197443379334],
[7.141053813239122, 0.7430111245902487],
[7.141496623764133, 0.7842196568918953],
[7.141884082973518, 0.820849695463236],
[7.142216190867276, 0.8539191475174256],
[7.142548298761035, 0.8880065067847701],
[7.142880406654793, 0.9220938660521146],
[7.143267865864178, 0.9608869574514097],
[7.1437106763891896, 1.0013320593431903],
[7.144153486914201, 1.0352880027511073],
[7.144651648754839, 1.0687074561432264],
[7.145315864542356, 1.1042800607937213],
[7.146256836908005, 1.138729794631096],
[7.14741921453616, 1.1694591171184374],
[7.148636943479941, 1.1913444386753453],
[7.149854672423722, 1.19990442944186],
[7.151072401367504, 1.195971922592381],
[7.152290130311285, 1.1828782508245066],
[7.153507859255066, 1.1567368593243719],
[7.154725588198847, 1.137952160864767],
[7.155943317142628, 1.1129212135971651],
[7.15716104608641, 1.087335044213297],
[7.158378775030191, 1.0610548471840957],
[7.159596503973972, 1.0357462888583608],
[7.160814232917754, 1.0101601194744925],
[7.162031961861534, 0.9880440883172893],
[7.163249690805316, 0.9653728350438197],
[7.164467419749097, 0.9464493310551482],
[7.165685148692878, 0.9294691044734089],
[7.16690287763666, 0.9167918492927342],
[7.168120606580441, 0.9095280097456568],
[7.169338335524222, 0.9071223637159103],
[7.17000255131174, 0.9083465487308109],
[7.111299589603283, 0.026328368995689466],
[7.110259917920657, -0.0008022094313808736],
[7.112558139534884, -0.0008889347753140431],
[7.113816689466485, 0.015667346359342194],
[7.115020519835841, 0.018640786722762703],
[7.116279069767442, 0.006517822574400478],
[7.117154582763338, 0.03365459566889495],
[7.117592339261286, 0.07439279353689687],
[7.1181395348837215, 0.11210799370208813],
[7.121751025991792, 0.12253774875461354],
[7.123009575923393, 0.1496600676251194],
])
ferri_sort = np.argsort(ferri_cyanide_reference[:,0])
ferri_cyanide_reference = ferri_cyanide_reference[ferri_sort,:]
ferri_spline = UnivariateSpline(ferri_cyanide_reference[:,0], ferri_cyanide_reference[:,1])
ferri_spline.set_smoothing_factor(0.0001)
# -




